import requests

class MovieRecommender:
    def __init__(self, movies, similarity):
        self.movies = movies
        self.similarity = similarity

    # Function to fetch movie poster from TMDB API
    def fetch_poster(self, movie_id):
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path

    # Function to recommend movies based on similarity scores
    def recommend(self, movie):
        index = self.movies[self.movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(self.similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:
            movie_id = self.movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(self.fetch_poster(movie_id))
            recommended_movie_names.append(self.movies.iloc[i[0]].title)
        return recommended_movie_names, recommended_movie_posters