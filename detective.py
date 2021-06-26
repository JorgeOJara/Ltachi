class SherlockHolmes:
	def __init__(self,content,valueYouwannacheck):
		self.content = content
		self.valueYouwannacheck = valueYouwannacheck
		self.finalContentValue =''

  # find by phone number
	def findByphone(self):
		try:
			for x in range(len(self.content)):
				for rows in range(len(self.content[x]['Mobile'])):
					if self.content[x]['Mobile'][rows] == int(self.valueYouwannacheck):
						self.finalContentValue = self.content[x]
			if len(self.finalContentValue) > 0:
				print('its a number')
			else:
				self.findBylandline()
		except:
			self.findByName()


   # find by landline

	def findBylandline(self):
		# 8636763640
		for x in range(len(self.content)):
			for rows in range(len(self.content[x]['landLine'])):
				if self.content[x]['landLine'][rows] == int(self.valueYouwannacheck):
					self.finalContentValue = self.content[x]

		if len(self.finalContentValue) > 0:
			print('its a landline')
		else:
			print('number not found..')

   # find by name 
	def findByName(self):
		for x in range(len(self.content)):
			if self.content[x]['name'] == str(self.valueYouwannacheck):
				self.finalContentValue = self.content[x]

		if len(self.finalContentValue) > 0:
			print('name found')
		else:
			print('not Found....')



   # function to return value from getters

	def givebackValue(self):
		return self.finalContentValue
