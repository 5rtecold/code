import json
import csv

# import sys

with open("correspondence-1.csv") as f:
    contents_of_f = csv.reader(f)
    diary = []
    for line in contents_of_f:
        diary.append(line)
    
data = {}
kees = ()

for i in diary[0]:
    kees = tuple(diary[0])
print(kees)
l=[]
for i in range(len(diary)):
    if i == 0:
        pass
    else:
        l.append(diary[i])
print(l)        
kees1 = ('name', 'cnic')
l=['Ilyas', '3520228348195']
l2=[]
# d={}

d = dict(zip(kees1, l))
print(d)
# __________________pandas

# df = pd.read_csv('correspondence-1.csv')
# df.to_json('output.json', orient='records', lines=True)
