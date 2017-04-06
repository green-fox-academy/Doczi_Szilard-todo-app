import sys

#myfile = open('duplicated-chars.txt', 'r')

class Controller():
	#def __init__(self, View):


	def arg_reader(self):
		self.list_argv = []
		if len(sys.argv) <= 1:
			self.list_argv = []
		else:
			self.list_argv = sys.argv[1:]

		if len(self.list_argv) == 0:
			view.print_welcome_page()
		else:
			pass
			# if( arguments[0] == '-l' ):
			# 	print('Addolunk ilyet', arguments[1])

#arguments = arg_reader()



#class Model(Controller):

class View():

	#def __init__(self):


	def print_welcome_page(self):
		print("Python Todo application\n=======================\n\nCommand line arguments:\n-l   Lists all the tasks\n-a   Adds a new taskA\n-r   Removes an task\n-c   Completes an task")



view = View()
controller = Controller()

controller.arg_reader()
