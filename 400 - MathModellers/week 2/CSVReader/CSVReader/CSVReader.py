import csv
import itertools
  
combined = open(r'D:\Dev\MSPA\400 - MathModellers\week 2\combined.csv','wb')
writer = csv.writer(combined)

with open(r'D:\Dev\MSPA\400 - MathModellers\week 2\trainLabels.csv') as labelfile, open(r'D:\Dev\MSPA\400 - MathModellers\week 2\train.csv') as trainfile:
        
    labelreader = csv.reader(labelfile, delimiter=",",quoting=csv.QUOTE_NONE)
    trainreader = csv.reader(trainfile, delimiter=",",quoting=csv.QUOTE_NONE)

    for info1, info2 in itertools.izip(labelreader,trainreader):
        writer.writerow(info1 + info2)

