import webbrowser

class Movie():
    """ This class provides a way to store movie related information

        Attributes:
        
        movie_title (string): Contains title of the movie
        movie_storyline (string): Really really brief plot of the movie
        poster_image (string): URL to movie image file
        trailer_youtube(string): URL to movie trailer on youtube
        
    """
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
