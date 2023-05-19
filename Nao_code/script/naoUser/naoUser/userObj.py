import numpy as np

class User():
	def __init__(self, name):
		self.username = name
		self.feature_array = []
		self.history=""
		self.question = ''
		
	def add_feature_array(self,feature):
		self.feature_array = np.array(feature)
		
	def add_chat_history(self,history):
		self.history = history

	def add_question(self,question):
		self.question = question

	def get_question(self):
		return self.question

	def get_chat_history(self):
		return self.history
	
	def get_name(self):
		return self.username
	
	def get_feature_array(self):
		return self.feature_array
	def change_username(self,newName):
		self.username = newName
		
# x = np.array([233,1,2,3.5,2.2])
# print("x: " + str(type(x)))
# ss = np.array2string(x, separator=',')
# print("ss:  " + ss)
# #print("type of ss:  " + str(type(ss)))
# recover = np.fromstring(ss.strip('[]'), dtype=np.float64, sep=',')
# print(recover)
# #print(type(recover))
