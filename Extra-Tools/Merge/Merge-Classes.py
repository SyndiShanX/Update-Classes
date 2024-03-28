from itertools import zip_longest

filename1 = 'Old-Classes.txt'
filename2 = 'New-Classes.txt'
outfilename = 'Output.txt'

with open(filename1) as f1, open(filename2) as f2, open(outfilename, 'w') as of:
    for lines in zip_longest(f1, f2):
        for line in lines:
            if line is not None: print(line.rstrip(), file=of)
