import streamlit as st
import joblib
from recommender_utils import recommend

# Load model
model = joblib.load("models/recommender.pkl")
movies = model['movies']
similarity = model['similarity']

st.header('🎬 Movie Recommender System')
selected_movie = st.selectbox("Type or select a movie from the dropdown", movies['title'].values)

# Recommendation
if st.button('Show Recommendation'):
    title, poster = recommend(movies, similarity, selected_movie)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.image(poster[i], use_container_width=True)
            st.caption(title[i])