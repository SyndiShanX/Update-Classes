inputFileDir = 'Changes.txt'
outputFileDir = 'Output.txt'

outputText = ''

with open(inputFileDir, 'r') as inputFile:
  inputText = "\n".join(line.rstrip() for line in inputFile).split('\n')

i = 0
classNum = len(inputText) - 1

while i < classNum:
  class1 = inputText[i]
  class2 = inputText[i + 1]

  outputText = outputText + '\n' + class2 + '\n' + class1

  i = i + 2

with open(outputFileDir, "w") as outputFile:
  outputFile.write(outputText)