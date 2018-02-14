http://mechatronics2018.dreslab.com/pages/140639

Project 4: Robotic Arm

By Isaac Collins, James Liao, and Andrew Sack

Overview:

The goal of this project was to build a robotic arm with a 2-dimensional range of motion that could hold a pen, make markings on a sheet of paper, as well as record and “playback” its position in 2-dimensional space. This project was successful to calculate its position in space and in using the motor controllers to ‘remember’ the arm’s position.

Construction:

The arm was constructed using 3 motors, which had roles as the ‘elbow’, ‘shoulder’, and ‘wrist’ joints. The wrist joint held a red expo marker as a writing tool using only lego pieces.The wrist joint motor was a EV3 medium motor and the shoulder and elbow motors were large motors. A caster wheel attached to the wrist joint allowed for smooth movement as the arm moved across the page, and a button was connected to the EV3 block as a mechanical way to control arm recording and playback. Long pieces were used for the ‘bones’ of the arm to give the largest freedom of movement to the arms motion.

Design Challenges:

One big difficulty with controlling the arm’s two dimensional motion was friction causing the arm to move at the shoulder as well as at the wrist. This difficulty could be fixed by creating a wider base (at the expense of the arm’s current range of extension) or by printing/laser cutting a tool to secure the pieces of the EV3 together with the arm. Our attempted solution of adding the caster wheel did decrease friction however there was still some uncertainty when it came to control.

Software:

Challenge 2: Calculating End Effector Positions

This challenge uses the built in encoders in each motor to calculate the arm position. First, the encoder values for the straightened-out arm are recorded to serve as a reference for all other values and to effectively zero the encoders. Then, for each time position is calculated, the angle of the shoulder motor (theta), is calculated by subtracting the initial position from the shoulder position and converting to radians. The angle of the wrist (alpha) is calculated similarly, but the wrist angle is added to theta, so alpha is relative to the x-axis. The trigonometric equations below are then used to calculate the positions and the results are printed to the console. The lengths are constant and were determined by measuring the joint-to-joint distances on the arm.

x_pos = length_1 * m.cos(theta) + length_2 * m.cos(alpha)

y_pos = length_1 * m.sin(theta) + length_2 * m.sin(alpha)

Challenge 3: Recording and Playing Back Positions

This challenge involves recording the position of the arm while it is manually moved, and then the robot repeating that motion independently. The storage of arm positions is accomplished by saving the relative positions of each joint in separate python lists. This is because the position-based movement of the EV3 motors only accepts relative positions, not absolute. While the arm is manually moved, the code loops through reading the position of the three motors and then saving the position minus the previous position to the list. It then sleeps for a set amount of time and repeats. After the recording is complete, the program waits for a button made from a touch sensor to be pressed to give the user time to reset the robot position. The program then iterates through the lists and commands each motor to move the recorded distance at a given speed and then sleep for the same amount of time as in recording.

Code Files:

calc_position.py

record_and_play.py
