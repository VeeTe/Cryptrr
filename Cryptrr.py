import os
import random
import binascii
import codecs
import time
import numpy as np

def reassembleHexArrayToASCII(strHexArray):
	for line1 in strHexArray:
		strLine = bytes.fromhex(line1).decode('utf-8')
def string2Hex(strString):
	strHexArr = list(strString)
	strHexLetter = ""
	for letter in strHexArr:
		strHexLetter += str(format(ord(letter),"x"))	
	return(strHexLetter)
def hex2String(strHex):
	strString = str(codecs.decode(strHex, "hex"))
	strString = strString[2:len(strString)-1]
	return strString
def getVocabArray():
	try:
		strWordsArray = []
		try:
			fileOpen = open("20k.txt","r")
			
			for line1 in fileOpen:
				strWord = str(line1)
				strWord = strWord[0:(len(strWord)-1)]
				strWordsArray.append(strWord)
		except Exception:
			print("getVocabArray;Readfile has malfunctioned")
		return strWordsArray
	except Exception:
		print("getVocabArray has malfunctioned") 
def encodeHexLetter(strHexLetter):

	strArray = list("0123456789abcdef")
	strWordsArr = getVocabArray()
	intCounter1 = 0
	for strWord in strArray:
		if str(strWord) == strHexLetter:
			break
		intCounter1 += 1
	strWord = strWordsArr[intCounter1+16*random.randint(0,78)]
		
	return(strWord)
	
def encodeHex(strHex):
	strArray = []
	hexByLetterArr = list(strHex)
	for strLetter in hexByLetterArr:
		strArray.append(encodeHexLetter(str(strLetter)))
	return strArray

def decodeHex(strEncodedArr):
	try:
		strArray = list("0123456789abcdef")
		strWordsArr = getVocabArray()
		strWordsEncArr = []
		for strEncodedWord in strEncodedArr:
			intCounter1 = 0
			for strWord in strWordsArr:
				if strWord == strEncodedWord:
					break
				intCounter1+=1
			strWordsEncArr.append(intCounter1)
		strTranslatedHex = ""
		for intNumber in strWordsEncArr:
		
			strTranslatedHex += strArray[int(intNumber)%16]
		
		return hex2String(strTranslatedHex)
		
	except Exception:
		print("decodeHex has malfunctioned (normal if you're just trying to encode the message - disregard this) \n if you're trying to decode the message & you get this - the message is incomplete or corrupted. Lmao GLHF <3!")

def vocabMixer():
	
	strWordsArr = getVocabArray()
	npArray = np.array(strWordsArr)
	np.random.shuffle(npArray)
	with open("20k.txt", 'w') as f:
		for strItem in npArray:
			f.write(str(strItem)+"\n")

def makeRealisticSentence(strArrayWords):
	try:
		intWordsInSentences = random.randint(1,40)
		strSentence = ""
		intCounter1 = 0
		for strWord in strArrayWords:
			intRandom = random.randint(1,40)
			if strSentence != "":
				if strSentence[len(strSentence)-2] == "." or strSentence[len(strSentence)-2] == "?" or strSentence[len(strSentence)-2] == "!":
					strWord = strWord.capitalize()
				elif intCounter1 != len(strArrayWords)-1:
					if intRandom == 1 or intRandom == 4 or intRandom == 9:
						strWord += "."
					elif intRandom == 2:
						strWord += ","
					elif intRandom == 3: 
						strWord += ":"
					elif intRandom == 5:
						strWord += "!"
					elif intRandom == 6:
						strWord += "?"
					elif intRandom == 7:
						strWord += ";"
					elif intRandom == 8:
						strWord += " -"
			else:
				strWord = strWord.capitalize()
			strSentence += strWord + " "
			intCounter1 += 1
		strSentence = strSentence[0:(len(strSentence)-1)]
		intRandom = random.randint(1,4)
		if intRandom == 1 or intRandom == 4:
			strSentence += "."
		elif intRandom == 2:
			strSentence += "?"
		elif intRandom == 3: 
			strSentence += "!"
		return strSentence
	
	except Exception:
		print("makeRealisticSentence has malfunctioned")
def turnToArray(strSentences):
	try:
		strSentences=strSentences.replace(".","")
		strSentences=strSentences.replace(",","")
		strSentences=strSentences.replace("!","")
		strSentences=strSentences.replace(":","")
		strSentences=strSentences.replace("?","")
		strSentences=strSentences.replace(";","")
		strSentences=strSentences.replace(".","")
		strSentences=strSentences.replace(" -","")
		strSentences = strSentences.lower()
		strSentencesArr = []		
		strSentencesArr = strSentences.split(" ")
		return decodeHex(strSentencesArr)		
	except Exception:
		print("turnToArray has malfunctioned")
				
def bashCommandExec(strCommand):
	try:
		os.system (strCommand)
	except Exception:
		print("bashCommandExec has malfunctioned")

def saveFile(strContent,strFileName, strFileExtension):
	try:
		strFileName=str(os.getcwd()+"/"+str(strFileName)+"."+strFileExtension)
		with open(strFileName, 'w') as outfile:
			outfile.write(strContent)		
	except Exception:
		print("saveFile has malfuncitoned")

