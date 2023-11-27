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
for i in $(cat cf_cidrrs.txt);do ./FlexScanner --threads 200 --output json $i --ports 443; done

                  
2023-11-27 16:20:29,949 - ERROR - Error grabbing banner for 1.0.0.101:443: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:992)                                                         
{"host": "1.0.0.101", "port": 443, "status": "open", "http_headers": {"Server": "cloudflare", "Date": "Mon, 27 Nov 2023 23:20:28 GMT", "Content-Type": "text/html", "Content-Length": "253", "Connection": "close",
 "CF-RAY": "-"}, "banner": null}                                                                                                                                                                                   
2023-11-27 16:20:29,950 - ERROR - Error grabbing banner for 1.0.0.134:443: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:992)                                                         
{"host": "1.0.0.134", "port": 443, "status": "open", "http_headers": {"Server": "cloudflare", "Date": "Mon, 27 Nov 2023 23:20:28 GMT", "Content-Type": "text/html", "Content-Length": "253", "Connection": "close",
 "CF-RAY": "-"}, "banner": null}                                                                                                                                                                                   
2023-11-27 16:20:29,953 - ERROR - Error grabbing banner for 1.0.0.86:443: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:992)                                                          
{"host": "1.0.0.86", "port": 443, "status": "open", "http_headers": {"Server": "cloudflare", "Date": "Mon, 27 Nov 2023 23:20:28 GMT", "Content-Type": "text/html", "Content-Length": "253", "Connection": "close", 
"CF-RAY": "-"}, "banner": null}                                                                                                                                                                                    
2023-11-27 16:20:29,957 - ERROR - Error grabbing banner for 1.0.0.103:443: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:992)                                                         
{"host": "1.0.0.103", "port": 443, "status": "open", "http_headers": {"Server": "cloudflare", "Date": "Mon, 27 Nov 2023 23:20:28 GMT", "Content-Type": "text/html", "Content-Length": "253", "Connection": "close",
 "CF-RAY": "-"}, "banner": null}                                                                                                                                                                                   
