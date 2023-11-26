import socket
import struct

class UnrealUDPServer:
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.addr, self.port))
        
        self.sock.settimeout(0.1)
        
        
    def run(self):
            
        
        while True:
            try:
                data, addr = self.sock.recvfrom(1024)
            except:
                continue
            
            print("recv:", data)
            
            content = "hello Unreal!"
            
            buffer = struct.pack(">BB", 1, len(content))
            buffer += content.encode()
            
            self.sock.sendto(buffer, ("127.0.0.1", 8000))
            print("sent:", buffer)
            

    def close(self):
        self.sock.close()
        


server = UnrealUDPServer("127.0.0.1", 8000)

server.run()

server.close()
