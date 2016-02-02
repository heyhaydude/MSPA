import csv
import itertools
import numpy as np
    
with open(r'D:\Dev\MSPA\400 - MathModellers\week 4\train.csv') as fl:
    
    data =np.genfromtxt('D:\\Dev\\MSPA\\400 - MathModellers\\week 4\\train.csv',delimiter=",",missing_values='',skip_header=1)

    print(data[:,][1:2])




    #flreader = csv.reader(fl, delimiter=",",quoting=csv.QUOTE_NONE)
    
    #sex = []
    #survived = []
    #next(flreader)
    #for row in flreader:
    #    sex.append(row[5][0])
    #    survived.append(int(row[1]))

    #total_survived = sum(survived)
    #total_passengers = len(survived)
    #total_male = len(sex[sex=='m'])
    #total_female = total_passengers - total_male 
    #print('%d passengers survived out of %d' % (total_survived,total_passengers))
    
    #data = numpy.array(sex,survived)
   
    #print(total_male)
    #data = sex + survived
    #male_survived = sum(data[data[0]=='m'])