2023-11-27 16:20:29,957 - ERROR - Error grabbing banner for 1.0.0.19:443: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:992)                                                          
{"host": "1.0.0.19", "port": 443, "status": "open", "http_headers": {"Server": "cloudflare", "Date": "Mon, 27 Nov 2023 23:20:28 GMT", "Content-Type": "text/html", "Content-Length": "253", "Connection": "close", 
"CF-RAY": "-"}, "banner": null}                                                                                                                                                                                    
2023-11-27 16:20:29,963 - ERROR - Error grabbing banner for 1.0.0.4:443: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:992)                                                           
{"host": "1.0.0.4", "port": 443, "status": "open", "http_headers": {"Server": "cloudflare", "Date": "Mon, 27 Nov 2023 23:20:28 GMT", "Content-Type": "text/html", "Content-Length": "253", "Connection": "close", "
CF-RAY": "-"}, "banner": null}                                                                                                                                                                                     
2023-11-27 16:20:29,966 - ERROR - Error grabbing banner for 1.0.0.13:443: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:992)                                                          
{"host": "1.0.0.13", "port": 443, "status": "open", "http_headers": {"Server": "cloudflare", "Date": "Mon, 27 Nov 2023 23:20:28 GMT", "Content-Type": "text/html", "Content-Length": "253", "Connection": "close", 
"CF-RAY": "-"}, "banner": null}                                                                                                                                                                                    
2023-11-27 16:20:29,978 - ERROR - Error grabbing banner for 1.0.0.89:443: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:992)                                                          
2023-11-27 16:20:29,978 - ERROR - Error grabbing banner for 1.0.0.14:443: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:992)                                                          
{"host": "1.0.0.89", "port": 443, "status": "open", "http_headers": {"Server": "cloudflare", "Date": "Mon, 27 Nov 2023 23:20:28 GMT", "Content-Type": "text/html", "Content-Length": "253", "Connection": "close", 
"CF-RAY": "-"}, "banner": null}                                                                                                                                                                                    
2023-11-27 16:20:30,008 - {"host": "1.0.0.3", "port": 443, "status": "open", "http_headers": {"Server": "cloudflare", "Date": "Mon, 27 Nov 2023 23:20:28 GMT", "Content-Type": "text/html", "Content-Length": "253", "Connection": "close", "
CF-RAY": "-"}, "banner": "HTTP/1.1 403 Forbidden\r\nDate: Mon, 27 Nov 2023 23:20:31 GMT\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Length: 16\r\nConnection: keep-alive\r\nReport-To: {\"endpoints\":[{\
"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=DIZU%2FMTwrh4zTLoy0tKVLLGKc06OVGKjHtVHScZol55ocfXKDfmy2X6L5aS410b4BwFeU2O%2FUJk8nNw9YZTlHjcsFzDLzECEsg3E7clxhdfyGsf0RmTHEbQ%3D\"}],\"group\":\"cf-nel\",\
"max_age\":604800}\r\nNEL: {\"report_to\":\"cf-nel\",\"max_age\":604800}\r\nReport-To: {\"endpoints\":[{\"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=lvPJxqvVM4Q6nTw0icf1V%2FXkNeWJUjdwDvflNtrJlF0B2F
BZTdf7OYL4BoLIr1v5krTyVGWGhdbdehtn2JzVIy%2B3pDygu7a%2Bs8Xe2Zy2iaN6voQ71AQLf1I%3D\"}],\"group\":\"cf-nel\",\"max_age\":604800}\r\nReport-To: {\"endpoints\":[{\"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/
v3?s=bPr1UEOIOQ7TeuTGQRdKPVUnIGv2V0vvb085ifJP3YsbBL1MPnyJBKjfZTCikkjFjSYD3sreIKUpceZcVizaJE8xqxD2Rh4GXJc6H1z2BDzpQz3LW%2BSqk8k%3D\"}],\"group\":\"cf-nel\",\"max_age\":604800}\r\nReport-To: {\"endpoints\":[{\"url
\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=jllC8NV6Tk8GNDoCqmUBMI"}                                                         
2023-11-27 16:20:30,014 - ERROR - Error grabbing banner for 1.0.0.112:443: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:992)
2023-11-27 16:20:30,085 - ERROR - Error grabbing banner for 1.0.0.79:443: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:992)
2023-11-27 16:20:30,016 - ERROR - Error grabbing banner for 1.0.0.130:443: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:992)
{"host": "1.0.0.14", "port": 443, "status": "open", "http_headers": {"Server": "cloudflare", "Date": "Mon, 27 Nov 2023 23:20:28 GMT", "Content-Type": "text/html", "Content-Length": "253", "Connection": "close", 
"CF-RAY": "-"}, "banner": null}
{"host": "1.0.0.112", "port": 443, "status": "open", "http_headers": {"Server": "cloudflare", "Date": "Mon, 27 Nov 2023 23:20:28 GMT", "Content-Type": "text/html", "Content-Length": "253", "Connection": "close",
 "CF-RAY": "-"}, "banner": null}
2023-11-27 16:20:30,016 - ERROR - Error grabbing banner for 1.0.0.135:443: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:992)
{"host": "1.0.0.130", "port": 443, "status": "open", "http_headers": {"Server": "cloudflare", "Date": "Mon, 27 Nov 2023 23:20:28 GMT", "Content-Type": "text/html", "Content-Length": "253", "Connection": "close",
 "CF-RAY": "-"}, "banner": null}
{"host": "1.0.0.17", "port": 443, "status": "open", "http_headers": {"Server": "cloudflare", "Date": "Mon, 27 Nov 2023 23:20:28 GMT", "Content-Type": "text/html", "Content-Length": "253", "Connection": "close", 
"CF-RAY": "-"}, "banner": null}
{"host": "1.0.0.79", "port": 443, "status": "open", "http_headers": {"Server": "cloudflare", "Date": "Mon, 27 Nov 2023 23:20:28 GMT", "Content-Type": "text/html", "Content-Length": "253", "Connection": "close", 
"CF-RAY": "-"}, "banner": null}

```
