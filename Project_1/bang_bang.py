#!/usr/bin/python3

# parameters
speed = 500; 
targetDistance = 20; # in CM
variance = 0.20; # Acceptable error from target distance in CM

def main():
	print('Test') 
	
	# create objects
	ev3 = Device('this')
	motorL = ev3.LargeMotor('outD')
	motorR = ev3.LargeMotor('outA')
	ultrasonic_sensor = ev3.UltrasonicSensor('in1')
	
	# Get distance reading for the first time
	distanceCM = ultrasonic_sensor.distance_centimeters #get distance in CM
	print(distanceCM)
	
	# while distance reading is not in the acceptable range (targetDistance+-variance)
	while ((distanceCM < (targetDistance - variance)) or (distanceCM > (targetDistance + variance))):
		
		if distanceCM > targetDistance: #if too far
			# drive forward at given speed
			motorL.run_forever(speed_sp=speed)
			motorR.run_forever(speed_sp=speed)
		
		else: # distanceCM < targetDistance (if too close)
			# drive backwards at given speed
			motorL.run_forever(speed_sp=speed*-1)
			motorR.run_forever(speed_sp=speed*-1)
		
		# update distance reading
		distanceCM = ultrasonic_sensor.distance_centimeters #get distance in CM
		print(distanceCM)
	# end of while loop
	
	# at correct distance so STOP
	motorL.stop(stop_action="brake")
	motorR.stop(stop_action="brake")
	
	print('done')
	

if __name__ == '__main__':
	main()