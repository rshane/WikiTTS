'''
Created on Jul 14, 2017

@author: shane
'''


import wikipedia
from gtts import gTTS
import os
from os import system

searchFor = input("What Wiki topic do you want to search? \n")
if searchFor == "random":
    wikiSearchResult = wikipedia.page(wikipedia.random(pages=1))
else:    
    wikiSearchResult = wikipedia.page(searchFor)
wikiContentUnicode = wikiSearchResult.content
#wikiContentAscii = wikiContentUnicode.decode("utf-8", "ignore")

inputFile = open(wikiSearchResult.title + ".txt", "a+", encoding='utf-8')
inputFile.write(wikiContentUnicode)
inputFilePath = os.path.abspath(inputFile.name)
print(inputFilePath)
commandString = "say -v Daniel -f " + inputFile.name.replace(' ', '\ ')  + " -o " + wikiSearchResult.title.replace(' ', '\ ') + ".aiff" 
system(commandString)
inputFile.close()
#slow - means speak slowly
#tts = gTTS(wikiContentAscii, lang='en-uk', slow=False)
#tts.save(wikiSearchResult.title + ".mp3")

