#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import pickle

# Load saved pickle files
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set page config
st.set_page_config(page_title="Movie Recommender", layout="centered")

# App title
st.title("🎬 Movie Recommendation System")
st.write("Enter a movie you like, and we'll recommend similar ones!")

# Dropdown for movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie", movie_list)

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)
    recommended_movies = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movies

# Button to show recommendations
if st.button("Recommend"):
    with st.spinner("Finding recommendations..."):
        recommendations = recommend(selected_movie)
        st.success("Here are 5 movies you might enjoy:")
        for i, title in enumerate(recommendations, start=1):
            st.write(f"{i}. {title}")

