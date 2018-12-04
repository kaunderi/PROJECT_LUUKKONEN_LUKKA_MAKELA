#!/usr/bin/python

import time
import easygopigo3
import socket
from _thread import *
import sys

host = ''
port = 5560
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

def threaded_client(conn):

    manualControl = False

    print("threadissa")
    while True:

            data = conn.recv(1024)
            data = data.decode('utf-8')
            dataMessage = data.split(' ', 1)
            #split the data such that you separate the command from rest
            command = dataMessage[0]

            if command == 'REPEAT':
                reply = REPEAT(dataMessage)
            elif command == 'EXIT':
                print("Client left")
                break
            elif (command == 'KILL') or (not data) :
                print("server shutting down")
                gpg.stop()
                #s.close()
                break
            else:
                reply = "Unknow command"

            conn.sendall(str.encode("ok"))
            print("Data has been sent!")

            if dataMessage[1] == "CMD":
                manualControl = not manualControl

            if manualControl == True:
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
                else:
                    print("Manual Control ON")

    print("Thread killed")
    conn.close()

def openThread(s):
    while True:
            print("THREAD1")
            conn, addr = s.accept()
            print("connected to: " + addr[0] + ":" + str(addr[1]))
            start_new_thread(threaded_client, (conn,))

def main():

    gpg.stop()
    s = setupServer()
    s.listen(5)
    print("In Main")
    start_new_thread(openThread, (s,))

    while True:

        try:
            print("Mainissa loop")
            time.sleep(5);
            #conn = setupConnection()
            #dataTransfer(conn)

        except:
            print("ERROR OCCURED")
            s.close()
            break


if __name__ == "__main__":
    main()


