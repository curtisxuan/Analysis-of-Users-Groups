import codecs
import time
# create dict for embedding_d.txt. KEY is feature, VALUE is float vector
embedding_d = {}
in_file = "./embedding_d.txt"
count=0
with codecs.open(in_file, 'r', 'utf8') as f:
    for line in f:
        if count==0:
            count+=1
            continue
        info = line.rstrip().split('\t')
        vector = [float(v) for v in info[3].split(' ')]
#         print(info)
        embedding_d[info[0]]=vector

# print([sum(x) for x in zip(vector1, vector2)])
# convert all features to value sums and store in userVecD.txt
in_file = "./userD.txt"
with codecs.open(in_file, 'r', 'utf8') as f:
    for line in f:
        user = line.rstrip().split(' ')
        vecVal = [0 for i in range(50)]
        for i in range(1,len(user)):
            try:
                vecVal = [sum(x) for x in zip(vecVal, embedding_d[user[i]])]
            except:
                continue
        with open('userVecD.txt', 'a') as f:
            f.write(user[0] + ' ')
            for i in vecVal:
                f.write(str(i) + ' ')
            f.write('\n')
