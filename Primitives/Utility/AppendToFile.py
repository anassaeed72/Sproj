import sys
if len(sys.argv) <3:
	print('Arguments not given')
	sys.exit()
with open(sys.argv[1], "a") as myfile:
    myfile.write(sys.argv[2])
    myfile.write(" ")
