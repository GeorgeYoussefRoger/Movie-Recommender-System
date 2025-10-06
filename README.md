# Movie Recommender System

A Content-Based Movie Recommendation System built using the TMDB 5000 Movies Dataset from Kaggle. It recommends similar movies based on a combination of metadata such as genres, keywords, cast, crew and movie descriptions using TF-IDF vectorization and cosine similarity.

## Project Structure

```
Movie-Recommendation-System/
├── data/
│ ├── tmdb_5000_movies.csv # Original TMDB 5000 movies dataset
│ ├── tmdb_5000_credits.csv # Cast and crew data corresponding to each movie
├── notebooks/
│ ├── 1_data_preprocessing.ipynb # Data cleaning, merging and missing value handling
│ ├── 2_feature_engineering.ipynb # Feature extraction
│ ├── 3_model_building.ipynb # TF-IDF vectorization, similarity calculation
├── ui/
│ └── app.py # Streamlit app for movie recommendations
├── .gitignore
├── README.md # Project documentation
└── requirements.txt # Dependencies
```

## Methodology

1. Data Preprocessing
   - Load and merge TMDB Movies and Credits datasets.
   - Retain relevant columns: `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`.
   - Handle missing values and export the clean dataset.
2. Feature Engineering
   - Parse JSON-like fields using `ast.literal_eval()`.
   - Extract:
     - Top 3 cast members
     - Director name
     - Genre and keyword lists
   - Clean text data and combine all features into a single column called `tags`.
3. Model Building
   - Convert tags into numerical vectors using TF-IDF Vectorizer.
   - Compute pairwise cosine similarity between all movie vectors.
   - Save model files (`movies.pkl`, `similarity.pkl`) for deployment.

## Dataset
- Source: [Kaggle - TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## Getting Started
1. Clone this repository and install dependencies:
   ```
   git clone https://github.com/GeorgeYoussefRoger/Movie-Recommender-System.git
   ```
   ```
   cd Movie-Recommender-System
   ```
   ```
   pip install -r requirements.txt
   ```
2. Run the Jupyter notebooks to generate required data and models

   The following files will be created:

   `data/clean_movies.csv` `data/tags_movies.csv`
   `models/movies.pkl` `models/similarity.pkl`

3. Run the Streamlit app
   ```
   streamlit run ui/app.py
   ```
