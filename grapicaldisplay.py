from detective import SherlockHolmes
from tkinter import *
from tkinter import messagebox
class guiDisplay:
	def __init__(self,content):
		self.valueIwannafind = ""
		self.content = content
		# variable to store data from the detective
		self.ContentFoundBydetective = []

	def callThedetectiveJuan(self):
		detectiveHomes  = SherlockHolmes(self.content,self.valueIwannafind.get())
		detectiveHomes.findByphone()
		if len(detectiveHomes.givebackValue()) > 0:
			self.ContentFoundBydetective.append(detectiveHomes.givebackValue())
			self.showContentFound()


	def displaySearch(self):
		Label(text="        ", width=30).grid(row=1, column=1)
		Label(text="        ", width=30).grid(row=1, column=2)
		self.valueIwannafind = Entry(text="valueToCheck", width=30)
		self.valueIwannafind.grid(row=2, column=1)
		Button(text="find",width=25 , command = self.callThedetectiveJuan).grid(row=2, column=2)
		Label(text="        ", width=30).grid(row=3, column=1)
		Label(text="        ", width=30).grid(row=3, column=2)
	
	def makeLISTintoString(self,valueTORepair):
		RepairDone = " ".join(str(x) for x in valueTORepair)
		return RepairDone


	def showContentFound(self):
		ID = self.ContentFoundBydetective[-1]['ID']

		name = self.ContentFoundBydetective[-1]['name']
		changeToString =  self.makeLISTintoString(self.ContentFoundBydetective[-1]['Full Adress'])
		try:
			lastname = self.ContentFoundBydetective[-1]['Last Name']
		except IOError:
			print('lastname its not on json....')

		messagebox.showinfo("Info", str(ID) + " " + name + "  " +  lastname +"  "+ changeToString)


