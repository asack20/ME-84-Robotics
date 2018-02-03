#!/usr/bin/python3

# parameters
Kp = 10; # proportionality constant
base_speed = 500
target_angle = 20
num_its = 1000 # number of iterations to run code (roughly, how long to run for)

def main():
	print('Drive Backwards Circle')
	
	# create objects
	ev3 = Device('this')
	motorL = ev3.LargeMotor('outD')
	motorR = ev3.LargeMotor('outA')
	truck_gyro = ev3.GyroSensor('in1') # (should not be used for this program)
	trailer_gyro = ev3.GyroSensor('in2')
	
	# gyro initialization
	truck_gyro.mode = 'GYRO-CAL' # resets gyro? (should not be used for this program)
	trailer_gyro.mode = 'GYRO-CAL' # resets gyro? 
	
	truck_gyro.mode = 'GYRO-ANG' #sets mode to reading angle (should not be used for this program)
	trailer_gyro.mode = 'GYRO-ANG' #sets mode to reading angle
	
	count = 0
	
	# main loop
	while count < num_its:
		
		truck_angle = truck_gyro.value() # read truck angle
		trailer_angle = trailer_gyro.value() # read trailer angle
		
		# calculations
		error = (trailer_angle - truck_angle) - target_angle
		left_speed = base_speed - (error * Kp)
		right_speed = base_speed + (error * Kp)
		
		# set motor speeds
		motorL.run_forever(speed_sp=left_speed)
		motorR.run_forever(speed_sp=right_speed)
		
		# print debugging messages
		if (count % 20) == 0: # limit console output frequency
			print('COUNT: ' + str(count))
			print('error: ' + str(error))
			print('left speed: ' + str(left_speed))
			print('right speed: ' + str(right_speed))
		
		
		count += 1;
	# end while loop
	
	# stop motors at end of program
	motorL.stop(stop_action="brake")
	motorR.stop(stop_action="brake")
	
if __name__ == '__main__':
	main()