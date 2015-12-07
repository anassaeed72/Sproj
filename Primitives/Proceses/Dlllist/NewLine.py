import sys
if len(sys.argv) <2:
	print('Arguments not given')
	sys.exit()
with open(sys.argv[1], "a") as myfile:
    myfile.write("\n")
