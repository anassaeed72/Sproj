from Constants import ConstantsClass

class Print:
	@staticmethod
	def Print(printPermission,message):
		if printPermission.value:
			print(message)

