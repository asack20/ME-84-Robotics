#!/usr/bin/python3
import math as m
from time import sleep

# parameters
length_1 = 6.25 # (inches) length between shoulder and elbow
length_2 = 5.375 # (inches) length between elbow and wrist ??
sleep_time = 8 # seconds
num_its = 3 # number of times to run through main loop
xpos = 8 #x and y positions
ypos = 6
R = 10 

# it is assumed that the arm is fully straightened out when the program is run
def main():
	print('Calculate End Effector Position')
	
	# create objects
	ev3 = Device('this')
	shoulder = ev3.LargeMotor('outA')
	elbow = ev3.LargeMotor('outB')
	wrist = ev3.MediumMotor('outC')
	
	# record position at beginning of program for zeroing motor positions
	init_s = shoulder.position
	init_e = elbow.position
	init_w = wrist.position
	
	
def calcAngles():
	