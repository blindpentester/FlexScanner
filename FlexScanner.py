import socket
import threading
import logging
from queue import Queue, Empty
import ipaddress
import argparse
import sys
import json
from concurrent.futures import ThreadPoolExecutor
import requests
from datetime import datetime
import ssl
import multiprocessing
import signal



# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
shutdown_flag = threading.Event()


# Constants and Global Variables
TARGET_PORTS = [443, 22, 21, 23, 25, 139, 445]  # Common ports to scan starting from 443
import multiprocessing
THREADS = multiprocessing.cpu_count() * 2  # Example to set threads based on CPU cores
SCAN_QUEUE = Queue()  # Queue to hold scan tasks (IP, port)
RESULTS = []  # Store scan results
LOCK = threading.Lock()  # Thread lock for thread-safe operations on shared data

def signal_handler(signum, frame):
    print("Signal received, shutting down...")
    # Perform any cleanup here
    sys.exit(0)


def is_valid_cidr(cidr):
    try:
        ipaddress.ip_network(cidr)
        return True
    except ValueError:
        return False


def is_valid_port(port):
    return 1 <= port <= 65535

def validate_port_ranges(ports):
    for part in ports.split(','):
        if '-' in part:
            start, end = part.split('-')
            if not (is_valid_port(int(start)) and is_valid_port(int(end))):
                return False
        else:
            if not is_valid_port(int(part)):
                return False
    return True




# Function to be able to name your own ports with --ports arg
def parse_ports(ports):
    parsed_ports = []
    for part in ports.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            parsed_ports.extend(range(start, end + 1))
        else:
            parsed_ports.append(int(part))
    return parsed_ports

import ssl

def grab_banner(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=4) as sock:
            if port == 443:
                # Wrap socket for SSL/TLS for HTTPS
                context = ssl.create_default_context()
                with context.wrap_socket(sock, server_hostname=ip) as ssock:
                    ssock.send(b'GET / HTTP/1.1\r\nHost: ' + ip.encode() + b'\r\n\r\n')
                    return ssock.recv(1024).decode('utf-8').strip()
            else:
                # Regular banner grab for other services
                sock.send(b'GET / HTTP/1.1\r\nHost: ' + ip.encode() + b'\r\n\r\n')
                return sock.recv(1024).decode('utf-8').strip()
    except Exception as e:
        logging.error(f"Error grabbing banner for {ip}:{port}: {e}")
        return None




def print_output(result, output_format):
    """Prints the scan result in the specified output format."""
    if output_format == "json":
        print(json.dumps(result))  # Print result in JSON format
    else:
        # TXT output
        output = f"Host: {result['host']}, Port: {result['port']}, Status: {result['status']}"
        if result['http_headers']:
            output += f", HTTP Headers: {result['http_headers']}"
        if result['banner']:
            output += f", Banner: {result['banner']}"
        print(output)  # Print result in TXT format



def scan_host(ip, port, output_format):
    """Scan a single host/port and return the result"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(4)  # Adjust as necessary
            sock.connect((ip, port))
            status = "open"  # Set the status to 'open' upon successful connection
            http_headers = {}
            banner = None

            if port in [80, 443]:  # If an HTTP(s) port is open
                try:
                    response = requests.get(f"http://{ip}:{port}", timeout=1)
                    http_headers = dict(response.headers)
                except requests.RequestException:
                    # Keep things blank if they fail.
                    pass

            # Attempt to grab the banner if the port is open
            if status == "open":
                banner = grab_banner(ip, port)

            result = {
                "host": ip,
                "port": port,
                "status": status,
                "http_headers": http_headers,
                "banner": banner  # Include the banner in the result
            }
            print_output(result, output_format)  # Use the function for printing

            return result

            result = {"host": ip, "port": port, "status": status, "http_headers": http_headers}        
            print_output(result, output_format)  # Use the new function for printing

    except socket.timeout:
        return {"host": ip, "port": port, "status": "filtered"}
    except ConnectionRefusedError:
        return {"host": ip, "port": port, "status": "closed"}
    except Exception as e:
        logging.error(f"Error scanning {ip}:{port}: {e}")
        return {"host": ip, "port": port, "status": "error"}

def signal_handler(signum, frame):
    print("Signal received, initiating graceful shutdown...")
    shutdown_flag.set()


def worker(output_format):
    while not shutdown_flag.is_set():
        try:
            ip, port = SCAN_QUEUE.get(timeout=0.1)  # Use a timeout to periodically check the flag     
            scan_host(ip, port, output_format)
            SCAN_QUEUE.task_done()
        except Empty:
            continue
    print(f"Worker thread ending.")



def setup_arg_parser():
    parser = argparse.ArgumentParser(description="Multithreaded Port Scanner with CIDR support")       
    parser.add_argument("cidr", type=str, help="CIDR block to scan, e.g., 192.168.1.0/24")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads to use (default: 10)")
    parser.add_argument("--ports", type=str, default="443,22,21,23,25,139,445", help="Ports to scan, comma-separated and/or ranges (default: 443,22,21,23,25,139,445)")
    parser.add_argument("--output", type=str, default="json", choices=["json", "txt"], help="Output format (default: json)")
    parser.add_argument("--output-file", type=str, help="Output file (default: results-<timestamp>.txt)")
    return parser




def main():

    # Register the signal handler
    signal.signal(signal.SIGINT, signal_handler)

    global TARGET_PORTS

    parser = setup_arg_parser()
    args = parser.parse_args()

    # Validate CIDR block
    if not is_valid_cidr(args.cidr):
        logging.error(f"Invalid CIDR block: {args.cidr}")
        sys.exit(1)  # Exit the script

    # Validate Ports
    if not validate_port_ranges(args.ports):
        logging.error(f"Invalid port range: {args.ports}")
        sys.exit(1)  # Exit the script

    if args.ports:
        TARGET_PORTS = parse_ports(args.ports)

    try:
        network = ipaddress.ip_network(args.cidr)
        for ip in network.hosts():
            for port in TARGET_PORTS:
                SCAN_QUEUE.put((str(ip), port))
    except ValueError as e:
        logging.error(f"Invalid CIDR block: {args.cidr}")
        return

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for _ in range(args.threads):
            executor.submit(worker, args.output)  # Pass the output format to the worker

if __name__ == "__main__":
    main()
