sentence = input("Enter sentence ")
seqCount = {}

for i in sentence:
    if i in seqCount:
        seqCount[i] +=1
    else:
        seqCount[i] = 1

print(seqCount)