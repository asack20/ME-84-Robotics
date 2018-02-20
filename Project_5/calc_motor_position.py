#!/usr/bin/python3
import math as m
from time import sleep

# parameters
length_1 = 6.25 # (inches) length between shoulder and elbow
length_2 = 5.375 # (inches) length between elbow and wrist ??
sleep_time = 8 # seconds
num_its = 3; # number of times to run through main loop

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
	
	for  x in range(1, num_its):
		
		# read motor position in degrees, subtract initial position to zero, then convert to radians
		theta = m.radians(shoulder.position - init_s) # theta is shoulder position
		alpha = theta + m.radians(elbow.position - init_e)  #alpha is theta + elbow position
		
		print('Alpha Measured: ' + str(alpha) + ' radians')
		print('Theta Measured: ' + str(theta) + ' radians')
		
		ang_w = wrist.position - init_w # get zeroed wrist position

		# trig to calculate position in x and y
		x_pos = length_1 * m.cos(theta) + length_2 * m.cos(alpha) 
		y_pos = length_1 * m.sin(theta) + length_2 * m.sin(alpha)
		
		# print position to console
		print('X Position: ' + str(x_pos) + ' inches')
		print('Y Position: ' + str(y_pos) + ' inches')
		print('End Effector: ' + str(ang_w) + ' degrees')

		# Calculate motor position from x_pos and y_pos
		cos_alpha = m.pow(length_2, 2) - (m.pow(length_1, 2) + (m.pow(x_pos,2) + m.pow(y_pos,2)))/(-2*length_1*m.sqrt(m.pow(x_pos,2) + m.pow(y_pos,2)))
		alpha_calc = m.atan(m.sqrt(1 - m.pow(cos_alpha,2))/cos_alpha)
		beta_calc = m.atan(y_pos/x_pos)
		
		cos_theta = ((m.pow(x_pos,2) + m.pow(y_pos,2)) - (m.pow(length_1,2) + m.pow(length_2,2)))/(-2*length_1*length_2)
		theta_calc = m.pi - m.atan(m.sqrt(1 - m.pow(cos_theta,2))/cos_theta)
		
		print('Alpha Calculated: ' + str(alpha_calc) + ' radians')
		print('Theta Calculated: ' + str(theta_calc) + ' radians')
		
		sleep(sleep_time) 

	# end for loop

	print('end')

if __name__ == '__main__':
	main()