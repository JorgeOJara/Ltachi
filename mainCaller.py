# python modules 
import json
# costume Scripts
from newCopyRefact import xslToJson
from newRefactJSONReformat import ReFormatJson

try:
	with open('end.json', 'r') as StringFromJson:
		load  = json.load(StringFromJson)
		final_dictionary = eval(load)
		print(final_dictionary)
except IOError:
	# because it cant find file, hes making one.. for the next time
	# later add input to send name of the file you wanna format
	load = xslToJson("me2.xlsx")
	headersGiver = load.giveHeadersBack()
	valueFromContent =  load.giveValueBack()
	formatingJson = ReFormatJson(headersGiver,valueFromContent)
	formatingJson.headFinderManager()
	formatingJson.saveToFile()
	print(formatingJson.giveBackFinalList())