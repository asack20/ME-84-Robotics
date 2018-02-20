#!/usr/bin/python3
filename = '/home/robot/.PythonIDE/ide/Projects/Project_5/positions.txt';

def main():
	print('Test')
	
	# File io
	# initalize lists as empty
	x_pos = []
	y_pos = []
	pen = []
	
	# read in data from file
	with open(filename, 'r') as f:
		data = f.readlines()
	
	size = len(data)
	
	# for each line of file (element in data)
	for i in range(0, size):
		line = data[i].split('\t'); # split line up by tabs
		# append values to lists
		x_pos.append(float(line[0])) 
		y_pos.append(float(line[1]))
		pen.append(int(line[2]))
	# end for
	
	# debug prints
	print(size)
	print(data)
	print(x_pos)
	print(y_pos)
	print(pen)

if __name__ == '__main__':
	main()