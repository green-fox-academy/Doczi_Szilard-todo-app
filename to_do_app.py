import sys

class Controller():

	def __init__(self):
		self.list_argv = []
		self.arg_reader()
		self.control()

	def arg_reader(self):
		if len(sys.argv) <= 1:
			self.list_argv = []
		else:
			self.list_argv = sys.argv[1:]

	def control(self):
		if len(self.list_argv) == 0:
			view.print_welcome_page()
		else:
			if self.list_argv[0] == '-l':
				model.print_list()
			if self.list_argv[0] == '-a':
				if len(self.list_argv) == 1:
					print('Unable to add: no task provided')
				else:
					model.add(self.list_argv[1])
					model.writer()

			# if( self.list_argv[0] == '-r' ):
			# if( self.list_argv[0] == '-c' ):

class Model():

	def __init__(self):
		self.to_do = ""
		self.reader()

	def reader(self):
		try:
			myfile = open('database.txt', 'r')
			self.to_do = myfile.readlines()
			myfile.close()
		except:
			self.to_do = []

	def writer(self):
		myfile = open('database.txt', 'w')
		myfile.writelines(self.to_do)
		myfile.close()

	def print_list(self):
		if len(self.to_do) == 0:
			print('Nothing to do today')
		else:
			for i in range(len(self.to_do)):
				print(i + 1, self.to_do[i][1:-1])

	def add(self, thing):
	        self.to_do.append("0" + " + " + thing + '\n')

class View():

	#def __init__(self):


	def print_welcome_page(self):
		print("Python Todo application\n=======================\n\nCommand line arguments:\n-l   Lists all the tasks\n-a   Adds a new taskA\n-r   Removes an task\n-c   Completes an task")



view = View()
model = Model()
controller = Controller()



controller.arg_reader()
