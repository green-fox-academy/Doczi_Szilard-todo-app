import sys

#class Controller():
	#def __init__(self, View):


	# def arg_reader(self):
	# 	if len(sys.argv) == 1:
	# 		return []
	# 	else:
	# 		return sys.argv[1:]

#arguments = arg_reader()

# if len(arguments) == 0:
# 	print('help text')
# else:
# 	if( arguments[0] == '-l' ):
# 		print('Addolunk ilyet', arguments[1])


#class Model(Controller):

class View():

	#def __init__(self):


	def printer(self):
		print("Python Todo application\n=======================\n\nCommand line arguments:\n-l   Lists all the tasks\n-a   Adds a new taskA\n-r   Removes an task\n-c   Completes an task")



view = View()
view.printer()
