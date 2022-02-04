# POD-MATCHER


## Introduction:
Recruiters have long found manually scanning resumes to be a time-consuming activity. Once they've combed through and filtered the resumes, they'll have to pair the mentees with a suitable mentor. The inspiration for the PodMatcher came from the need to automate the entire process in order to save time and resources. As part of the submission to the MLH hackathon, we created an application that, when we submit a job description and a set of resumes to the tool, ranks resumes in decreasing order based on how closely they fit the job description.

## Pre-processing:
The following pre-processing techniques have been used:
Removed stop words using stop words from nltk-corpus
A stop word is a word that occurs more frequently in any language. We often remove stop words from any document we process using Natural Language Processing, since keeping them increases document size if we keep them. When they are removed, we have fewer words to deal with.
Lexical lemmatization was done using WordNetLemmatizer.
The process of stemming words in a document to their root form is known as lemmatization. As a result, we can convert all of the verb forms to their root form. As a result, we'll have to compare two documents using absolute words. Working and working, for example, have the same root word work. All of the terms in our page will be transformed to their root form if we use lemmatization.

Documents must be converted into vectors after they have been pre-processed. The Python scikit-learn library offers different methods for vectorization. The following two methods were used: 
Bag of Words(BoW)
TF-IDF vectorizer

## Bow:
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

## Project Details:
This project uses 
BoW and TF-IDF vectorizer to convert the text documents into vector form. 
Cosine similarity as comparison function.
Textract python library to read word documents.
Flask to make the whole project intractable with the user.
Heroku to host the backend server and Firebase Firestore for the database.
Can-Merge utility to determine whether or not a particular pull request can be merged without navigating to the web interface. The GraphQL API of GitHub is used to fetch the latest status of any status checks currently running and determine if the PR should be merged.
To build a Pod, you must first upload the Job Description for that pod in the requirements.txt file, which describes what skill sets, languages, time zones, and other factors the Matcher should consider. When an application is uploaded, the server sends a request to the Firestore database, which retrieves all of the applications, and then uses BoW and TF-IDF for vectorization and cosines similarity for comparison to provide a percentage-wise list of applicants.
The following is the result of putting all of the above components together:



