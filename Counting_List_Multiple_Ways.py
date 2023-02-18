
# To determine number of word appearance in a list. 
# Program Structure:  
# Program Paragdim: 0. Procedural 1. Functional.  
# To learn: Efficiency. 

word_list = ['Soul', 'Effort', 'Will',"Soul", "Effort","Will"]
# Idea 1: iterate over the list and count each word, create a dictionary, some pattern to do two steps in one. 
word_count = {}
for word in word_list: 
    if word not in word_count.keys(): # Avoid method call  using in. 
        word_count[word] = 1
    else: 
        word_count[word] += 1

# Functional: dictionary Comprehension 
{k:word_list.count(k) for k in set(word_list)} 

# Mose Efficient using modules. 
import collections 
print(collections.Counter(word_list))
