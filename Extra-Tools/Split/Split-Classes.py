inputFileDir = 'Changes.txt'
outputFileDir1 = 'Old_Output.txt'
outputFileDir2 = 'New_Output.txt'

outputText1 = ''
outputText2 = ''

with open(inputFileDir, 'r') as inputFile:
  inputText = "\n".join(line.rstrip() for line in inputFile).split('\n')

i = 0
classNum = len(inputText) - 1

while i < classNum:
  class1 = inputText[i]
  class2 = inputText[i + 1]

  outputText1 = outputText1 + '\n' + class1
  outputText2 = outputText2 + '\n' + class2

  i = i + 2

with open(outputFileDir1, "w") as outputFile1:
  outputFile1.write(outputText1)
  
with open(outputFileDir2, "w") as outputFile2:
  outputFile2.write(outputText2)