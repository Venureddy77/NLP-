#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import pandas as pd
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)
subjects = ["Python", "Machine Learning", "Data Science", "Web Dev", "Statistics", "AI", "NLP", "SQL"]
adjectives = ["amazing", "confusing", "helpful", "outdated", "practical", "difficult", "engaging", "vague"]
nouns = ["lectures", "assignments", "quizzes", "grading", "instructor", "content", "projects", "videos"]
def generate_unique_feedback(target_count=50):
    feedback_set = set()
    while len(feedback_set) < target_count:
        comment = f"The {random.choice(subjects)} {random.choice(nouns)} were {random.choice(adjectives)}."
        feedback_set.add(comment)
    return list(feedback_set)
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
raw_comments = generate_unique_feedback(50)
results = []
for comment in raw_comments:
    tokens = word_tokenize(comment.lower())
    stems = " ".join([stemmer.stem(w) for w in tokens])
    lemmas = " ".join([lemmatizer.lemmatize(w) for w in tokens])
    results.append({
        "Original Comment": comment,
        "Stemmed Version": stems,
        "Lemmatized Version": lemmas
    })
df = pd.DataFrame(results)
print(df)
df.to_csv("student_feedback_full_50.csv", index=False)


# In[ ]:




