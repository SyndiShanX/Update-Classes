from collections import OrderedDict
import os

inputFileDir = 'Changes.txt'
mergedFileDir = 'Merged.txt'
outputFileDir = 'Output.txt'

with open(inputFileDir, 'r') as inputFile:
  inputText = "\n".join(line.rstrip() for line in inputFile).split('\n')

i = 0
classNum = len(inputText) - 1

mergedText = ''

print('Merging Classes...')

while i < classNum:
  class1 = inputText[i]
  class2 = inputText[i + 1]
  
  if mergedText != '':
    mergedText = mergedText + '\n' + class1 + ', ' + class2
  else:
    mergedText = class1 + ', ' + class2

  i = i + 2
  
with open(mergedFileDir, "w") as mergedFile:
  mergedFile.write(mergedText)
  
print('Removing Duplicates...')

with open(mergedFileDir, 'r') as mergedFile:
  lines = (line.rstrip() for line in mergedFile)
  unique_lines = OrderedDict.fromkeys( (line for line in lines if line) )

splitList = list(unique_lines.keys())

i = 0
classNum = len(splitList) - 1

outputText = ''

print('Splitting Classes...')

while i < classNum:
  class1 = splitList[i].split(', ')[0]
  class2 = splitList[i].split(', ')[1]

  if outputText != '':
    outputText = outputText + '\n' + class1 + '\n' + class2
  else:
    outputText = class1 + '\n' + class2

  i = i + 1

os.remove(mergedFileDir)

with open(outputFileDir, "w") as outputFile:
  outputFile.write(outputText)