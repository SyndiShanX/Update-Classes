import os

# Delete Output File if it already Exists
if os.path.exists('Output.txt') == 1:
  os.remove('Output.txt')

# Open, Read, then Close Files
oldFile = open('stable.js', 'r')
newFile = open('canary.js', 'r')

oldFileLines = oldFile.readlines()
newFileLines = newFile.readlines()

oldFile.close()
newFile.close()

# Define Empty Lists
oldFileGroups = []
newFileGroups = []

# Create List of the Functions in the Old File
oldFileLines = '\n'.join([line.strip() for line in oldFileLines])
for x in range(0, len(oldFileLines.split('e.exports = {')) - 1):
  oldFileGroups.append(oldFileLines.split('e.exports = {')[x + 1].split('}')[0].split('\n'))

# Create List of the Functions in the New File
newFileLines = '\n'.join([line.strip() for line in newFileLines])
for x in range(0, len(newFileLines.split('e.exports = {')) - 1):
  newFileGroups.append(newFileLines.split('e.exports = {')[x + 1].split('}')[0].split('\n'))

# Create Output File
outputFile = open('Output.txt', 'a+')

print("Diff:")

# Check if the Function Groups are the Same Length
for z in range(0, 3):
  for x in range(0, len(oldFileGroups)):
    if len(newFileGroups) > x + z:
      if len(oldFileGroups[x]) == len(newFileGroups[x + z]):
        for y in range(0, len(oldFileGroups[x])):
          oldFileLine = oldFileGroups[x][y]
          newFileLine = newFileGroups[x + z][y]
            
          # Ensure Lines aren't Empty
          if oldFileLine != '' and newFileLine != '':
          
            # Check if the Key Names are the same
            if oldFileLine.split(': "')[0] == newFileLine.split(': "')[0]:
          
              # Compare the Current Line
              if oldFileLine != newFileLine:
              
                # Output the Removed Line
                if oldFileLine != '':
                  if len(oldFileLine.split(': "')) > 1:
                    print("- " + oldFileLine.split(': "')[1].split('"')[0].split(' ')[0])
                    outputFile.write(oldFileLine.split(': "')[1].split('"')[0].split(' ')[0] + '\n')
              
                # Output the Added Line
                if newFileLine != '':
                  if len(newFileLine.split(': "')) > 1:
                    print("+ " + newFileLine.split(': "')[1].split('"')[0].split(' ')[0])
                    outputFile.write(newFileLine.split(': "')[1].split('"')[0].split(' ')[0] + '\n')