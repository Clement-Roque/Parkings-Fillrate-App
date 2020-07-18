import datetime

class Parking():

	def __init__(self,name:str,label:str,status:str,free:int,total:int,last_update:datetime):
		self.name = name
		self.label = label
		self.status = status
		self.free = free
		self.total = total
		self.last_update = last_update

	def toJson(self)->dict:

		return {
			"Name" : self.name,
			"Label" : self.label,
			"Status" : self.status,
			"Free" : self.free,
			"Total" : self.total,
			"Last_update" : self.last_update.strftime('%Y-%m-%dT%H:%M:%S'),
		}