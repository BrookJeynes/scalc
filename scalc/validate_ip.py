import ipaddress

def validate_ip(address):
    try: 
        ipaddress.ip_address(address)
        return True
    except:
        return False