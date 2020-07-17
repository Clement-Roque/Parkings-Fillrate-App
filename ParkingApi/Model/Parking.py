import datetime

class Parking():

	def __init__(self,name:str,label:str,status:str,free:int,total:int,last_update:str):
		self.name = name
		self.label = label
		self.status = status
		self.free = free
		self.total = total
		self.last_update = datetime.datetime.strptime(last_update,'%Y-%m-%dT%H:%M:%S')
