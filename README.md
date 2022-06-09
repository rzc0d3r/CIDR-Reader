# CIDR-Reader
Reads cidr ranges and turns them into an ip list

# Functions
isIP(ip: str) - checks the specified ip for correct syntax

isCIDR(cidr: str) - checks the specified cidr range for correct syntax

parseIP(ip: str) - parses the ip and outputs it as a list (the first element is the ip parts, the second is the netmask (if any))

cidr2ipfile(cidr: str, fd: file object) - Convert cidr range to ip and write to file. You need to specify the file object in Write mode

cidr2iplist(cidr: str) - Convert cidr range to ip and returns a list of received ips

# Constants
addresses_by_mask: int list - Stores the number of devices in the mask. To get data use addresses_by_mask[index_mask]
