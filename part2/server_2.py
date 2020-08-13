import socket                
import sys
import threading
import csv
import random 
import time

def check_in_a(hostname,username,password,framesize):
   socket_a = socket.socket()
   print("Socket to connect with server A successfully created for Authentication")
   port_a = 11111
   socket_a.connect((hostname, port_a))
   msg_a = socket_a.recv(1024)      #Thankyou for connecting
   print(msg_a.decode("utf-8"))

   socket_a.send(bytes(username,"utf-8"))
   msg_a = socket_a.recv(1024)   #username recieved
   print(msg_a.decode("utf-8"))

   socket_a.send(bytes(password,"utf-8"))
   msg_a = socket_a.recv(1024)   #password recieved
   print(msg_a.decode("utf-8"))

   type="Authentication"
   socket_a.send(bytes(type,"utf-8"))
   msg_a = socket_a.recv(1024)   #type recieved
   #print(msg_a.decode("utf-8"))

   acknowledgement_a = socket_a.recv(1024)
   #socket_a.close()
   result_a = acknowledgement_a.decode("utf-8")
   if result_a == "Login Success":
      print("SUCCESS")
      socket_a.close()
      return 1
   else:
      print("FAILURE")
      socket_a.close()
      return 0

def check_in_b(hostname,username,password,framesize):
   socket_b = socket.socket()
   print("Socket to connect with server B successfully created for Authentication")
   port_b = 22222
   socket_b.connect((hostname, port_b))
   msg_b = socket_b.recv(1024)
   print(msg_b.decode("utf-8"))
   
   socket_b.send(bytes(username,"utf-8"))
   msg_b = socket_b.recv(1024)
   print(msg_b.decode("utf-8"))

   socket_b.send(bytes(password,"utf-8"))
   msg_b = socket_b.recv(1024)
   print(msg_b.decode("utf-8"))

   type="Authentication"
   socket_b.send(bytes(type,"utf-8"))
   msg_b = socket_b.recv(1024)   #type recieved
   #print(msg_b.decode("utf-8"))

  
   acknowledgement_b = socket_b.recv(1024)
   
   result_b = acknowledgement_b.decode("utf-8")
   
   if result_b == "Login Success":
      print("SUCCESS")
      socket_b.close()
      return 1
   else:
      print("FAILURE")
      socket_b.close()
      return 0


def check_in_c(hostname,username,password,framesize):
   socket_c = socket.socket()
   print("Socket to connect with server C successfully created for Authentication")
   port_c = 33333
   socket_c.connect((hostname, port_c))
   msg_c = socket_c.recv(1024)
   print(msg_c.decode("utf-8"))

   socket_c.send(bytes(username,"utf-8"))
   msg_c = socket_c.recv(1024)
   print(msg_c.decode("utf-8"))

   socket_c.send(bytes(password,"utf-8"))
   msg_c = socket_c.recv(1024)
   print(msg_c.decode("utf-8"))

   type="Authentication"
   socket_c.send(bytes(type,"utf-8"))
   msg_c = socket_c.recv(1024)   #password recieved
   #print(msg_c.decode("utf-8"))

   acknowledgement_c = socket_c.recv(1024)
   #socket_c.close()
   result_c = acknowledgement_c.decode("utf-8")

   if result_c == "Login Success":
      print("SUCCESS")
      socket_c.close()
      return 1    
   else:
      print("FAILURE")
      socket_c.close()
      return 0

def transfer_to_a(hostname,username,password,framesize):
   socket_a = socket.socket()
   print("Socket to connect with server A successfully created for File Transfer")
   port_a = 11111
   socket_a.connect((hostname, port_a))
   msg_a = socket_a.recv(1024)      #Thankyou for connecting
   #print(msg_a.decode("utf-8"))

   socket_a.send(bytes(username,"utf-8"))
   msg_a = socket_a.recv(1024)   #username recieved
   #print(msg_a.decode("utf-8"))

   socket_a.send(bytes(password,"utf-8"))
   msg_a = socket_a.recv(1024)   #password recieved
   #print(msg_a.decode("utf-8"))

   type="Transfer"
   socket_a.send(bytes(type,"utf-8"))
   msg_a = socket_a.recv(1024)   #type recieved
   #print(msg_a.decode("utf-8"))

   socket_a.send(framesize.encode())
   BUFFER_SIZE=(int)(framesize)
   filename='recieved_file.txt'
   f = open(filename,'rb')
   counter=1
   while True:
      l = f.read(BUFFER_SIZE)
      #print(l.decode("utf-8"))
      if not l:
    #     print("Sent1")
         f.close()
         break
      time.sleep((random.randint(1,10))/10)
      print("Frame ", counter, " sent to server A.")
      counter+=1
      socket_a.send(l)
      #print("sent")
   l="end"
   time.sleep((random.randint(1,10))/10)
   socket_a.send(bytes(l,'utf-8'))
   socket_a.close()
      
def transfer_to_b(hostname,username,password,framesize):
   socket_b = socket.socket()
   print("Socket to connect with server B successfully created for File Transfer")
   port_b = 22222
   socket_b.connect((hostname, port_b))
   msg_b = socket_b.recv(1024)      #Thankyou for connecting
   #print(msg_b.decode("utf-8"))

   socket_b.send(bytes(username,"utf-8"))
   msg_b = socket_b.recv(1024)   #username recieved
   #print(msg_b.decode("utf-8"))

   socket_b.send(bytes(password,"utf-8"))
   msg_b = socket_b.recv(1024)   #password recieved
   #print(msg_b.decode("utf-8"))

   type="Transfer"
   socket_b.send(bytes(type,"utf-8"))
   msg_b = socket_b.recv(1024)   #type recieved
   #print(msg_b.decode("utf-8"))

   socket_b.send(framesize.encode())
   BUFFER_SIZE=(int)(framesize)
   filename='recieved_file.txt'
   f = open(filename,'rb')
   counter=1
   while True:
      l = f.read(BUFFER_SIZE)
      #print(l.decode("utf-8"))
      if not l:
    #     print("Sent1")
         f.close()
         break
      time.sleep((random.randint(1,10))/10)
      print("Frame ", counter, " sent to server B.")
      counter+=1     
      socket_b.send(l)
      #print("sent")
   l="end"
   time.sleep((random.randint(1,10))/10)
   socket_b.send(bytes(l,'utf-8'))
   socket_b.close()

