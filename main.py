import streamlit as st
import pickle

# Load data
movies = pickle.load(open('movies_with_posters_final.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown movie titles
movies_list = movies['title'].values

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a movie",
    movies_list
)


# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_sorted = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_sorted:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(movies.iloc[i[0]].poster)

    return recommended_movies, recommended_movies_posters


# Button click
if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

    cols = st.columns(5)

    for idx in range(5):
        with cols[idx]:
            st.text(recommended_movie_names[idx])

            if recommended_movie_posters[idx]:
                st.image(
                    recommended_movie_posters[idx],
                    width='stretch'
                )
            else:
                st.image(
                    "https://via.placeholder.com/300x450?text=No+Poster",
                    width='stretch'
                )