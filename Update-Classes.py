import os

fileDir = os.getcwd()
fileDir = fileDir.replace('\\', '/')
fileDir = fileDir + '/'

changesDir = input('Enter the Directory of your Diff File (Leave Blank to use Changes.txt): ')
if changesDir == '':
  changesDir = 'Changes.txt'
  
with open(changesDir, 'r') as rawFile:
  rawText = "\n".join(line.rstrip() for line in rawFile).split('\n')

themeDir = input('Enter the Directory of your Theme File (Leave Blank to use Input.css): ')
if themeDir == '':
  themeDir = 'Input.css'

themeFile = open(themeDir, 'r')
themeText = themeFile.read()

i = 0
classNum = len(rawText) - 1

while i < classNum:
  class1 = rawText[i]
  class2 = rawText[i + 1]

  themeText = themeText.replace(class1, class2)

  i = i + 2

with open(fileDir + 'Output.css', "w") as outputFile:
  outputFile.write(themeText)