def transfer_to_c(hostname,username,password,framesize):
   socket_c = socket.socket()
   print("Socket to connect with server C successfully created for File Transfer.")
   port_c = 33333
   socket_c.connect((hostname, port_c))
   msg_c = socket_c.recv(1024)      #Thankyou for connecting
   #print(msg_c.decode("utf-8"))

   socket_c.send(bytes(username,"utf-8"))
   msg_c = socket_c.recv(1024)   #username recieved
   #print(msg_c.decode("utf-8"))

   socket_c.send(bytes(password,"utf-8"))
   msg_c = socket_c.recv(1024)   #password recieved
   #print(msg_c.decode("utf-8"))

   type="Transfer"
   socket_c.send(bytes(type,"utf-8"))
   msg_c = socket_c.recv(1024)   #type recieved
   #print(msg_c.decode("utf-8"))

   socket_c.send(framesize.encode())
   BUFFER_SIZE=(int)(framesize)
   filename='recieved_file.txt'
   f = open(filename,'rb')
   counter=1
   while True:
      l = f.read(BUFFER_SIZE)
      #print(l.decode("utf-8"))
      if not l:
    #     print("Sent1")
         f.close()
         break
      time.sleep((random.randint(1,10))/10)
      print("Frame ", counter, " sent to server C.")
      counter+=1
      socket_c.send(l)
      #print("sent")
   l="end"
   time.sleep((random.randint(1,10))/10)
   socket_c.send(bytes(l,'utf-8'))
   socket_c.close()


def check_d(hostname,username,password):
   socket_d = socket.socket()
   print("Socket to connect with server D successfully created for Exclusive Access Check.")
   port_d = 44444
   socket_d.connect((hostname, port_d))
   msg_d = socket_d.recv(1024)
   print(msg_d.decode("utf-8"))

   socket_d.send(bytes(username,"utf-8"))
   msg_d = socket_d.recv(1024)
   print(msg_d.decode("utf-8"))

   socket_d.send(bytes(password,"utf-8"))
   msg_d = socket_d.recv(1024)
   print(msg_d.decode("utf-8"))
   
   acknowledgement = socket_d.recv(1024)
   socket_d.close()
   result_d = acknowledgement.decode("utf-8")

   print(result_d)
   if result_d=="Login Success":
      return 1    
   else:
      return 0


def fun(c):
   hostname=c.recv(1024).decode("utf-8")

   username=c.recv(1024).decode("utf-8")
   c.send(bytes("Username recieved","utf-8"))
   print('Username recieved-',username)

   password=c.recv(1024).decode("utf-8")               
   c.send(bytes("Password recieved","utf-8"))
   print('Password recieved-',password)
   framesize=c.recv(1024).decode()
   BUFFER_SIZE=(int)(framesize)
   
   result_a = check_in_a(hostname,username,password,framesize)
   result_b = 0
   result_c = 0
   if result_a==0:
      result_b = check_in_b(hostname,username,password,framesize)
   if result_a==0 and result_b==0:
      result_c = check_in_c(hostname,username,password,framesize)
   result = result_a+result_b+result_c

   if result==0:
      c.send(bytes("Wrong Credentials, Authentication failed","utf-8"))
      c.send(bytes("No exclusive access","utf-8"))
   else:
      c.send(bytes("Authentication successful","utf-8"))
      filename='recieved_file.txt'
      
      #print ('file opened for writing')
      counter=1
      print('Recieving data...')
      with open('recieved_file.txt', 'ab') as f:
         while True:
            #f= open(filename, 'wb')
            data = c.recv(BUFFER_SIZE)
            #print("chalja")
            print('data=', data.decode("utf-8"))
            #print(data.decode("utf-8")[-3:])
            if(data.decode("utf-8")[-3:]!="end"):
          #     print("likhde")
               print("Frame ", counter, " recieved from client.")
               counter+=1
               f.write(data)
               #f.close()
           #    print("likhde1")
            else:
               
               f.write(data[: len(data) - 3])
               
               f.close()
               print ('File Recieved successfully from client.')
               break
      if(result_a==1):
         transfer_to_a(hostname,username,password,framesize)
      elif(result_b==1):
         transfer_to_b(hostname,username,password,framesize)
      elif(result_c==1):
         transfer_to_c(hostname,username,password,framesize)

      
      #f.close()
      result_d = check_d(hostname,username,password)
      if(result_d==1):
         c.send(bytes("User has Exclusive access","utf-8"))
      else:
         c.send(bytes("No exclusive access to this user","utf-8"))

   c.close()








s = socket.socket()          
print ("Socket successfully created")
  
port = (int)(sys.argv[1])               
  
s.bind(('192.168.56.1', port))         
print ("Socket binded to %s" %(port)) 
  
s.listen(5)      
print ("Socket is listening")            
  
while True:
   c, addr = s.accept()      
   print ('Got connection from', addr) 
   c.send(bytes("Thank you for connecting","utf-8")) 
   t1=threading.Thread(target=fun,args=(c,))
   # send a thank you message to the client.  
   t1.start()   

   # Close the connection with the client 
   