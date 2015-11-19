class Movie():
    """constructor for Movie taking arguments for movie title, description,
        trailer, poster, csat, release date"""
    def __init__(self, movie_title, movie_description, movie_poster,
                movie_trailer, movie_release_date, movie_cast):
        super(Movie, self).__init__()
        self.title = movie_title
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        self.movie_description = movie_description
        self.release_date = movie_release_date
        self.cast = movie_cast
