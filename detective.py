class JonhTheDetective:
	def __init__(self,content,valueYouwannacheck):
		self.content = content
		self.valueYouwannacheck = valueYouwannacheck
		self.finalContentValue =[] 

	def findByphone():
		for x in range(len(content)):
			for rows in range(len(content[x]['mobile'])):
				if(content[x]['mobile'][rows] == self.valueYouwannacheck):
					print("we have a match...")

	
				# for end results
	def givebackValue(self):
		return self.finalContentValue


