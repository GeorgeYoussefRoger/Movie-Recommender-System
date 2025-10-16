# 🎬 Movie Recommender System

A Content-Based Movie Recommendation System that suggests movies similar to a given title using the TMDB 5000 Movies Dataset from Kaggle. The system combines metadata such as genres, keywords, cast, crew, and movie descriptions to create a similarity-based recommendation engine using TF-IDF vectorization and cosine similarity.

## 🚀 Features

- Cleaned and merged TMDB movies and credits datasets
- Extracted meaningful metadata (cast, crew, genres, keywords)
- Created unified feature representation using tags
- Used TF-IDF and cosine similarity to compute movie similarity
- Interactive Streamlit web app for generating movie recommendations

## 🧠 Methodology

🧹 Data Preprocessing

- Loaded and merged tmdb_5000_movies.csv and tmdb_5000_credits.csv
- Selected key attributes: movie_id, title, overview, genres, keywords, cast, crew
- Handled missing values and exported cleaned dataset

🧩 Feature Engineering

- Parsed JSON-like columns using ast.literal_eval()
- Extracted top 3 cast members and director from crew
- Processed and cleaned text data
- Combined multiple metadata sources into a single descriptive feature column (tags)

🤖 Model Building

- Converted tags text into numerical vectors using TF-IDF Vectorizer
- Computed pairwise cosine similarity to measure movie similarity
- Serialized model components:
  - movies — stores movie metadata
  - similarity — stores cosine similarity matrix

🧮 Recommendation Logic

- Retrieve the selected movie from user input
- Compute similarity scores with all other movies
- Return top 5 most similar movies

## 📂 Project Structure

```
Movie-Recommendation-System/
├── data/
│ ├── tmdb_5000_movies.csv          # Original TMDB 5000 movies dataset
│ ├── tmdb_5000_credits.csv         # Cast and crew data corresponding to each movie
├── notebooks/
│ ├── 1_data_preprocessing.ipynb    # Data cleaning, merging and missing value handling
│ ├── 2_feature_engineering.ipynb   # Feature extraction
│ ├── 3_model_building.ipynb        # TF-IDF vectorization, similarity calculation
├── ui/
│ └── app.py                        # Streamlit app for movie recommendations
├── recommender_utils.py            # Module containing recommendation and poster functions
├── requirements.txt                # Dependencies
├── README.md                       # Project documentation
├── .gitignore
└── LICENSE
```

## 🧰 Technologies Used

- Python — pandas, scikit-learn
- Natural Language Processing — TF-IDF Vectorizer, Cosine Similarity
- Web App — Streamlit

## 📦 Installation & Usage

1️⃣ Clone the repository

```
git clone https://github.com/GeorgeYoussefRoger/Movie-Recommender-System.git
cd Movie-Recommender-System
```

2️⃣ Install dependencies

```
pip install -r requirements.txt
```

3️⃣ Generate model files

- Run the Jupyter notebooks in the notebooks/ folder sequentially to prepare cleaned data and model artifacts.
- This will generate the following files:
  `data/clean_movies.csv`
  `data/tags_movies.csv`
  `models/recommender.pkl`

4️⃣ Run the Streamlit app

```
streamlit run ui/app.py
```

## 📂 Dataset

- Source: [Kaggle - TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Contains metadata for 5000+ popular movies

## 📜 License

- This project is licensed under the MIT License.
- See the `LICENSE` file for more details.
