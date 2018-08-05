import socket
import threading
from generate import get_reply
from affeni import get_sense

memory = [""]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('0.0.0.0',7800))

sock.listen(1)

def handler(Address, info, text):
	
	flick = get_sense(text) #determines if negetive or positive
	print(flick)
	texts = get_reply(text) #genarates commands from texts [command, sureity]

	if (flick == "positive") and (texts == None) and (memory[-1] != ""):
		reply = [memory[-1],""] #[command from memory, surity absolute]
	elif (flick == "negetive") and (texts == None) and (memory[-1] != ""): # yes no filter
		reply = ["Then tell me what are you asking about",""]
	elif (flick == "negetive") and (texts != None) and (texts[1] == ""):
		reply = ["ok i won't do that",""]
	else:
		reply = texts

	sendSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#sendSock.connect(('0.0.0.0',5000))
	sendSock.connect((Address,8080))
	#from here code checks if confusion exists in arrays second member
	#if exists sends confusion and if no confusion  it sends command to phone
	if (reply != None and reply[1] == ""):
		sendSock.send((reply[0]).encode())
		print("I am sure about this answer sent: "+reply[0])
		memory.append("")

	elif (reply != None and reply[1] != ""):
		sendSock.send(reply[1].encode())
		print("I am not sure about this answer")
		memory.append(reply[0])

	elif (reply == None):
		sendSock.send("comm none".encode())
		print("I don't know about it.")

	print("memory:"+memory[-1])

while(True):
	Address, info = sock.accept()
	gettext = Address.recv(1024).decode()
	#print(info[1])
	addressThread = threading.Thread(target = handler , args = (info[0], info[1],gettext))
	addressThread.daemon = True
	addressThread.start()
