# Import python modules
import webbrowser


# Movies class definition
class Movie():
    """Movie class defines a movie

    Attributes:
        movie_title (str): Title of the movie
        movie_storyline (str): One or two sentence summary of the movie plot
        poster_image (str): Poster of the movie (image url)
        trailer_youtube (str): Movie trailer youtube url
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Launch a browser and play youtube trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)