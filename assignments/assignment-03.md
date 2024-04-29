# Assignment 03

**Group members**
- First member student's name (student ID number) (number of problem that you solve)
- Second member student's name (student ID number) (1)
- Third member student's name (student ID number) (2, 4)
- etc.


## Problem 1
Explain with your own words how Naive Bayes classifier can be used to 
identify spam and non-spam email. Provide with simple examples, figures,
and demonstration with simple data sets.

## Problem 2
Using California housing dataset (this dataset can be accessed through
[scikit-learn library](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset)),   
perform kNN to that data set. Please follow the below hints:
1. Create two classes, divide the data rows from the column target `MedHouseVal`
   where label 1 (high value) is the median house value greater than or equal to
   $180,000 and label 0 (low value) for the median house value less than
   $180,000.
2. Select two attributes/features/variables that explicitly show a clear cut 
of division between class. In total there are 8 attributes/features/variables.

## Problem 3
With the samme dataset from Problem 2 and now without differentiate the
data rows into two classes, perform clustering to the two selected 
attributes/features/variables. What is your optimum number of classes?

## Problem 4
Perform word2vec for Harry Potter Book 1. You can download the text data 
from [here](https://www.kaggle.com/datasets/santiviquez/hp1txt).
Some hints to solve this problem:
- Remove rows that do not contain any text
- Remove double quotes in each sentences (and also all the non alphabet characters)
- Remove stopwords. See [this solution](https://stackoverflow.com/a/5486535)   
  from stackoverflow.
- Set the words into lowercase
- [optional] Transform each word using Snowball stemmer. See [this tutorial](https://www.nltk.org/howto/stem.html)
  from NLTK module
