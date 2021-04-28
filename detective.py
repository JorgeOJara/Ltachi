class JonhTheDetective:
	def __init__(self,content,valueYouwannacheck):
		self.content = content
		self.valueYouwannacheck = int(valueYouwannacheck)
		self.finalContentValue =[]

	def findByphone(self):
		# 8635892236.0
		for x in range(len(self.content)):
			for rows in range(len(self.content[x]['Mobile'])):
				if self.content[x]['Mobile'][rows] == self.valueYouwannacheck:
					self.finalContentValue.append(self.content[x])
					
		if len(self.finalContentValue) > 0:
			print('its a number')
		else:
			self.findBylandline()


	def findBylandline(self):
		# 8636763640
		for x in range(len(self.content)):
			for rows in range(len(self.content[x]['landLine'])):
				if self.content[x]['landLine'][rows] == self.valueYouwannacheck:
					self.finalContentValue.append(self.content[x])

		if len(self.finalContentValue) > 0:
			print('its a landline')
		else:
			print('not found..')
	

	def givebackValue(self):
		return self.finalContentValue
