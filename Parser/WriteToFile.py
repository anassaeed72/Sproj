import sys
if len(sys.argv) <3:
	print('Arguments not given')
	sys.exit()
with open(sys.argv[1], "w") as myfile:
    myfile.write(sys.argv[2])
