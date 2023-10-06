import socket
import json

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8080))

operation= input("Enter operation: Random/Add/Subtract: ")
num1= int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

request={"method":operation, "Num1":num1, "Num2":num2}
client.send(json.dumps(request).encode())

response_info=client.recv(1024).decode()
response=(json.loads(response_info))

if "error" in response:
    print(f"Error on server: {response['error']}") 
elif "Result is" in response:
    print(f"Response from server: {response['Result is']}")