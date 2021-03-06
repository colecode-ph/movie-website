class Movie():
    """This class provides a way to store movie related information"""
    def __init__(self, movie_title, movie_year, movie_storyline, poster_image,
                 trailer_youtube):
        """This function initializes the class instance, and defines the
        variables which contain the movie related information"""
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
