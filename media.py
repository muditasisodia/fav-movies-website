class Movie():
    """Class describing the behaviour of a movie
    Args:
    title (str): Title of movie
    poster_img_url (str): URL of movie poster
    trailer_youtube_url (str): URL of YouTube trailer for movie
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
