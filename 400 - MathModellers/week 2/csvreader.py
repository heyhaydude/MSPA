import csv
import itertools
    
with open(r'D:\Dev\MSPA\400 - MathModellers\week 2\trainLabels.csv') as labelfile, open(r'D:\Dev\MSPA\400 - MathModellers\week 2\train.csv') as trainfile:
        
    labelreader = csv.reader(labelfile, delimiter=",",quoting=csv.QUOTE_NONE)
    trainreader = csv.reader(trainfile, delimiter=",",quoting=csv.QUOTE_NONE)
    
    for line in itertools.chain(labelreader.next(),trainreader.next()):
        print line
        