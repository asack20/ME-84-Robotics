#!/usr/bin/python3

# parameters
Kp = 40; # proportionality constant
targetDistance = 20; # in CM
variance = .20;  # Acceptable error from target distance in CM

def main():
	print('Test')
	
	# create objects
	ev3 = Device('this')
	motorL = ev3.LargeMotor('outD')
	motorR = ev3.LargeMotor('outA')
	ultrasonic_sensor = ev3.UltrasonicSensor('in1')
	
	# get first distance reading
	distanceCM = ultrasonic_sensor.distance_centimeters #get distance in CM
	print(distanceCM)
	
	# while distance reading is not in the acceptable range (targetDistance+-variance)
	while ((distanceCM < (targetDistance - variance)) or (distanceCM > (targetDistance + variance))):
		
		# calculate speed based on distance from target distance
		error = distanceCM - targetDistance;
		speed = Kp * error;
		
		# if speed is within acceptable range for motors
		if abs(speed) <= 1050:
			# run at calculated speed
			motorL.run_forever(speed_sp=speed)
			motorR.run_forever(speed_sp=speed)
		elif speed > 1050: # out of range and positive
			# run forward at max speed
			motorL.run_forever(speed_sp=1050)
			motorR.run_forever(speed_sp=1050)
		else: # speed < -1050 (out of range and negative)
			# run backward at max speed
			motorL.run_forever(speed_sp= -1050)
			motorR.run_forever(speed_sp= -1050)
		
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