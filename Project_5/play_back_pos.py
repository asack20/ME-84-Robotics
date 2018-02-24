#!/usr/bin/python3
import math as m
from time import sleep
# parameters
length_1 = 6.25 # (inches) length between shoulder and elbow
length_2 = 5.375 # (inches) length between elbow and wrist 

speed = 200 # speed to run motors at for playback
filename = '/home/robot/.PythonIDE/ide/Projects/Project_5/line.txt';
sleep_time = 0.25;

# it is assumed that the arm is fully straightened out when the program is run

def main():
	print('Test')
	
	# create objects
	ev3 = Device('this')
	shoulder = ev3.LargeMotor('outA')
	elbow = ev3.LargeMotor('outB')
	wrist = ev3.MediumMotor('outC')
	
	# File io
	# initalize lists as empty
	x_pos = []
	y_pos = []
	pen = []
	
	# read in data from file
	with open(filename, 'r') as f:
		data = f.readlines()
	
	size = len(data)
	
	# for each line of file (element in data)
	for i in range(0, size):
		line = data[i].split('\t'); # split line up by tabs
		# append values to lists
		x_pos.append(float(line[0])) 
		y_pos.append(float(line[1]))
		pen.append(int(line[2]))
	# end for
	
	# debug prints
	print(size)
	print(data)
	print(x_pos)
	print(y_pos)
	print(pen)
	
	# get intial motor positions
	s_prev = 0
	e_prev = 0
	w_prev = 90
	
	for x in range(0, len(x_pos)): # go through position
		
		print(x_pos[x])
		print(y_pos[x])
		print(pen[x])
		
		# calculate motor angles from position all in radians
		cos_alpha = (m.pow(length_2, 2) - (m.pow(length_1, 2) + (m.pow(x_pos[x],2) + m.pow(y_pos[x],2))))/(-2*length_1*m.sqrt(m.pow(x_pos[x],2) + m.pow(y_pos[x],2)))
		#print(cos_alpha) 
		alpha_calc = m.atan(m.sqrt(1 - m.pow(cos_alpha,2))/cos_alpha)
		beta_calc = m.atan(y_pos[x]/x_pos[x])
		
		theta_1_c = alpha_calc + beta_calc
		
		cos_theta = ((m.pow(x_pos[x],2) + m.pow(y_pos[x],2)) - (m.pow(length_1,2) + m.pow(length_2,2)))/(-2*length_1*length_2)
		theta_2_c = -m.atan(m.sqrt(1 - m.pow(cos_theta,2))/cos_theta)
		
		# target motor position in degrees
		s_curr = m.degrees(theta_1_c)
		e_curr = m.degrees(theta_2_c) 
		w_curr = 90*pen[x]
		# angle to move motors by
		shoulder_ang = s_curr - s_prev
		elbow_ang = e_curr - e_prev
		wrist_ang = w_curr-w_prev
		# update previous values
		s_prev = s_curr
		e_prev = e_curr
		w_prev = w_curr
		# set motors to move by those angles at given speed
		if wrist_ang != 0: # makes pen move before arm does
			wrist.run_to_rel_pos(position_sp=wrist_ang, speed_sp=speed, stop_action="hold")
			sleep(0.5)
		#end if
		shoulder.run_to_rel_pos(position_sp=shoulder_ang, speed_sp=speed, stop_action="hold")
		elbow.run_to_rel_pos(position_sp=elbow_ang, speed_sp=speed, stop_action="hold")
		

		
		sleep(sleep_time)
	
	# end for loop
	
	# set motors to coast again
	shoulder.stop(stop_action="coast")
	elbow.stop(stop_action="coast")
	wrist.stop(stop_action="coast")
	
	print('end')

if __name__ == '__main__':
	main()