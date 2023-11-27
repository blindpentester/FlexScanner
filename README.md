# FlexScanner
I built my own version of masscan for updating my MongoDB project, and i modified it to be an every day sort of scanner and removed the MongoDB part.

Enjoy.


```python
./FlexScanner --help
usage: FlexScanner [-h] [--threads THREADS] [--ports PORTS] [--output {json,txt}] [--output-file OUTPUT_FILE] cidr

Multithreaded Port Scanner with CIDR support

positional arguments:
  cidr                  CIDR block to scan, e.g., 192.168.1.0/24

options:
  -h, --help            show this help message and exit
  --threads THREADS     Number of threads to use (default: 10)
  --ports PORTS         Ports to scan, comma-separated and/or ranges (default: 443,22,21,23,25,139,445)
  --output {json,txt}   Output format (default: json)
  --output-file OUTPUT_FILE
                        Output file (default: results-<timestamp>.txt)
```
Example of usage:
```bash
for i in $(cat ovh3.txt);do ./FlexScanner --threads 100 --output json $i --ports 80,443,22,23,21,8443,8080,8181; done
{"host": "103.5.12.33", "port": 22, "status": "open", "http_headers": {}, "banner": "SSH-2.0-OpenSSH_7.8"}
{"host": "103.5.12.34", "port": 22, "status": "open", "http_headers": {}, "banner": "SSH-2.0-OpenSSH_7.8"}
{"host": "103.5.12.35", "port": 22, "status": "open", "http_headers": {}, "banner": "SSH-2.0-OpenSSH_7.8"}
{"host": "103.5.14.33", "port": 22, "status": "open", "http_headers": {}, "banner": "SSH-2.0-OpenSSH_6.6.1"}
{"host": "103.5.14.34", "port": 22, "status": "open", "http_headers": {}, "banner": "SSH-2.0-OpenSSH_6.6.1"}
{"host": "103.5.14.35", "port": 22, "status": "open", "http_headers": {}, "banner": "SSH-2.0-OpenSSH_6.6.1"}

```
