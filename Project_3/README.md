http://mechatronics2018.dreslab.com/pages/140315

Mack

By Isaac Collins, James Liao, and Andrew Sack

Overview:

The goal of this project was to use proportional control techniques to push a trailer mounted to our car base along different driving patterns. We succeeded in pushing our trailer to drive straight, to drive in a circle, and to parallel park inside of a parking spot.

Construction:

The “tractor” of our truck has 2 wheels each attached to their own motor and well as a castor wheel in the front of the truck for balance. The truck gyro is mounted above the center of the EV3 controller and the axle it is attached to is also used for cable management.

The hitch consists of a beam mounted to the trailer which connects to a beam on the back of the tractor with 1 pin, which allows for free rotation and easy separation of the two pieces for transport. The trailer gyro is mounted on the beam offset several inches from the point of rotation, but along the centerline of the trailer.

Code:

All three challenges involved using a gyro and proportional control to drive a truck in reverse. An error is calculated from the gyro angle and then that error is multiplied by a proportionality constant, Kp, to get a speed difference. This speed difference is then added to one motor’s speed and subtracted from the other. This causes the robot to turn and push the trailer back on course.

Challenge 1: Drive Straight

For this challenge, the code only utilizes data from 1 gyro mounted on the trailer. The error is simply the trailer angle.

Challenge 2: Drive in a Circle

This challenge utilizes data from both the truck gyro and the trailer gyro. The error is calculated by taking the difference between the 2 gyro angles and then subtracting the target turn angle.

Challenge 3: Parallel Parking

This challenge uses very similar code to driving in a circle. The motion of parallel parking can be done by drive 2 opposite direction arcs. The robot simply drives a 15 degree arc counter-clockwise and then another 15 degree arc clockwise. The exact angle and duration of these arcs were determined experimentally and since the robot was built very compactly, these arcs did not have to be very precise to fulfil the challenge requirements.

Technical Drawbacks:

One of the main difficulties we ran into during this project was with the EV3 gyro sensors. During initial testing, the robot would steer off course repeatedly. This problem was caused by drift issues with the gyro sensor. We swapped the truck and trailer gyro which fixed issues for driving straight, since that program only uses the trailer gyro. However, we continued to have issues with driving in a circle, since we only had 1 good gyro. This resulted in the angle between the trailer and truck gradually increasing until the trailer hit the hard stop on the hitch and could rotate any further.

Code Files:

drive_straight.py

drive_circle.py

parallel_park.py
