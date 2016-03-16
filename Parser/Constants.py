from enum import Enum
class ConstantsClass:
	# pathValue="/home/xen/Documents/Sproj/"
	pathValue="/Users/Anas_Saeed/Dropbox/8th\ Semester/Sproj/Sproj"
	# PrintLevel = enum(Command=True, IfConditionAnswer=True, IfConditionCondition=True,BaseClass =True)

class PrintLevel(Enum):
	Command=True
	IfConditionAnswer=True
	IfConditionCondition=True
	BaseClass =True
	Error = True