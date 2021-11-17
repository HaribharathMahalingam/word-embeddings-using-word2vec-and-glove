Obtain word embeddings using Gensim, word2Vec and glove methods

I have obtained Pearson Correlation coeffecients for a datset of 999 word pairs and their human-judged similarities present at: https://fh295.github.io//simlex.html

Step1: install genism and import.

Step2: load word2vec dataset in a variable (wordVec) as a 300 dimensional vector.

Step3: evaluate the word pairs in SimLexA2.txt using wordVec.evaluate_word_pairs(“SimLexA2.txt”). 

Step4: obtain the Pearson correlation coefficients from the output of the previous step.

![3](https://github.com/HaribharathMahalingam/POS-tags-stanza-nltk/blob/main/3.PNG)

Step5: load glove dataset in a variable (glove) as a 300 dimensional vector.

Step6: evaluate the word pairs in SimLexA2.txt using glove.evaluate_word_pairs(“SimLexA2.txt”). 

Step7: obtain the Pearson correlation coefficients from the output of the previous step. 

![4](https://github.com/HaribharathMahalingam/POS-tags-stanza-nltk/blob/main/4.PNG)

I also obtained Pearson correlation coeffecients for 10 pair of words given a human score of their similarity.

Step8: evaluate the word pairs in task2.txt using wordVec.evaluate_word_pairs(“task2.txt”).

![1](https://github.com/HaribharathMahalingam/POS-tags-stanza-nltk/blob/main/1.PNG)

Step9: evaluate the word pairs in task2.txt using glove.evaluate_word_pairs(“task2.txt”).

![2](https://github.com/HaribharathMahalingam/POS-tags-stanza-nltk/blob/main/2.PNG)

The similarity scores for all 10 pair of words using word2Vec and glove are shown below,

![5](https://github.com/HaribharathMahalingam/POS-tags-stanza-nltk/blob/main/5.PNG)

![6](https://github.com/HaribharathMahalingam/POS-tags-stanza-nltk/blob/main/6.PNG)

Then, word2Vec nad glove was evaluated on 10 word analogy questions which was in the format supported by Gensim,

![7](https://github.com/HaribharathMahalingam/POS-tags-stanza-nltk/blob/main/7.PNG)

Step10: evaluate for word analogy questions on task3.txt using analogy = wordVec.evaluate_word_analogies("task3.txt").

![9](https://github.com/HaribharathMahalingam/POS-tags-stanza-nltk/blob/main/9.PNG)

Step11: evaluate for word analogy questions on task3.txt using analogy1 = glove.evaluate_word_analogies("task3.txt").

Step12: evaluate accuracy for word2Vec using analogy[0].

![8](https://github.com/HaribharathMahalingam/POS-tags-stanza-nltk/blob/main/8.PNG)

Step13: evaluate accuracy for glove using analogy1[0].

![10](https://github.com/HaribharathMahalingam/POS-tags-stanza-nltk/blob/main/10.PNG)

Step14: display the correct and incorrect analogy using analogy[1] and analogy1[1].

Step15: Get a list of 10 common English words and evaluate the 5 most similar words for each of them with word2Vec (wordVec.most_similar()) and glove methods (glove.most_similar())




