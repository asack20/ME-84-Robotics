#!/usr/bin/python3
import math as m
from time import sleep
# parameters
length_1 = 6.25 # (inches) length between shoulder and elbow
length_2 = 5.5 # (inches) length between elbow and wrist ??

sleep_time = 0.1 # seconds
num_its = 150 
speed = 300

def main():
	print('Calculate End Effector Position')
	
	# create objects
	ev3 = Device('this')
	shoulder = ev3.LargeMotor('outA')
	elbow = ev3.LargeMotor('outB')
	wrist = ev3.MediumMotor('outC')
	#NEED CODE button = ev3.
	
	# record

	init_ang_s = shoulder.position
	init_ang_e = elbow.position
	init_ang_w = wrist.position
	
	prev_s = init_s
	prev_e = init_e
	prev_w = init_w
	
	s_list = []
	e_list = []
	w_list = []
	
	for  x in range(1, num_its):
		
		curr_s = shoulder.position
		curr_e = elbow.position
		curr_w = wrist.position

		s_list.append(curr_s - prev_s)
		e_list.append(curr_e - prev_e)
		w_list.append(curr_w - prev_w)
		
		prev_s = curr_s
		prev_e = curr_e
		prev_w = curr_w

		sleep(sleep_time)

	# end for loop

	# print('s')
	# print(s_list)
	# print('e')
	# print(e_list)
	# print('w')
	# print(w_list)
	# print('end')
	

	# playback

if __name__ == '__main__':
	main()


	
	init_ang_s = shoulder.position
	init_ang_e = elbow.position
	init_ang_w = wrist.position
	
	#print(shoulder.position)
	#print(elbow.position)
	#print(wrist.position)
	
	for x in range(0, len(target_s)):
		shoulder_ang = target_s[x]
		elbow_ang = target_e[x]
		wrist_ang = target_w[x]
	
		shoulder.run_to_rel_pos(position_sp=shoulder_ang, speed_sp=speed, stop_action="coast")
		elbow.run_to_rel_pos(position_sp=elbow_ang, speed_sp=speed, stop_action="coast")
		wrist.run_to_rel_pos(position_sp=wrist_ang, speed_sp=speed, stop_action="coast")
		sleep(0.1)
	# end while
	

if __name__ == '__main__':
	main()