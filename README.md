# CS410_Final_Project - #Professional Health Search

## Introduction : 
The system aims to find medical health professionals in the given research areas. The underlying data we are collecting from web crawler from different hospitals like https://nyulangone.org/ and rank it. The code is available here. We are utilizing the common code from Expert Search system (https://github.com/CS410Fall2020/ExpertSearch).
At part of search we will display specialization, doctor and contact information. For Ranking we will use BM25. 


## Team members :
1. Ambalika Roy
2. Sharad Kaushik
3. Faizan Ali Danish Khan

## Implementation of the application:

### 1 Front end: 
    We used java script, CSS3 and bootstrap to create UI.
### 2 Back end: 
    Gunicorn,Flask and python.

## An overview of the Software:
The purpose of the code is find the specilized doctor based on search term.
The user inputs a search term like 'Cardiology' then our system will return following results.
•	Total number of dcotor who are specilzied in cardilogy
•	Matching term preview.
•	Doctor name and degree.
•	a link to navigate to doctor info page


## Steps to run the code.

 Make sure you have python 2.7.x 

### Step 1 - Clone code 
    git clone https://github.com/toskaushik/ExpertSearch.git

### Step 3 -  Navigate to ExpertSearch
    cd ExpertSearch

### Step 2 -  install dependencies
    pip install -r requirements.txt

### Step 3 -  run the application using Gunicorn
    gunicorn server:app -b 127.0.0.1:5000
    

## Progress Report:

1) Which tasks have been completed? 
  a) Completed design
  b) Data crawling 
  c) Service layer API to fetch documents
      
2) Which tasks are pending? 
  a) Data cleaning 
  b) Data tokenization
  c) Document indexing    (60% completed)
  d) Document ranking     (60% completed)
  e) UI module for search (70% completed)
  f) Unit and integration testing

3) Are you facing any challenges?
  Not so far
