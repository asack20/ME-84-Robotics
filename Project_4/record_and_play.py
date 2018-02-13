#!/usr/bin/python3
import math as m
from time import sleep
# parameters
length_1 = 6.25 # (inches) length between shoulder and elbow
length_2 = 5.5 # (inches) length between elbow and wrist 

sleep_time = 0.1 # seconds between points collected and played
num_its = 150 # number of data points to collect for arm position. num_its * sleep_time is the length of time data is collected for
speed = 300 # speed to run motors at for playback

# it is assumed that the arm is fully straightened out when the program is run

def main():
	print('Calculate End Effector Position')
	
	# create objects
	ev3 = Device('this')
	shoulder = ev3.LargeMotor('outA')
	elbow = ev3.LargeMotor('outB')
	wrist = ev3.MediumMotor('outC')
	#NEED CODE button = ev3.Button('in1')
	
	# record

	# record position at beginning of program for zeroing motor positions
	init_ang_s = shoulder.position
	init_ang_e = elbow.position
	init_ang_w = wrist.position
	
	# set previous angle values to initial at beginning
	prev_s = init_s
	prev_e = init_e
	prev_w = init_w
	
	# initialize empty lists for relative positions for each motor
	s_list = []
	e_list = []
	w_list = []
	
	# recording loop
	for  x in range(1, num_its): 
		
		# get motor positions
		curr_s = shoulder.position
		curr_e = elbow.position
		curr_w = wrist.position

		# save position relative to previous position
		s_list.append(curr_s - prev_s)
		e_list.append(curr_e - prev_e)
		w_list.append(curr_w - prev_w)
		
		# previous positions are now current
		prev_s = curr_s
		prev_e = curr_e
		prev_w = curr_w

		sleep(sleep_time)

	# end for loop
	
	# code idles while user resets arm position
	while !(button.is_pressed()):
		# Wait until button is pressed
	# end while


	# playback loop
	for x in range(0, len(s_list)): # go through angle lists
		
		# get current relative angles from list
		shoulder_ang = s_list[x]
		elbow_ang = e_list[x]
		wrist_ang = w_list[x]
	
		# set motors to move by those angles at given speed
		shoulder.run_to_rel_pos(position_sp=shoulder_ang, speed_sp=speed, stop_action="coast")
		elbow.run_to_rel_pos(position_sp=elbow_ang, speed_sp=speed, stop_action="coast")
		wrist.run_to_rel_pos(position_sp=wrist_ang, speed_sp=speed, stop_action="coast")
		
		sleep(sleep_time)
	
	# end for loop


if __name__ == '__main__':
	main()


	

	