# Content-Based Movie Recommendation System

A content-based movie recommendation application that finds movies similar to a user-selected title using movie metadata and text-similarity techniques.

## How it works

```
Movie metadata
     ↓
Text preprocessing
     ↓
Feature representation
     ↓
Cosine similarity
     ↓
Top similar movies
     ↓
Flask web application
```

The training notebook preprocesses movie metadata with NLP techniques such as stemming and builds a similarity-based recommendation system. The deployment component loads the precomputed movie data and similarity matrix and serves recommendations through Flask.

## Features

- Content-based recommendation rather than collaborative filtering.
- NLP preprocessing of movie metadata.
- Similarity calculation using cosine similarity.
- Precomputed artifacts for fast inference in the web application.
- Flask-based web interface.

## Technology

**Python · Pandas · NumPy · scikit-learn · NLTK · Flask · HTML/CSS**

## Repository structure

```
.
├── movie_recommend.ipynb
├── deplyment/
│   ├── application.py
│   └── templates/
└── README.md
```

> The original directory name `deplyment` is retained to avoid breaking the existing project structure.

## Running the project

### Notebook

Open `movie_recommend.ipynb` to inspect the data preprocessing and recommendation pipeline.

### Flask application

The deployment code expects the precomputed `movies.pkl` and `similarity.pkl` artifacts in the working directory used by the Flask application.

Install the required Python packages:

```bash
pip install pandas numpy scikit-learn nltk flask requests
```

Then run the Flask application from the deployment directory after placing the required model artifacts there:

```bash
python application.py
```

## What I learned

This project was an early hands-on implementation of a recommendation workflow: transforming unstructured movie metadata into features, measuring item-to-item similarity, and connecting the result to a usable web application.

## Limitations

- Recommendations depend on the metadata representation used by the project.
- The current implementation performs a simple title lookup and similarity ranking.
- There is no offline recommendation evaluation suite in the repository yet.

## Possible next steps

- Add precision@k / recall@k style evaluation.
- Improve feature engineering and handle missing metadata more systematically.
- Add input validation and an API layer.
- Containerize the Flask service.
- Add automated tests and CI.

## Author

**Ronak Vekariya**

[GitHub](https://github.com/Ronakvekariya)
