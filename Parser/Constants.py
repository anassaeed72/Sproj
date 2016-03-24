from enum import Enum
class ConstantsClass:
	pathValue="/home/xen/Documents/Sproj/"
	# pathValue="/Users/anassaeed/Dropbox/8th\ Semester/Sproj/Sproj/"

class PrintLevel(Enum):
	Command=True
	IfConditionAnswer=True
	IfConditionCondition=True
	BaseClass =True
	Error = True
	RawOuput = True
	Alpha =True
	Beta = False
	Gamma = True