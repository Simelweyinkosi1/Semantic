""" Finding similarities in words
"""
import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2)) # 0.59299 Cat and monkey have more similarity both animals
print(word3.similarity(word2)) # 0.40415 monkey & banana have 40% because monkey eats bananas
print(word3.similarity(word1)) # 0.22358 least likely less likelihood probalbly because cats dont eat bananas

# Compare series of words to one another - Working with Vectors
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

"""
Note
Output shown below

cat cat 1.0                   - similar 100%
cat apple 0.20368057489395142 - Less likely cats don't eat apple
cat monkey 0.5929929614067078 - both animals 50/50 maybe because different families
cat banana 0.2235882580280304 - Less likely cats don't eat banana
apple cat 0.20368057489395142 - Less likely cats don't eat apple
apple apple 1.0               - similarity = 100%
apple monkey 0.2342509925365448 - 
apple banana 0.6646699905395508
monkey cat 0.5929929614067078
monkey apple 0.2342509925365448
monkey monkey 1.0
monkey banana 0.4041501581668854
banana cat 0.2235882580280304
banana apple 0.6646699905395508
banana monkey 0.4041501581668854
banana banana 1.0
"""

# Own Example

word1 = nlp("Freedom")
word2 = nlp("Speech")
word3 = nlp("Fighter")

print(word1.similarity(word2)) # 0.59299 Cat and monkey have more similarity both animals
print(word3.similarity(word2)) # 0.40415 monkey & banana have 40% because monkey eats bananas
print(word3.similarity(word1)) # 0.22358 least likely less likelihood probalbly because cats dont eat bananas

# Compare series of words to one another - Working with Vectors
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))



# Working with sentences

sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ",similarity)

""" Note

Where did my dog go -  0.6085941301496852 - above 50% i guess they are all questions and the word my appear in both sentences
Hello, there is my car -  0.8033180111627156 - highest similarity both sentences end with car
I've lost my car in my car -  0.6787541571030323 - this sentence also ends with car but the similarity is lower
I will name my dog Diana -  0.6491444051802615 - the similarity is high above 50% percent but i only see the word my in both sentences

"""