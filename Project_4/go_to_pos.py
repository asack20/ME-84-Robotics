#!/usr/bin/python3
import math as m
from time import sleep
# parameters
length_1 = 6.25 # (inches) length between shoulder and elbow
length_2 = 5.5 # (inches) length between elbow and wrist ??

target_s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 13, 12, 7, 10, 6, 9, 12, 11, 8, 5, 3, 0, -10, -18, -19, -17, -13, -12, -6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
target_e = [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 17, 24, 21, 18, 15, 4, 0, -2, -11, -19, -28, -36, -36, -24, -11, -7, -7, -7, -5, -1, 0, 11, 20, 23, 20, 15, 10, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
target_w = [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 17, 24, 21, 18, 15, 4, 0, -2, -11, -19, -28, -36, -36, -24, -11, -7, -7, -7, -5, -1, 0, 11, 20, 23, 20, 15, 10, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
speed = 300

#ang_1 = 0 # angle of shoulder
#ang_2 = 0 # angle of elbow
#ang_3 = 0 # angle of wrist

def main():
	print('Calculate End Effector Position')
	
	# create objects
	ev3 = Device('this')
	shoulder = ev3.LargeMotor('outA')
	elbow = ev3.LargeMotor('outB')
	wrist = ev3.MediumMotor('outC')
	
	
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