bashCommandExec("clear")	
print("X___________X___________________X___________________X___X_________________________________________X")
print("XXXXXXXXXXXXXXxXXXXXXXXXXXXXXXXXXXXXXXXxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxXXxx")
print("X       _..._  X                                        X                                      Xx")
print("X    .-'_..._''.                  X                                                       X    Xxxxx")
print("X  .' .'      '.\                         X _________   _...._                                 XxxxXX")
print("X / .'                      .-.          .- \ X      |.'      '-.                              XXXxXXX")
print("X. '              .-,.--.    \ \        / /  \        .'```'.    '.      .|   .-,.--.  .-,.--. XXX")
print("X| |              |  .-. |    \ \      / /    \      |       \     \   .'X|_  |  .-. | |  .-.X|XX")
print("X| |    X         | |  | |     \ \    / /  X   |     |        |    | .'     | | |  | | | |  | |XXXXX")
print("X. '              | |  | |      \ \  / /       |      \  X   /    . '--.  .-' | |  | | | |  | |XXXX")
print("X \ '.          . | |  '-        \ `  /        |     |\`'-.-'   .'     |  |   | |  '-  | |  '- XX")
print("X  '. `._____.-'/ | |     X       \  /         |     | '-....-'`       |  |   | |      | |     Xx")
print("X    `-.______ / X| |             / /         .'     '.                |  '.' | |      | |     xXXx")
print("X  X          `   |_|         |`-' /        '-----------'              |   /  |_| X    |_|     XxX")
print("X                              '..'                                X   `'-'                    Xx")
print("X_________________________________________________X_______________________________________v1.0_XXXX")
print("XXxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxXXXXXXXXXXXXXXXXXxXXX")
print("XXXXXXXX Made by ya boi ( VT ) XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxXXXXXXXXXXXXXXXXXXXXXXXXxxxXxx")
print("XXxXXXXXXXXXXXXXxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX made on 02/13/2022 XXXXXXXxXXXXXXXXXXXXXXXXXXXXX")
print("XXXxXXXXXXxXX_XXxXXX____XXX_XXXX_XXXXXXXX__XXXXX___XxXXX__XXXXXXXXXX_XXXXXXXXXXXXXXXXXXXxXXXXXXXXX")
print("XXXXxX Easy to encode and decode text, turning it into a plausibly deniable  string. XXXXXXXXXXXXXXXXXX")
print("xX How to use: XXXXXXXXXXXxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxXXXXXXXXxXx")
print("XXXXXxX 1) Make sure you have a 20k.txt key in the local folder XXXXXXXXXXXXXXXXXXxXXXXXXXXXXXXXXXXX")	
print("X 2) To use a custom key, drop it in the same folder as Cryptrr.py & rename it to 20k.txt XxXXXXXX")
print("XXXXXXXXxXXX 3) Use and enjoy the proggo - afterall shizz free :D & mayB virus free ;) XXXXxXXxXXx")	
print("X===============================================x====================================X=========x")
print("XXXXxXXXXXXXXXXXXxXXX DISCLAIMER XxXXXXXXXXXXXXXXXXXXXXXXXxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") 
print("xXXX This tool comes as is - use it at your own risk - plis don't do anyting illegal with it <3 XX")
print("XXXxXXXxX Softwares comes with no guarantees & by using it you consent to these terms & cond. XxX")
print("X===================X======================================================X===================XXx")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxXXXXXXXXXXXXXXXXXXXXXXXX") 
print("X [        Authors Notes:                                                                     ] xXx")
print("X [*Please do not use this tool to smuggle data in/out of production environment              ] XXXXXx") 
print("X [*Heads up, might trigger DLP if word salads are too large                                  ] XXXXX")
print("X [*Please do not use this tool to avoid/bypass IDS/IPS <3                                    ] X")
print("X [*Encoded output may vary so same 1 character has 78*78 variations of 2 words               ] XxxX")
print("x [*Encoded output is generated based on position of words in the 20k.txt dictionary, and can ] X")
print("X [     bizarre and inappropriate - so just a heads up (x_x)                                  ] XX")
print("X [Mad props to: https://github.com/first20hours/google-10000-english/blob/master/20k.txt     ] XxX")
print("XXXXXXXXXXXXXXXXXXXxXXxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxX")
print("XxX_.-=` 20k.txt is the key, if you shuffle it previous key may be irrecoverable XXXXXXXXXXXXXXXX")
print("XXXxX_.-=` if you need another key the current copy the 20k.txt in another folder XXXXXXXXXXXXXXXXXXXXX")
print("XXXX_.-=` Type yes to shuffle XXXXXXXXXXxXXXXXXXXXXXXXXXXXXXXXXXXXxXXXXXXXXXXXXXxXXXXXXXXXXXXXXXXXXXXXXXX")
print("XX_.-=` just a heads up; yes is case sensitive so make sure u type it right XxXXXXXXXXXXXXXXXXxXXXXxXXX")
print("XXXx_.-=` if shuffle was successful you'll see '20k.txt has been successfully shuffl'd lol' xXXXXXXXX")
print("Xx_.-=` Finally: to use a different key replace the existing one and then restart the program xXXXXXXXX")
print()	
strLocalInput = input("__Do_you_want_to_shuffle_current_key?__: ")
if strLocalInput == "yes":
	vocabMixer()
	print()
	print("XXXXxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxXXXXXXXXxXXXXX")
	print("xXx 20k.txt has been successfully shuffl'd lol XxxXXX")
	print("XXXxXXXXXXXXxXXXXXXXXXXXXXXXXXXXXXxXXXXXXXXxXXxXXXX")
	
while 1>0:
	UserInput = input ("\n"+"\n"+"\n"+"__String_to_encode_or_decode__: ")
	try:
		print("\n"+"Encoded Message: \n" + makeRealisticSentence(encodeHex(string2Hex(UserInput))) + "\n \n")
	except Exception:
		print("Encoded Message: \n" + "Error has occurred. Whoops."+ "\n \n")

	try:
		print("\n"+"Decrypted Message: \n" + str(turnToArray(UserInput))+ "\n \n")		
	except Exception:
		print("Decrypted Message: \n" + "Message entered cannot be decoded, this is normal if you are just trying to encode the message."+ "\n \n")
