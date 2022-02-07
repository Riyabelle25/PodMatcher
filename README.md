# MLH Fellowship Orientation Hackathon | POD-MATCHER

## Making life easier at MLH, Matching mentees to their mentors!


<img width="1440" alt="Screenshot 2022-02-05 at 2 36 16 AM" src="https://user-images.githubusercontent.com/55790848/152603132-ef9fb46a-ce56-4429-81d4-990819984f08.png">

Check out our App [here](https://pod-matcher.herokuapp.com/)

## Introduction:
Recruiters have long found manually scanning resumes to be a time-consuming activity. Once they've combed through and filtered the resumes, they'll have to pair the mentees with a suitable mentor. The inspiration for the PodMatcher comes from the hope to automate this process for MLH in particular, and save time and resources. As part of the submission to the MLH hackathon, we created an application that:

* Asks user (presumably a Pod Mentor/MLH admin) to upload a ```requirements``` document detailing what skills/primary language/timezone they are looking for in potential mentees.

* These requirements are then matched with a set of applications that are stored in the ```firebase DB``` 

* The ranked applications are shown in decreasing order based on how closely they fit the uploaded requirements.

* PodMatcher is built on React therefore responsive across devices!


## Team Mates:rocket:


* Riya Elizabeth John [@Riyabelle25](https://github.com/Riyabelle25) : ```Flask Backend | API integration | Heroku ``` 

* Deepti Ravi Kumar [@deepti-96](https://github.com/deepti-96) : ```Documentation | NLP```

* Priya Nagda [@pri1311](https://github.com/pri1311) : ```React Frontend```


## Project Details:

<img width="1440" alt="Screenshot 2022-02-05 at 2 37 58 AM" src="https://user-images.githubusercontent.com/55790848/152603316-4ffb7509-11f8-424d-bd8e-bf5e0ace7cb3.png">

This project uses:

```bash
* BoW and TF-IDF vectorizer to convert the text documents into vector form. 

* Cosine similarity as comparison function.

* Textract python library to read word documents.

* Flask, for the NLP tasks and hosting backend server.

* Firebase Firestore for the DB

* React for the Client side

* Heroku to host the application

* Can-Merge utility to determine whether or not a particular pull request can be merged 
without navigating to the web interface. 
The GraphQL API of GitHub is used to fetch the latest status of any status checks 
currently running and determine if the PR should be merged.

```

## Pre-processing:
The following pre-processing techniques have been used:
Removed stop words using stop words from nltk-corpus
A stop word is a word that occurs more frequently in any language. We often remove stop words from any document we process using Natural Language Processing, since keeping them increases document size if we keep them. When they are removed, we have fewer words to deal with.
Lexical lemmatization was done using WordNetLemmatizer.
The process of stemming words in a document to their root form is known as lemmatization. As a result, we can convert all of the verb forms to their root form. As a result, we'll have to compare two documents using absolute words. Working and working, for example, have the same root word work. All of the terms in our page will be transformed to their root form if we use lemmatization.

Documents must be converted into vectors after they have been pre-processed. The Python scikit-learn library offers different methods for vectorization. The following two methods were used: 
1. Bag of Words(BoW)
2. TF-IDF vectorizer

## BoW:
It's a Bag of all the words in a document, as the name implies. If we have more than one document, Bag will include all of the words from all of them. The index is used to refer to each word. Instead of counting the number of times each word appears in BoW, we will simply assume that if a word exists, it is represented as 1, and if it does not, it is represented as 0.

## TF -IDF:
Another method for converting text to vector form is the TF-IDF method.
Term Frequency (TF) is a term used to describe how often something happens. The following formula can be used to express this.
TF(word-i) = (number of times word-i appears in a document)/(number of words in the document) 
Inverse Document Frequency (IDF) is a term that refers to the frequency with which documents are produced. This is a metric for determining the significance of a word. A word's relevance is reduced if it appears in all of the papers. The following formula can be used to express this.
IDF(word-i) = log(Total Number of Documents /Total Number of Documents containing the word word-i)
Here, log is with base ‘e’. By using the above formula, the denominator becomes equal to the numerator when a word appears in all the documents. The significance of log1 declines accordingly. Multiplying both will give us TF-IDF.

## Cosine similarity:
To compare vectors, we need a measure that compares their similarity. An example of this would be cosine similarity. A cosine measurement deals with how close two vectors are to each other. It converts the distance between them into a similarity score between 0 and 100 percent based on the cosine angle between them.

<img width="1061" alt="can-merge utility 2022-02-04 at 3 30 38 PM" src="https://user-images.githubusercontent.com/55790848/152604272-8dae5ced-e821-4801-a0e1-70ed37f7be40.png">

