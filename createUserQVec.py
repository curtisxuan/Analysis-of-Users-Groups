import codecs
import time
# create dict for embedding_d.txt. KEY is feature, VALUE is float vector
embedding_q = {}
in_file = "./embedding_q.txt"
count=0
with codecs.open(in_file, 'r', 'utf8') as f:
    for line in f:
        if count==0:
            count+=1
            continue
        info = line.rstrip().split('\t')
        vector = [float(v) for v in info[3].split(' ')]
#         print(info)
        embedding_q[info[0]]=vector

# print([sum(x) for x in zip(vector1, vector2)])
# convert all features to value sums and store in userVecQ.txt
in_file = "./userQ.txt"
with codecs.open(in_file, 'r', 'utf8') as f:
    for line in f:
        user = line.rstrip().split(' ')
        vecVal = [0 for i in range(50)]
        for i in range(1,len(user)):
            try:
                vecVal = [sum(x) for x in zip(vecVal, embedding_q[user[i]])]
            except:
                continue
        with open('userVecQ.txt', 'a') as f:
            f.write(user[0] + ' ')
            for i in vecVal:
                f.write(str(i) + ' ')
            f.write('\n')

