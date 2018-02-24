http://mechatronics2018.dreslab.com/pages/102609

Project 5: Robotic Arm (Part 2)

By Isaac Collins, James Liao, and Andrew Sack

Overview:

The goal of this project was to program the robot arm we designed and built in our last project to use inverse kinematics so the robot could achieve a desired end effector location and travel through a sequence of pre-planned points. Our project was successful by implementing a way for a user to give the robot a drawing through a GUI and have the robot copy that drawing by moving a marker across a series of desired locations.

Construction Updates:

This project primarily uses the same robot arm as was used for Project 4. However, some small modifications were made based on lessons learned from that project. The main changes we made to this project were the removal of the button we used for the last one because it was not needed for these challenges, as well as more firmly mounting the arm onto the EV3. This did not fully fix the issue as the EV3 still would move about as the arm was in operation however it became easier to steady.

Software:

Challenge 1: Calculate Motor Positions

This builds on the previous code from robot arm part 1 for when a user moves the robot arm the EV3 calculates the end effector position, this code takes those calculated end effector positions and from that data uses inverse kinematics to find the original motor angles used to achieve that position. The only difficulty we ran into was when the user manipulates the motors, there is always 2 possible positions to have the motor which would achieve the same end effector position. Unfortunately the computer has no way of telling which of the two positions is correct, which means that this program was not always accurate in perfectly determining the correct angles of the motors, however in the second challenge this is not an issue because the angles calculated will always be done by the same method and therefore will achieve the desired end effector locations the same way.

Challenge 2: Playing Back Sequence of End Effector Positions

This code takes a text file as input. The data in the file is read into into 3 lists which correspond to shoulder, elbow, and wrist position data. After first recording the initial relative motor angles, the robot then uses the inverse kinematics equations to calculate the new angles the shoulder and elbow motors would need to change to and a boolean pen matrix is used determine whether the pen should be up or down. The motors would iterate this process until it had moved through all the positions it had been given.

Bonus Challenge: Dynamically Inputting Sequence of End Effector Positions

For this challenge, we used MATLAB to create a simple GUI program for plotting arm motion. The boundaries of the plot are the limits of the arm motion, with a blue semicircle to denote the right boundary, since it is not a straight line. The plotting is done by mouse clicks, with a left-click to select a new point, a middle-click to toggle the pen, and a right-click to end the program. When a point is clicked, the x-position, y-position, and pen state are saved as a tab-delimited line in a text file. When the program is finished, the text file is saved and can be copied over to the EV3 where the information is read and used to move the arm.
