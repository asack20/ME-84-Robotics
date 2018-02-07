#!/usr/bin/python3

# parameters
Kp = 5; # proportionality constant
base_speed = 200 # target speed for truck to move
target_angle_1 = -15 # angle for 1st turn
target_angle_2 = 15 # angle for 2nd turn
turn_1_its = 200 # number of iterations to run 1st turn (roughly, how long to run for)
turn_2_its = 200 # number of iterations to run 2nd turn

def main():
	print('Parallel Park')
	
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
	
	count = 0 # reset count
	
	# 1st turn
	while count < turn_1_its: # loop through a set number of times
		
		truck_angle = truck_gyro.value() # read truck angle
		trailer_angle = trailer_gyro.value() # read trailer angle
		
		# calculations
		error = (trailer_angle - truck_angle) - target_angle_1 # calculate error from 1st target angle
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
		if (count % 50) == 0: # limit console output frequency to make it easier to read and so it doesn't slow down code
			print('COUNT: ' + str(count))
			print('trailer angle: ' + str(trailer_angle))
			print('truck angle: ' + str(truck_angle))
			print('error: ' + str(error))
			#print('left speed: ' + str(left_speed))
			#print('right speed: ' + str(right_speed))
		
		
		count += 1; # increase counter variable
	# end while loop
	
	count = 0 # reset counter 
	
	# 2nd turn
	while count < turn_2_its: # loop through a set number of times
		
		truck_angle = truck_gyro.value() # read truck angle
		trailer_angle = trailer_gyro.value() # read trailer angle
		
		# calculations
		error = (trailer_angle - truck_angle) - target_angle_2 # calculate error from 2nd target angle
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
		if (count % 50) == 0: # limit console output frequency to make it easier to read and so it doesn't slow down code
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