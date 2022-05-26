test1 = "This is a test of the emergency text system" 
outfile = open('file1.txt', 'wt')
outfile.write(test1)
outfile.close()
with open('file1.txt', 'rt') as infile:
    test2=infile.read()
print(len(test2))