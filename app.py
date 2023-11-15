import streamlit as st
import pickle

movies = pickle.load(open("movies_list.pkl", "rb"))
similarity= pickle.load(open("similarity.pkl", "rb"))

movies_list = movies['title'].values
st.header("Movie Recomender System")
select_values = st.selectbox("Select movie from dropdown", movies_list)



def recomend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])) ,reverse=True,key= lambda vector: vector[1] )
    recomend_movie = []
    for i in distance[0:5]:
        recomend_movie.append(movies.iloc[i[0]].title)
    return recomend_movie



if st.button("Show Recomend"):
    movie_name = recomend(select_values)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])

