http://mechatronics2018.dreslab.com/pages/152029

Project 2: Walker

By Isaac Collins, James Liao, and Andrew Sack

Overview:

The goal of this project was to design a robot walker. Our final design was a walker with 4 legs driven by a single motor, successfully able to navigate forwards and backwards at 3 different speeds.

Research:

We got a lot of inspiration from this video, including the use of 4-bar linkage legs to keep the feet always parallel to the ground and the drive linkage.

https://youtu.be/oWs0MZRbVs8

Upon construction, we also noticed a few similarities between our robot and another well known walker:

Unfortunately, though we cannot test it, we are forced to assume that our robot holds a similar flaw as the AT-AT and must avoid Lego X-Wings at all cost.

Construction:

Drive mechanism:

The robot is powered by a single continuously rotating motor. The robot is utilizes only 1 motor to move by having the legs on each side attached to the motor 180 degrees apart.This causes the sides move offset from each other. The legs are connected by individual linkages to the outside of a gear attached the the motor shaft. When the motor spins this causes the legs to move back and forth.The best linkage was determined by testing different linkage lengths to optimize motion and balance, though piece availability also played a role. The linkage lengths were determined to be 9 and 7 hole-lengths for the front and back legs respectively along each side.

Legs:

The legs were made by using a 4 bar parallel linkage, so that no matter what direction the legs were going the ‘feet’ of the robot would always be parallel to the ground. By using a flipped L piece, this concentrated the majority of our robot’s weight onto distinct points on the ground which gave us greater traction, especially on low friction surfaces such as tabletops. Slippage was still an issue our robot dealt with especially at higher speeds.

Performance:

Our walker successfully performed to match our tests, with the leg design minimizing slippage, however at higher speeds the robot still would slip and sway back and forth while in motion. By using longer  linking pieces and positioning the L beams as the ‘feet’ of the robot, we maintained balance at all three speeds even if it became more unstable as the motor speed increased. Even with slippage as well, the robot could still keep moving forward, though it did have difficulty driving straight. One further way not tested that could have been used to improve traction between the robot and the floor would have been to add rubber components available in the kit to the feet. Overall this robot performed to expectations and successfully walked.

Software:

The software for this robot is very simple, since the robot only needs one motor rotating continuously for it to move. The core code is that the motor is turned on at a given speed, the code waits for a certain amount of time, and then the motor is turned off. However, since the robot needs to be able to move at multiple speeds and directions, the included file is slightly longer to demonstrate multiple speeds.

Code: walker.py


