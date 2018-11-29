#!/usr/bin/python

import time
import easygopigo3
import socket
from threading import Timer
import threading

host = ''
port = 5560

storeValue = "Moro"
stopFlag = False
gpg = easygopigo3.EasyGoPiGo3()




def setupServer():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket created")
	try:
		s.bind((host, port))
	except socket.error as msg:
		print(msg)
	print("Socket bind complete")
	return s

def setupConnection():
	s.listen(20) #Allows one connection at a time.
	conn, address = s.accept()
	print("Connected to: " + address[0] + ":" + str(address[1]))
	return conn

def REPEAT(dataMessage):
	reply = dataMessage[1]
	return reply


def dataTransfer(conn):
	#loop that sends/receive data until not to
    while True:
            #Receive the data
		#if not data: break
        print("inwhileloop")
        data = conn.recv(1024) #receive the data
        data = data.decode('utf-8')
        dataMessage = data.split(' ', 1)

                    #split the data such that you separate the command from rest
        command = dataMessage[0]
        stopFlag = False
        if command == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif command == 'EXIT':
            print("Client left")
            break
        elif command == 'KILL':
            print("server shutting down")
            gpg.stop()
            s.close()
            break
        else:
            reply = "Unknow command"
            #send reply to client
            break
        conn.sendall(str.encode(reply))

        print("Data has been sent!")
        if dataMessage[1] == "87":
            gpg.forward()
        elif dataMessage[1] == "68":
            gpg.right()
        elif dataMessage[1] == "65":
            gpg.left()
        elif dataMessage[1] == "83":
            gpg.backward()
        elif dataMessage[1] == "STOP":
            print("stop this shit")
            gpg.stop()
            stopFlag = True
        else:
            print("elsessa")

    conn.close()


s = setupServer()


def main():

    gpg.stop()

    while True:

        try:
            conn = setupConnection()
            dataTransfer(conn)

        except:
            print("ERROR OCCURED")
            s.close()
            break

main() #start main

