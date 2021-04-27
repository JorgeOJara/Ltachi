from detective import JonhTheDetective
from tkinter import *
class guiDisplay:
	def __init__(self,content):
		self.valueIwannafind = ""
		self.content = content

	def callThedetectiveJohn(self):
		detectivejonh  = JonhTheDetective(self.content,self.valueIwannafind)
		detectivejonh.givebackValue()


	def displaySearch(self):
		Label(text="        ", width=30).grid(row=1, column=1)
		Label(text="        ", width=30).grid(row=1, column=2)
		self.valueIwannafind = Entry(text="valueToCheck", width=30)
		self.valueIwannafind.grid(row=2, column=1)
		Button(text="find",width=25 , command = self.callThedetectiveJohn).grid(row=2, column=2)
		Label(text="        ", width=30).grid(row=3, column=1)
		Label(text="        ", width=30).grid(row=3, column=2)

