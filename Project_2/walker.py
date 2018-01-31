#!/usr/bin/python3
from time import sleep
speed = 1000;

#speeds
slow = 200
medium = 500
fast = 1000

waitTime = 5 # seconds

def main():
	
	print('Test') # debug statement
	
	# create motor object
	ev3 = Device('this')
	motor = ev3.LargeMotor('outA')
	
	# goes forward at increasing speeds, then backwards at increasing speeds
	
	# forwards
	motor.run_forever(speed_sp=slow)
	sleep(waitTime)
	motor.stop(stop_action="brake")
	
	motor.run_forever(speed_sp=medium)
	sleep(waitTime)
	motor.stop(stop_action="brake")
	
	motor.run_forever(speed_sp=fast)
	sleep(waitTime)
	motor.stop(stop_action="brake")
	
	# backwards
	motor.run_forever(speed_sp=-slow)
	sleep(waitTime)
	motor.stop(stop_action="brake")
	
	motor.run_forever(speed_sp=-medium)
	sleep(waitTime)
	motor.stop(stop_action="brake")
	
	motor.run_forever(speed_sp=-fast)
	sleep(waitTime)
	motor.stop(stop_action="brake")
	

if __name__ == '__main__':
	main()