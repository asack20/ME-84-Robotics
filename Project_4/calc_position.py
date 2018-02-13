#!/usr/bin/python3
import math as m
from time import sleep
# parameters
length_1 = 6.25 # (inches) length between shoulder and elbow
length_2 = 5.5 # (inches) length between elbow and wrist ??
sleep_time = 3 # seconds
num_its = 5;

def main():
	print('Calculate End Effector Position')
	
	# create objects
	ev3 = Device('this')
	shoulder = ev3.LargeMotor('outA')
	elbow = ev3.LargeMotor('outB')
	wrist = ev3.MediumMotor('outC')
	
	init_s = shoulder.position
	init_e = elbow.position
	init_w = wrist.position
	
	for  x in range(1, num_its):
		theta = m.radians(shoulder.position - init_s)
		alpha = theta + m.radians(elbow.position - init_e)

		ang_w = wrist.position - init_w

		x_pos = length_1 * m.cos(theta) + length_2 * m.cos(alpha)
		y_pos = length_1 * m.sin(theta) + length_2 * m.sin(alpha)
		
		print('X Position: ' + str(x_pos) + ' inches')
		print('Y Position: ' + str(y_pos) + ' inches')
		print('End Effector: ' + str(ang_w) + ' degrees')

		sleep(sleep_time)

	# end while

if __name__ == '__main__':
	main()