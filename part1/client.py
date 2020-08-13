import socket                
import sys

# Create a socket object 
s = socket.socket()          
hostname=(str)(sys.argv[1])
# Define the port on which you want to connect 
port=(int)(sys.argv[2])  
# connect to the server on local computer 
s.connect((hostname, port)) 
  
# recieve data from the server 
print (s.recv(1024).decode("utf-8")) 
s.send(bytes(hostname,'utf-8'))

username=input("Enter Username-")
s.send(bytes(username,'utf-8'))
result1=s.recv(1024).decode("utf-8")
print(result1)

password=input("Enter password-")
s.send(bytes(password,'utf-8'))
result2=s.recv(1024).decode("utf-8")
print(result2)

filename=(str)(sys.argv[3])
framesize=(str)(sys.argv[4])
s.send(bytes(framesize.encode()))
BUFFER_SIZE=(int)(framesize)

result = s.recv(1024)			#authentication result
print(result.decode("utf-8"))

if(result.decode("utf-8")=="Authentication successful"):
	f = open(filename,'rb')
	counter=1
	while True:
		l = f.read(BUFFER_SIZE)
		if not l:
			f.close()
			break
		s.send(l)
		print("Frame ", counter, " sent to main server.")
		counter+=1
	l="end"
	s.send(bytes(l.encode()))
	print('Successfully sent the file')
exc = s.recv(1024)				#exclusive access result
print(exc.decode("utf-8"))
# close the connection 
s.close()        