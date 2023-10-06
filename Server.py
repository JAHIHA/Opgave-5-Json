import socket 
import threading
import random
import json

def handle_client(client_socket):
    try:
        info=client_socket.recv(1024).decode()
        request=json.loads(info)

        if "method" in request:
            method=request["method"]
            if method == "Random" and "Num1" in request and "Num2" in request:
                val1=request["Num1"]
                val2=request["Num2"]
                randomNumber= random.randint(val1,val2)
                response={"Result is": randomNumber}
            elif method =="Add" and "Num1" in request and "Num2" in request:
                val1=request["Num1"]
                val2=request["Num2"]
                result=val1+val2
                response={"Result is": result}
            elif method =="Subtract" and "Num1"in request and "Num2" in request:
                val1=request["Num1"]
                val2=request["Num2"]
                result=val1-val2
                response={"Result is": result}
            else:
                response={"error":"Invalid request"}
        else:
            response={"error":"Invalid request"}
        

        client_socket.send(json.dumps(response).encode())
    except Exception as e:
        print(f"Error handling client: {str(e)}")
    finally:
        client_socket.close()

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8080))
server.listen(2)
print("Server in running on port 8080")
while True:
    client_socket,addr=server.accept()
    print(f"Accepting adress from {addr[0]}:{addr[1]}")
    client_handler=threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()

