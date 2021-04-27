# python modules 
import json
from tkinter import *
from tkinter import filedialog
# costume Scripts
from newCopyRefact import xslToJson
from newRefactJSONReformat import ReFormatJson



root = Tk()
root.title('LIstTachi')


# take file specified by user 
root.filename = filedialog.askopenfilename(initialdir='/',title='Select file',filetypes=(("xlsx files",".xlsx"),("all files","*.*")))
direcionOfFile = root.filename
fullName = direcionOfFile.split("/")
onlyFileName = fullName[-1].split('.')

# try to find a json file already made 
# if not make that shit
try:
	with open(onlyFileName[0] + ".json", 'r') as StringFromJson:
		load  = json.load(StringFromJson)
		final_dictionary = eval(load)
		print(final_dictionary)
except IOError:
	# because it cant find file, hes making one.. for the next time
	# later add input to send name of the file you wanna format
	load = xslToJson(direcionOfFile)
	headersGiver = load.giveHeadersBack()
	valueFromContent =  load.giveValueBack()
	formatingJson = ReFormatJson(headersGiver,valueFromContent,onlyFileName[0])
	formatingJson.headFinderManager()
	formatingJson.saveToFile()
	print(formatingJson.giveBackFinalList())



root.mainloop()