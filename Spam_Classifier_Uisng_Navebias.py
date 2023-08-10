# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:30:11 2023

@author: Arsalan Bakhtiar
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\Arsalan Bakhtiar\Downloads\spam.csv')

df.columns

df.groupby('Category').describe()



df['Spam'] = df['Category'].apply(lambda x : 1 if x=='spam' else 0)


from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(df.Message,df.Spam,test_size= 0.25)

from sklearn.feature_extraction.text import CountVectorizer
v = CountVectorizer()
X_train_count = v.fit_transform(X_train.values) 
X_train_count.toarray()[:3]

# corpus = All numique word in the dataset 


from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(X_train_count, y_train)

Email = [
    'U dun say so early hor... U c already then say...',
    'SMS. ac Sptv: The New Jersey Devils and the Detroit Red Wings play Ice Hockey. Correct or Incorrect? End? Reply END SPTV']

emails_count = v.transform(Email)


model.predict(emails_count)


X_test_count = v.fit_transform(X_test)
X_test_count.toarray()


model.score(X_test_count, y_test)


# PIPLINE

from sklearn.pipeline  import Pipeline

clf = Pipeline([('vectorizer',CountVectorizer()),
                ('nb',MultinomialNB())])


clf.fit(X_train, y_train)

clf.score(X_test, y_test)
































