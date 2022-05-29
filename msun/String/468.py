"468. Validate IP Address"
class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def check_ipv4(pieces: list):
            if len(pieces) != 4:
                return False
            for each in pieces:
                try:
                    if int(each) > 255:
                        return False
                except ValueError:
                    return False
                    
                if len(each) > 1 and each[0] == '0':
                    return False
            return True

        def check_ipv6(pieces: list):
            if len(pieces) != 8:
                return False
            for each in pieces:
                if len(each) > 4:
                    return False
                for e in each:
                    if e not in '0123456789abcdefABCDEF':
                        return False
            return True

        if '.' in queryIP:
            if check_ipv4(queryIP.split('.')):
                return "IPv4"

        if ':' in queryIP:
            if check_ipv6(queryIP.split(':')):
                return "IPv6"

        return "Neither"