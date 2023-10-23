# NNW - my work 
# this program is to tell you how many positive, negative, 
# neutral words in a given txt file 

from matplotlib.pyplot import title


readFile = open('hound.txt','r').read() #houndofthebaskervilles textbook
posWords = open('positive.txt', 'r').read()
negWords = open('negative.txt', 'r').read()
neuWords = open('neutral.txt', 'r').read()

readFileList = readFile.split()

counter1 = 0
counter2 = 0
counter3 = 0
    
for word in readFileList:
    if word in posWords:
        counter1 += 1
            #print(word)

for words in readFileList:
    if words in negWords:
        counter2 += 1
            #print(words)
        
for wordz in readFileList:
    if wordz in neuWords:
        counter3 += 1
            #print(wordz)

print("Positive word amount: ",counter1, "for file ", readFile.title)
print("Negative word amount: ",counter2, "for file ", readFile.title)
print("Neutral word amount: ",counter3, "for file ", readFile.title)







