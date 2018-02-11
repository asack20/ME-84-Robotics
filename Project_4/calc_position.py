#!/usr/bin/python3
import math as m
from time import sleep
# parameters
length_1 = 6.25 # (inches) length between shoulder and elbow
length_2 = 5.5 # (inches) length between elbow and wrist ??

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
	
	s_list = []
	e_list = []
	w_list = []
	
	for  x in range(1, 50):
		s_list.append(shoulder.position - init_ang_s)
		e_list.append(elbow.position - init_ang_e)
		w_list.append(wrist.position - init_ang_w)
		
		theta = m.radians(shoulder.position - init_ang_s)
		alpha = theta + m.radians(elbow.position - init_ang_e)

		x_pos = length_1 * m.cos(theta) + length_2 * m.cos(alpha)
		y_pos = length_1 * m.sin(theta) + length_2 * m.sin(alpha)
		
		#if touch.is_pressed:
		#print('X Position: ' + str(x_pos) + ' inches')
		#print('Y Position: ' + str(y_pos) + ' inches')

		sleep(0.1)

	# end while
	
	print('s')
	print(s_list)
	print('e')
	print(e_list)
	print('w')
	print(w_list)
	print('end')
	

if __name__ == '__main__':
	main()