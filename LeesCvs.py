import csv
with open('toets.csv' , 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimeter = ' ', quotechar = '`|')

