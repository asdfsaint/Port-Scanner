Port Scanner

A lightweight multithreaded TCP port scanner written in Python. Scans a user-defined port range on a target host, identifies open ports, and attempts to grab service banners from open connections.

Built from scratch using only Python's standard library — no external dependencies.


Features


Multithreaded scanning for fast results
User-defined target IP, start port, and end port
Banner grabbing on open ports
Clean output — only reports open ports
No external libraries required



Requirements


Python 3.x


No pip installs needed. Uses only built-in Python modules (socket, threading).


Usage

bashpython portscanner.py

You will be prompted to enter:

Enter Target IP: 192.168.122.1
Enter Starting Port: 1
Enter Ending Port: 500


Example Output

Scanning 192.168.122.1 from port 1 to 500:
Port 53 is open
port 53 - no banner: timed out
Scan Complete for 192.168.122.1 from port 1 to 500.


How It Works


Creates a TCP socket for each port in the specified range
Attempts a connection using connect_ex() — returns 0 if the port is open
On an open port, attempts to receive a service banner using recv()
Each port is scanned in its own thread for speed
All threads are joined before printing the completion message



Legal Disclaimer

This tool is intended for educational purposes and authorized security testing only.
Only use this scanner against systems you own or have explicit written permission to test.
Unauthorized port scanning may be illegal in your jurisdiction.
The author assumes no liability for misuse of this tool.
