from Constants import ConstantsClass

class Print:
	Everthing = 0
	Basic = 1
	OnlyImp = 2
	@staticmethod
	def p(level,message):
		if level>= ConstantsClass.printLevel:
			print(message)

