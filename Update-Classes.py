import json
import os

fileDir = os.getcwd()
fileDir = fileDir.replace('\\', '/')
fileDir = fileDir + '/'

with open(input('Enter the Directory of your Diff File: '), 'r') as rawFile:
  rawText = " ".join(line.rstrip() for line in rawFile)
  editedText = '"dummy": "dummy-content",' + rawText

classString = ('{' + rawText + '}')
classJson = json.loads(classString)

themeDir = input('Enter the Directory of your Theme File: ')

themeFile = open(themeDir, 'r')
themeText = themeFile.read()

i = 1
classNum = len(editedText.split('":')) - 2

while i < classNum:
  class1 = classJson[editedText.split('":')[i].split('"')[3]]
  class2 = classJson[editedText.split('":')[i + 1].split('"')[3]]

  themeText = themeText.replace(class1, class2)

  i = i + 2

with open(fileDir + 'Output.css', "w") as outputFile:
  outputFile.write(themeText)
