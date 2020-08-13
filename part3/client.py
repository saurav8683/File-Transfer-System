import socket                
import sys
import time

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
print(filename)
framesize=(str)(sys.argv[5])
corruption_pro=(str)(sys.argv[6])
corruption_prob=(int)(corruption_pro)
#s.send(bytes(framesize.encode()))
BUFFER_SIZE=(int)(framesize)
#corruption_prob = (float)(sys.argv[6])
s1.sendall(framesize.encode())

#fs_ack = s1.recv(1024).decode()
s2.sendall(framesize.encode())
#fs_ack = s2.recv(1024).decode()
s1.sendall(corruption_pro.encode())

#fs_ack = s1.recv(1024).decode()
s2.sendall(corruption_pro.encode())

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
	frame_number_attempted = 1
	frame_number_sent=0
	#frame_number_attempted = 1
	seq_num_1 = 0
	seq_num_2 = 0
	#print("hoja")
	frame = f.read(BUFFER_SIZE)
	while(frame):
		#print("send")
		
		print(frame)
		
		checksum = 0
		for i in range(0,len(frame.decode())):
			checksum += ord(frame.decode()[i])
			checksum = checksum % 65536
		checksum_str = str(checksum)
		#ack="negative"
		if(frame_number_attempted%2==1):		#send to server 1
			ack = "negative"
			#print("Sending to server 1")
			seq = (str)(seq_num_1)
			checksum_str = seq+checksum_str
			attempt = 0
			while ack=="negative":
				attempt += 1
				#print("counter : "+str(counter))
				s1.sendall(frame)
				if (frame_number_attempted%corruption_prob==0):		#corrupting the frame
					temp_checksum = checksum + 1
					temp_checksum_str = seq+str(temp_checksum)							
					s1.sendall(temp_checksum_str.encode())
					#frame_number_attempted+=1
					print("Frame "+str(frame_number_sent+1)+" sent to server 1 with checksum : "+ str(temp_checksum))
				
				else:													
					s1.sendall(checksum_str.encode())
					#print(checksum_str)
					frame_number_sent+=1
					print("Frame "+str(frame_number_sent)+" sent to server 1 with checksum : "+ str(checksum))
				
				if(attempt==1):
					seq_num_1 = (seq_num_1+1)%8
				#print("Frame "+str(frame_number_sent)+" sent to server 1 with checksum : "+ str(checksum))
				time.sleep(1)
				#print(ack)
				ack = s1.recv(1024).decode()
				ack_int = int(ack)
				#print(ack_int)
				if (ack_int==seq_num_1):
					ack = "positive"
					print("Frame sent Successfully")
				else:
					ack = "negative"
					print("Corrupted Frame")
				frame_number_attempted+=1
							#print("ack : "+ack)
		else:						#send to server 2
			#print("Sending to server2")
			ack = "negative"
			seq = (str)(seq_num_2)
			checksum_str = seq+checksum_str
			attempt = 0
			while ack=="negative":
				attempt += 1
				#print("counter : "+str(counter))
				s2.sendall(frame)
				if (frame_number_attempted%corruption_prob==0):		#corrupting the frame
					
					temp_checksum = checksum + 1
					temp_checksum_str = seq+str(temp_checksum)							
					s2.sendall(temp_checksum_str.encode())
					#frame_number_attempted+=1
					print("Frame "+str(frame_number_sent+1)+" sent to server 2 with checksum : "+ str(temp_checksum))
					#print("Corrupted frame")
				else:													
					s2.sendall(checksum_str.encode())
					frame_number_sent+=1
					print("Frame "+str(frame_number_sent)+" sent to server 2 with checksum : "+ str(checksum))
				
				if(attempt==1):
					seq_num_2 = (seq_num_2+1)%8
				time.sleep(1)
				ack = s2.recv(1024).decode()
				ack_int = int(ack)
				if (ack_int==seq_num_2):
					ack = "positive"
					print("Frame sent Successfully")
				else:
					ack = "negative"
					print("Corrupted Frame")
							#print("ack : "+ack)
				frame_number_attempted += 1
		frame = f.read(BUFFER_SIZE)
		#print('update frame',frame_number_attempted)
		
	#	print(sys.getsizeof(frame))
	frame1="end"
	frame2="end"
	s1.send(bytes(frame1.encode()))
	s2.send(bytes(frame2.encode()))
	print('Successfully sent the file')
	f.close()
exc = s1.recv(1024)	
print(exc.decode("utf-8"))
exc = s2.recv(1024)	
s1.close()
s2.close()