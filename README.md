# CS410_Final_Project - Professional Health Search

## Introduction : 
The system aims to find medical health professionals in the given research areas. The underlying data we are collecting from web crawler from different hospitals like https://nyulangone.org/ and rank it. The code is available here. We are utilizing the common code from Expert Search system (https://github.com/CS410Fall2020/ExpertSearch).
At part of search we will display specialization, doctor and contact information. For Ranking we will use BM25. 


## Team members :
1. Ambalika Roy
2. Sharad Kaushik
3. Faizan Ali Danish Khan

## Implementation of the application:

#### 1 Front end: 
    We used java script, CSS3 and bootstrap to create UI.
#### 2 Back end: 
    Gunicorn,Flask and python.

## An overview of the Software:
   The purpose of the code is find the specialized doctors based on search term.
   The user inputs a search term like 'Cardiology' then our system will return following results.
    1.	Total number of doctors who are specilzied in Cardiology
    2.	Matching term preview.
    3.	Doctors name and degree.
    4.	A link to navigate to doctor info page


## Steps to run the code.

 Make sure you have python 2.7.x 

#### Step 1 - Clone code 
    git clone https://github.com/toskaushik/ExpertSearch.git

#### Step 2 -  Navigate to ExpertSearch
    cd ExpertSearch

#### Step 3 -  Install dependencies
    pip install -r requirements.txt

#### Step 4 -  Run the application using Gunicorn
    gunicorn server:app -b 127.0.0.1:5000
 
##### Note - We tested Application in Mac and Linux OS.
