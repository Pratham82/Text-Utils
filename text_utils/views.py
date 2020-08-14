from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')


def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

# This will be the main endpoint
def analyze(request):
	
	inputText = request.POST.get('text', 'default')
	unChangedInput = request.POST.get('text', 'default')
	
	
	#* Checkbox values
	remmovePuncVal = request.POST.get('removePunc', 'default')
	allCapsVal = request.POST.get('allCaps', 'default')
	removeNewLinesVal = request.POST.get('removeNewLines', 'default')
	removeExtraSpaceVal = request.POST.get('removeExtraSpace', 'default')
	charCountVal = request.POST.get('charCount', 'default')

 

	#* Method for removing punctuations
	if remmovePuncVal == 'on':
		#* Method for removing punctuations
		def remPunc(str):
			punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
			val = ''
			for char in str:
				if char not in punctuations:
					val += char 
			return val
		inputText = remPunc(inputText)
		message = 'Remove Punctuations'
	
	#* Method for Capitalizing every character
	if allCapsVal == 'on':
		def allCaps(str):
			return "".join(list(map((lambda c: c.capitalize()), list(str))))
		
		inputText = allCaps(inputText)
		message = 'Capitalize every character'

	#* Method for Removing new lines
	if removeNewLinesVal == 'on':
		analyzed = ""
		for char in inputText:
			if char != "\n" and char != "\r":
				analyzed = analyzed + char

		inputText = analyzed
		message = 'Capitalize every character'


	#* Method for Removing extra space
	if removeExtraSpaceVal == 'on':
		def removeExtraSpace(str):
			return " ".join(str.split())
			
		inputText = removeExtraSpace(inputText)
		message = 'Capitalize every character'

	#* Method for Removing extra space
	if charCountVal == 'on':
		def charCount(str):
			return len("".join(list(filter((lambda v: v != ' '), list(str)))))
			
		inputText = charCount(inputText)
		message = 'Capitalize every character'

	# #* Error message
	
	if(remmovePuncVal != "on" and removeNewLinesVal!="on" and removeExtraSpaceVal!="on" and allCapsVal!="on"):
		inputText = unChangedInput
		message = 'Operation not selected'


	output = {'input': unChangedInput, 'result': inputText, 'message': message }
	return render(request, 'output.html',output )