# Movie Recommendation System using Content-Based Filtering
- This is a movie recommendation system that eecommendate movies based on the similarity of the movies with the given movie entered by user.

## Overview
- The system uses content-based filtering to recommend movies. It analyzes the features of movies (such as genre, cast, director, etc.) to find similar movies and recommend them to users.

## Requirements
- Python 3.x
- Pandas
- Scikit-learn
- NumPy
- Flask
- Requets
- Response

Enter a movie title when prompted, and the system will recommend similar movies.

## Dataset
- The system uses the tmbd dataset, specifically the tmdb_5000_moviea.csv and tmdb_5000_credits.csv files.

## How it works
- The system uses the following steps to recommend movies:

### Data Preprocessing:
- Load the dataset and preprocess the data (e.g., handle missing values, convert categorical variables to numerical values).
- The data is preprocessed using NLP(natural language processing) techniques. (PorterStemmer etc.)
### Feature Extraction:
Extract features from the movie content (e.g., genre, cast, director) using text processing techniques (e.g., TF-IDF).
### Similarity Calculation:
- Calculate the similarity between movies based on their features (e.g., cosine similarity).
- Recommendation Generation: For a given movie, find similar movies based on the calculated similarities and recommend them to the user.
### Deployment:
- First the variable containing cosine similarity matrix and movie list dictinary are dump as .pkl file as named "similarity.pkl" and "movie_dic.pkl" respectively , So to use them in Deplyment.
- The system is deployed using Flask Python framework
- The deploy model simply take movie name from one html file and request the main.py file to recommendate movies.

