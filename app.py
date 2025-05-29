import streamlit as st
import pandas as pd
import pickle
import os
import requests

# Google Drive direct download links with file IDs extracted from your URLs
MOVIES_URL = "https://drive.google.com/uc?export=download&id=1NdM9oOzUxihNngjGaQsHT_42wUasqBAB"
SIMILARITY_URL = "https://drive.google.com/uc?export=download&id=1AeWcfVrj8f9EcK1Xt79pq_mZLILh_kzZ"

# Filenames to save locally
MOVIES_FILE = "movies.pkl"
SIMILARITY_FILE = "similarity.pkl"

def download_file(url, filename):
    if not os.path.exists(filename):
        with st.spinner(f"Downloading {filename}..."):
            response = requests.get(url)
            if response.status_code == 200:
                with open(filename, "wb") as f:
                    f.write(response.content)
            else:
                st.error(f"Failed to download {filename}!")
                st.stop()

# Download files if not present
download_file(MOVIES_URL, MOVIES_FILE)
download_file(SIMILARITY_URL, SIMILARITY_FILE)

# Load saved pickle files
movies = pickle.load(open(MOVIES_FILE, 'rb'))
similarity = pickle.load(open(SIMILARITY_FILE, 'rb'))

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
