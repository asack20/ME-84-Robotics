#!/usr/bin/python3
import math as m
from time import sleep
# parameters
length_1 = 6.25 # (inches) length between shoulder and elbow
length_2 = 5.5 # (inches) length between elbow and wrist ??

target_s = [0, 0, 0, -1, -8, -18, -27, -33, -37, -44, -50, -53, -54, -53, -44, -36, -27, -17, -8, 0, 8, 18, 27, 36, 43, 48, 55, 60, 66, 69, 70, 69, 69, 69, 63, 57, 49, 41, 35, 26, 18, 9, 1, -7, -17, -25, -31, -36, -37]
target_e = [0, 0, 0, 3, 9, 17, 22, 25, 30, 35, 38, 40, 39, 39, 39, 35, 26, 14, 6, 1, -5, -12, -19, -25, -28, -33, -37, -41, -45, -46, -47, -47, -47, -45, -37, -30, -24, -17, -11, -5, 3, 8, 14, 21, 28, 32, 35, 40, 43]
target_w = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -47, -75, -75, -113]

speed = 100

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