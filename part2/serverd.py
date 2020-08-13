import socket                
import sys
import threading
import csv

def fun(c):
   username=c.recv(1024).decode("utf-8")
   c.send(bytes("Username recieved","utf-8"))
   print('Username recieved-',username)
   
   password=c.recv(1024).decode("utf-8")               
   c.send(bytes("Password recieved","utf-8"))
   print('Password recieved-',password)

   found=0
   count=0
   with open("attendance.csv",'r') as csvfile:
   	csvreader=csv.reader(csvfile,delimiter=',')
   	line_count=0
   	for row in csvreader:
         if line_count != 0:
            if (username ==row[1]):
               found = 1
               for i in range(2,10):
                  if(row[i]=="Done"):
                     count+=1
         else:
            line_count+=1
   if(found==1 and count>6):
      c.send(bytes("Login Success","utf-8"))
   else:
      c.send(bytes("Login failed","utf-8"))

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
   