Find The Wall
By: Isaac Collins, James Liao, Andrew Sack
1/24/18


Overview:
The goal of this project was to design, build and code a robot that will detect an object in front of it and stop before it gets too close, either by stopping wholesale or by slowing down. To accomplish this project, a Lego Mindstorms EV3 kit was used to construct the design of a simple driving robot. Two programs, Bang-Bang and Proportional Control were used to control our robots motion. At the top of each coding file we made key parameters easily accessible to modify. An additional feature to these programs was added so that if the robot initially was too close to an object, it would back up until it had reached the desired distance.

This project was successful in creating a robot that could accomplish these goals: The robot was stable and built using only the EV3 kit, and the code for this robot successfully detects an object in front of it and stops according to the program running.

Construction:
Our robot uses a two motor design with a caster wheel centered around the EV3 with an axis of symmetry through the ultrasonic sensor and caster wheel. The motors are secured and connected along the side, top and bottom of the EV3 unit, with the top support beam providing an easy handhold to move the robot during testing, while not blocking any buttons or the screen. This construction is sturdy under testing conditions.

Control:
We used two different algorithms to control our robot: bang-bang and proportional control
Bang-Bang:
The bang-bang program drives the robot (either forwards or backwards) at a fixed speed until it either detects that it is acceptably close to the target distance or has overshot. If it is at the target distance, the robot then stops. If it has overshot, then the robot drives the opposite direction at the same fixed speed. This process repeats until the robot reaches the target distance.

Since the bang-bang algorithm only has 2 speeds (full speed and stopped), this method results in the robot attempting to stop instantaneously, which is not possible. This results in the robot often over-shooting the target distance. The robot then attempts to correct for this and overshoots in the opposite direction. This repeats, resulting in the robot often oscillating repeatedly before finally stopping at the target distance.

Proportional:
The proportional program drives the robot at a speed proportional to how far the robot is from the target distance. This causes the robot to gradually slow down until it reaches the target distance and stops. The only time motor speed is not proportional to distance is when the robot is so far away that the calculated speed is greater than the maximum speed of the motors used, in which case the robot drives at max speed. This control method results in a much smoother motion where the robot is much less likely to overshoot the target and oscillate around the target distance.

Variance:
For both bang-bang and proportional control, we define the target distance as a range instead of an exact number. This is because it is unreasonable to expect a sensor reading to be an exact value. In addition, the precision of the sensor is greater than the expected precision of the robot. We added a variance parameter to account for this and settled on a value of 0.2 cm. This means that if the robot is within 0.2 cm of the target distance, the robot is considered at the target distance.