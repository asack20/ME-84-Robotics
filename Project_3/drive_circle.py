#!/usr/bin/python3

# parameters
Kp = 15; # proportionality constant
base_speed = 600 # target speed for truck to move
target_angle = 10 # angle between tractor and trailer 
num_its = 400 # number of iterations to run code (roughly, how long to run for)

def main():
	print('Drive Backwards Circle')
	
	# create objects
	ev3 = Device('this')
	motorL = ev3.LargeMotor('outD')
	motorR = ev3.LargeMotor('outA')
	truck_gyro = ev3.GyroSensor('in1')
	trailer_gyro = ev3.GyroSensor('in2')
	
	# gyro initialization
	truck_gyro.mode = 'GYRO-CAL' # resets gyro
	trailer_gyro.mode = 'GYRO-CAL' # resets gyro
	truck_gyro.mode = 'GYRO-ANG' #sets mode to reading angle 
	trailer_gyro.mode = 'GYRO-ANG' #sets mode to reading angle
	
	count = 0
	
	# main loop
	while count < num_its: # loop through a set number of times
		
		truck_angle = truck_gyro.value() # read truck angle
		trailer_angle = trailer_gyro.value() # read trailer angle
		
		# calculations
		# error is how far off from the target_angle the angle between the trailer and truck is
		error = (trailer_angle - truck_angle) - target_angle
		left_speed = base_speed - (error * Kp) # subtract error from 1 motor's speed
		right_speed = base_speed + (error * Kp) # add to the other
		
		# make sure speeds stay within motor's accepted range, so there isn't an error
		if left_speed > 1050:
			left_speed = 1050
		elif left_speed < -1050:
			left_speed = -1050
		
		if right_speed > 1050:
			right_speed = 1050
		elif right_speed < -1050:
			right_speed = -1050
		
		# set motor speeds
		motorL.run_forever(speed_sp=left_speed)
		motorR.run_forever(speed_sp=right_speed)
		
		# print debugging messages
		if (count % 200) == 0: # limit console output frequency to make it easier to read and so it doesn't slow down code
			print('COUNT: ' + str(count))
			print('trailer angle: ' + str(trailer_angle))
			print('truck angle: ' + str(truck_angle))
			print('error: ' + str(error))
			#print('left speed: ' + str(left_speed))
			#print('right speed: ' + str(right_speed))
		
		
		count += 1; # increase counter variable
	# end while loop
	
	# stop motors at end of program
	motorL.stop(stop_action="brake")
	motorR.stop(stop_action="brake")
	
if __name__ == '__main__':
	main()