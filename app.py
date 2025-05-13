import os
import pickle
import requests
import streamlit as st
import pandas as pd

# --- Download similarity.pkl from Google Drive if not present ---
simmilarity_url = 'https://drive.google.com/uc?id=1YduzIMdhDLOlKd1o1OmeAQoN3t3HURhD'

if not os.path.exists('simmilarity.pkl'):
    st.info("Downloading similarity file...")
    response = requests.get(simmilarity_url)
    with open('simmilarity.pkl', 'wb') as f:
        f.write(response.content)
    st.success("Download complete.")

# --- Load pickled files ---
simmilarity = pickle.load(open('simmilarity.pkl', 'rb'))
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# --- Movie recommender logic ---
def recommend(movie_title):
    movie_index = movies[movies["title"] == movie_title].index[0]
    distances = simmilarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]]["title"])
    return recommended_movies

# --- Streamlit UI ---
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox("Select a movie", movies["title"].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)
