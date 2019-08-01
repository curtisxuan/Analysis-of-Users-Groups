import codecs
import re
import time
info=[]
count=0
in_file = './batch.bfm'
with codecs.open(in_file, 'r') as f:
    for line in f:
        if count%100000==0:
            print(count)
        user = line.rstrip().split(' ')
#         print(user[2])
        #extract user id, stored in VAR:userid.group(0)
        userid = re.search ('\d*(?=_ie)', user[2])
        if userid:
#             print(userid.group(0))
#             print(count)
            q=[userid.group(0)]
            d=[userid.group(0)]
            for i in range (5,len(user)):
                if user[i].startswith('q:'):
                    q.append(user[i][2:])
                elif user[i].startswith('d:'):
                    d.append(user[i][2:])
            with open('userQ.txt', 'a') as f:
                for i in q:
                    f.write(i + ' ')
                f.write('\n')
            with open('userD.txt', 'a') as f:
                for i in d:
                    f.write(i + ' ')
                f.write('\n')
            count+=1    
        else:
            continue
            count+=1
# print(len(info))
