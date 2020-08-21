#import libraries
import string 
from collections import Counter
import matplotlib.pyplot as plt 


from nltk.tokenize import word_tokenize

#Cleaning the text
#----------------------------------------
#convert to lowercase 
#remove punctuations 
text = open('read.txt', encoding= 'utf-8').read()
lower = text.lower()
clean_text = lower.translate(str.maketrans('','',string.punctuation))


#Tokenization and removing stop words 
#----------------------------------------
#tokenize the text by extracting each word 
#remove unwanted words by creating a stop words list 
tokenized = clean_text.split()
#nltk stop words list
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", 
            "ourselves", "you", "your", "yours", "yourself", "yourselves", 
            "he", "him", "his", "himself", "she", "her", "hers", 
            "herself", "it", "its", "itself", "they", "them", "their", 
            "theirs", "themselves", "what", "which", "who", "whom", 
            "this", "that", "these", "those", "am", "is", "are", "was",
            "were", "be", "been", "being", "have", "has", "had", 
            "having", "do", "does", "did", "doing", "a", "an", "the", 
            "and", "but", "if", "or", "because", "as", "until", "while", 
            "of", "at", "by", "for", "with", "about", "against", "between", 
            "into", "through", "during", "before", "after", "above", "below", 
            "to", "from", "up", "down", "in", "out", "on", "off", "over", 
            "under", "again", "further", "then", "once", "here", "there", 
            "when", "where", "why", "how", "all", "any", "both", "each", 
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", 
            "only", "own", "same", "so", "than", "too", "very", "s", "t", "can",
            "will", "just", "don", "should", "now"]

final_text = []
for word in tokenized:
    if word not in stop_words:
        final_text.append(word)

emotions_list =[]
with open('emotions.txt', 'r') as file: 
    for line in file:
        final_line = line.replace('\n', '').replace(',','').replace("'",'').strip()
        word, emotion = final_line.split(':')
        
        if word in final_text:
            emotions_list.append(emotion)

print(emotions_list)

emotions_count = Counter(emotions_list)
print(emotions_count)

fig, ax = plt.subplots()
ax.bar(emotions_count.keys(), emotions_count.values())
fig.autofmt_xdate()
plt.title('emotions_count')
plt.savefig('emotions_count.png')
plt.show()