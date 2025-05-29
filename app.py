import streamlit as st
import pandas as pd
import pickle
import os
import requests

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)

# Google Drive file IDs for your pickle files
MOVIES_ID = "1NdM9oOzUxihNngjGaQsHT_42wUasqBAB"
SIMILARITY_ID = "1AeWcfVrj8f9EcK1Xt79pq_mZLILh_kzZ"

MOVIES_FILE = "movies.pkl"
SIMILARITY_FILE = "similarity.pkl"

# Download movies.pkl if not present
if not os.path.exists(MOVIES_FILE):
    with st.spinner("Downloading movies.pkl..."):
        download_file_from_google_drive(MOVIES_ID, MOVIES_FILE)

# Download similarity.pkl if not present
if not os.path.exists(SIMILARITY_FILE):
    with st.spinner("Downloading similarity.pkl..."):
        download_file_from_google_drive(SIMILARITY_ID, SIMILARITY_FILE)

# Load pickle files
movies = pickle.load(open(MOVIES_FILE, "rb"))
similarity = pickle.load(open(SIMILARITY_FILE, "rb"))

# Streamlit UI setup
st.set_page_config(page_title="Movie Recommender", layout="centered")

st.title("🎬 Movie Recommendation System")
st.write("Enter a movie you like, and we'll recommend similar ones!")

movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie", movie_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)
    recommended_movies = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movies

if st.button("Recommend"):
    with st.spinner("Finding recommendations..."):
        recommendations = recommend(selected_movie)
        st.success("Here are 5 movies you might enjoy:")
        for i, title in enumerate(recommendations, start=1):
            st.write(f"{i}. {title}")
