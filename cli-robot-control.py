import bluetooth
import msvcrt
import sys
import os
import time

keepGoing = True
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
direction = "None"
ifConnected = False

os.system('cls')

def btconnect():
        global ifConnected
	target_name = "HC-05"
	target_address = None
	nearby_devices = bluetooth.discover_devices()
	for bdaddr in nearby_devices:
		if target_name == bluetooth.lookup_name( bdaddr ):
			target_address = bdaddr
			break

	if target_address is not None:
		print "Found target bluetooth device at address ", target_address
		sock.connect((target_address, 1))
		print "Connected!"
		ifConnected = True
	else:
                print "No device to connect to!"
		ifConnected = False

while keepGoing:
        continueInputLoop = True
        print("         Hello! Bluetooth-controlled Robot v1.0")
        print("         Written by Zachary Murtishi, 2016")
        print("         This program is meant to be used with the HC-05 Bluetooth module")
        print "         This program is intended to be run on Python 2.7 on a Microsoft Windows system"
        print("         See readme for more info")
        print(" ")
        print "         Connected: ", ifConnected
        print(" ")
        print("                 1) Connect to Bluetooth module")
        print("                 2) Begin control")
        print("                 3) End program")
        pick = raw_input("Option? ")
        if int(pick) == 1:
                print "Connecting..."
                btconnect()
                time.sleep(2)
                os.system('cls')
        if int(pick) == 2:
                if ifConnected == True:
                        while continueInputLoop == True:
                                print "Use WASD keys to control robot. Press 'm' to stop controlling the robot."
                                print "Direction: ", direction
                                if str(msvcrt.getch()) == "w":
                                        direction = "Forward"
                                        sock.send("0")
                                        os.system('cls')
				
                                elif str(msvcrt.getch()) == "s":
                                        direction = "Backward"
                                        sock.send("1")
                                        os.system('cls')
				
                                elif str(msvcrt.getch()) == "a":
                                        direction = "Left"
                                        sock.send("2")
                                        os.system('cls')
				
                                elif str(msvcrt.getch()) == "d":
                                        direction = "Right"
                                        sock.send("3")
                                        os.system('cls')

                                elif str(msvcrt.getch()) == "e":
                                        direction = "None"
                                        sock.send("4")
                                        os.system('cls')
				
                                elif str(msvcrt.getch()) == "m":
                                        continueInputLoop = False
                                        direction = "None"
                                        sock.send("4")
                                        os.system('cls')
                                else:
                                        print "Invalid input!", msvcrt.getch()
                                        direction = "None"
                                        sock.send("4")
                                        os.system('cls')
                else:
                        print "Not connected!"
                        time.sleep(3)
                        os.system('cls')
        if int(pick) == 3:
                sock.close()
                keepGoing = False
                ifConnected = False
                print("Program ended")
                time.sleep(3)
                os.system('cls')
        if int(pick) >= 4:
                print "Invalid input: ", pick
                print "Please enter a valid choice!"
