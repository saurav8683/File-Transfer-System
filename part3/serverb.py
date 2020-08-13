import socket                
import sys
import threading
import csv

#BUFFER_SIZE = 1024

def fun(c):
   username=c.recv(1024).decode("utf-8")
   c.send(bytes("Username recieved","utf-8"))
   print('Username recieved-',username)

   password=c.recv(1024).decode("utf-8")
   c.send(bytes("Password recieved","utf-8"))
   print('Password recieved-',password)

   type=c.recv(1024).decode("utf-8")
   c.send(bytes("Type recieved","utf-8"))
   #print('Type recieved-',type)
   
   if(type=="Authentication"):
      found=0
      with open("login_credentials_b.csv",'r') as csvfile:
         csvreader=csv.reader(csvfile,delimiter=',')
         line_count=0
         #print("yes")
         for row in csvreader:
            if line_count != 0:
               if (username ==row[0]):
                  if password == row[1]:
                     found=1        
            else:
               line_count+=1
      print(found)
      if(found==0):
         c.send(bytes("Login Failed","utf-8"))
      else:
         c.send(bytes("Login Success","utf-8"))
   else:
      framesize=c.recv(1024).decode()
      BUFFER_SIZE=(int)(framesize)
      filename='recieved_file_b.txt'
      f= open(filename, 'wb')
      #print ('file opened for writing')
      counter=1
      seq_num=0
      print('Recieving data...')
      while True: 
         data = c.recv(BUFFER_SIZE)
         if(data.decode("utf-8")[-3:]!="end"):
            data_str = data.decode()
            checksum = 0
            for i in range(0,len(data_str)):
               checksum += ord(data_str[i])
               checksum = checksum % 65536
            extra_bits = c.recv(1024).decode()
            seq = int(extra_bits[:1])
            checksum_received = int(extra_bits[1:])
            print("seq : "+str(seq)+" CheckSum : "+str(checksum_received))
            ack = ''
            if (seq==seq_num and checksum==checksum_received):
               seq_num = (seq_num+1)%8
               str_seq_num = str(seq_num)
               ack = str_seq_num
               c.sendall(ack.encode())
               print("Frame Accepted")
               f.write(data)
            else:
               str_seq_num = str(seq_num)
               ack = str_seq_num
               print("Frame Corrupted")
               c.sendall(ack.encode())
         else:
            f.write(data[: len(data) - 3])
            f.close()
            print ('File Recieved successfully from client.')
            break
      
   c.close()

s = socket.socket()          
print ("Socket successfully created")
  
port = (int)(sys.argv[1])               
  
s.bind(('', port))         
print ("Socket binded to-%s" %(port)) 
  
s.listen(5)      
print ("Socket is listening")            
  
while True:
   c, addr = s.accept()      
   print ('Got connection from-', addr) 
   c.send(bytes("Thank you for connecting","utf-8")) 
   t1=threading.Thread(target=fun,args=(c,))
   # send a thank you message to the client.  
   t1.start()   

   # Close the connection with the client 
