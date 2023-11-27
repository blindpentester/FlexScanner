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
