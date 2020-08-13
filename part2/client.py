import socket                
import sys

# Create a socket object 
s1 = socket.socket() 
s2 = socket.socket()          
hostname=(str)(sys.argv[1])
port1=(int)(sys.argv[2])
port2=(int)(sys.argv[3])
# Define the port on which you want to connect 
      
  
# connect to the server on local computer 
s1.connect((hostname, port1)) 
s2.connect((hostname, port2)) 
  
# receive data from the server 
print (s1.recv(1024).decode("utf-8")) 
s1.send(bytes(hostname,'utf-8'))

username=input("Enter Username-")
s1.send(bytes(username,'utf-8'))
result1=s1.recv(1024).decode("utf-8")
print(result1)

password=input("Enter password-")
s1.send(bytes(password,'utf-8'))
result2=s1.recv(1024).decode("utf-8")
print(result2)

print (s2.recv(1024).decode("utf-8")) 
s2.send(bytes(hostname,'utf-8'))

s2.send(bytes(username,'utf-8'))
result1=s2.recv(1024).decode("utf-8")

s2.send(bytes(password,'utf-8'))
result2=s2.recv(1024).decode("utf-8")

filename=(str)(sys.argv[4])
framesize=(str)(sys.argv[5])
#s.send(bytes(framesize.encode()))
BUFFER_SIZE=(int)(framesize)
#corruption_prob = (float)(sys.argv[6])
s1.sendall(framesize.encode())
#fs_ack = s1.recv(1024).decode()
s2.sendall(framesize.encode())
#fs_ack = s2.recv(1024).decode()

result = s1.recv(1024)			#authentication result
print(result.decode("utf-8"))
result = s2.recv(1024)			#authentication result
#print(result.decode("utf-8"))
#if(result.decode("utf-8")=="Authentication successful"):
#	print('Successfully sent the file')
			#exclusive access result
#print(exc.decode("utf-8"))
# close the connection 
        
if(result.decode("utf-8")=="Authentication successful"):
	f = open(filename,'rb')
	frame_number = 1
	frame = f.read(BUFFER_SIZE)
	while(frame):
		
		if(frame_number%2==1):		#send to server 1
			s1.sendall(frame)
			print("Frame ",frame_number," sent to server 1")
		else:						#send to server 2
			s2.sendall(frame)
			print("Frame ",frame_number," sent to server 2")
		frame_number += 1
		frame = f.read(BUFFER_SIZE)
	
	#	print(sys.getsizeof(frame))
	frame1="end"
	frame2="end"
	s1.send(bytes(frame1.encode()))
	s2.send(bytes(frame1.encode()))
	print('Successfully sent the file')
	f.close()
exc = s1.recv(1024)	
print(exc.decode("utf-8"))
exc = s2.recv(1024)	
s1.close()
s2.close()