import socket

target = "216.158.227.108"

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port ))
        return True
    except:
        return False

print(portscan(80))         

