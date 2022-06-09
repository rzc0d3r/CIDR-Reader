def isIP(ip):
    try:
        if isCIDR(ip):
            parts = ip.split('/', 1)[0].split('.', 3)
            if len(parts) == 4:
                for part in parts:
                    part = int(part.strip())
                    if part < 0 or part > 255:
                        raise
                return True
        else:
            parts = ip.split('.', 3)
            if len(parts) == 4:
                for part in parts:
                    part = int(part)
                    if part < 0 or part > 255:
                        raise
                return True
    except:
        pass
    
def isCIDR(ip):
    try:
        ip, prefix = ip.split('/', 1)
        prefix = int(prefix.strip())
        if prefix >= 0 and prefix <= 32:
            return True
    except:
        pass

def parseIP(ip):
    if isCIDR(ip) and isIP(ip):
        res = []
        ip, mask = ip.split('/')
        for part in ip.split('.'):
            res.append(int(part.strip()))
        return res, int(mask.strip())
    elif isIP(ip):
        res = []
        for part in ip.split('.'):
            res.append(int(part.strip()))
        return res, None

addresses_by_mask = [
    4294967296, 2147483648, 1073741824, 536870912, 268435456, 134217728, 67108864,
    33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072,
    65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1
]
 
def cidr2ipfile(ip, fd):
    ip, mask = parseIP(ip)
    if mask is not None:
        for _ in range(addresses_by_mask[mask]):
            fd.write('{0}.{1}.{2}.{3}\n'.format(ip[0], ip[1], ip[2], ip[3]))
            if ip[3] < 255:
                ip[3] += 1
            else:
                ip[3] = 0
                if ip[2] < 255:
                    ip[2] += 1
                else:
                    ip[2] = 0
                    if ip[1] < 255:
                        ip[1] += 1
                    else:
                        ip[1] == 0
                        if ip[0] < 255:
                            ip[0] += 1
                        else:
                            break

def cidr2iplist(ip):
    ip, mask = parseIP(ip)
    res = []
    if mask is not None:
        for _ in range(addresses_by_mask[mask]):
            res.append('{0}.{1}.{2}.{3}'.format(ip[0], ip[1], ip[2], ip[3]))
            if ip[3] < 255:
                ip[3] += 1
            else:
                ip[3] = 0
                if ip[2] < 255:
                    ip[2] += 1
                else:
                    ip[2] = 0
                    if ip[1] < 255:
                        ip[1] += 1
                    else:
                        ip[1] == 0
                        if ip[0] < 255:
                            ip[0] += 1
                        else:
                            break
        return res
