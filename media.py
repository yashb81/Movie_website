import webbrowser


class Movie():
    # This class contains 2 methods
    def __init__(self, m_t, m_s, p_i, t_y):
        # This method sets the values of the variables
        # title, storyline, poster_image_url and trailer_youtube_url
        self.title = m_t
        self.storyline = m_s
        self.poster_image_url = p_i
        self.trailer_youtube_url = t_y

    def show_trailer(self):
        # this method opens up the link of the trailer
        # provided in as the arguements.
        webbrowser.open(self.trailer_youtube_url)
