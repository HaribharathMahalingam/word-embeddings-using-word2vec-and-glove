import gensim
import gensim.downloader as api
wordVec = api.load('word2vec-google-news-300')
glove = api.load("glove-wiki-gigaword-300")
print("TASK1")
pcc1 = wordVec.evaluate_word_pairs("SimLexA2.txt")
print("Pearson correlation coeffecients of SimLexA2.txt using word2Vec: ", pcc1)
pcc2 = glove.evaluate_word_pairs("SimLexA2.txt")
print("Pearson correlation coeffecients of SimLexA2.txt using glove: ", pcc2)
print("TASK2")
pearcc1 = wordVec.evaluate_word_pairs("task2.txt")
print("Pearson correlation coeffecients using word2Vec for task2: ", pearcc1)
a = ["table", "copy", "immense", "street", "broke", "present", "urban", "student", "ship", "steal"]
b = ["chair", "paste", "empty", "road", "fix", "future", "city", "teacher", "cruise", "loot"]
for i in range(len(a)):
    x = wordVec.similarity(a[i],b[i])
    print("The similarity score of", a[i], "and", b[i], "using word2Vec=", x)
pearcc2 = glove.evaluate_word_pairs("task2.txt")
print("Pearson correlation coeffecients using glove for task2: ", pearcc2)
a = ["table", "copy", "immense", "street", "broke", "present", "urban", "student", "ship", "steal"]
b = ["chair", "paste", "empty", "road", "fix", "future", "city", "teacher", "cruise", "loot"]
for j in range(len(b)):
    y = glove.similarity(a[j],b[j])
    print("The similarity score of", a[j], "and", b[j], "using glove=", y)
print("TASK3")
analogy = wordVec.evaluate_word_analogies("task3.txt")
print("Accuracy for word analogy questions by word2Vec:", analogy[0])
print("The correct and incorrect word analogies are shown below:")
print(analogy[1])
analogy1 = glove.evaluate_word_analogies("task3.txt")
print("Accuracy for word analogy questions by glove:", analogy1[0])
print("The correct and incorrect word analogies are shown below:")
print(analogy1[1])
print("TASK4")
list_words = ["vehicle", "knife", "ocean", "laptop", "jungle", "sorrow", "jacket", "excited", "safe", "garden"]
print("The 5 most similar words for each word estimated by word2Vec is shown below:")
for i in list_words:
        mswv = wordVec.most_similar(i)
        print(mswv[:5])
print("")
print("")
print("The 5 most similar words for each word estimated by Glove is shown below:")
for j in list_words:
    msg = glove.most_similar(j)
    print(msg[:5])
    
    
    
 
 
 
 
