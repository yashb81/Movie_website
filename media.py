import webbrowser
class Movie():
    def __init__(self, m_t, m_s, p_i, t_y):
        self.title = m_t
        self.storyline = m_s
        self.poster_image_url = p_i
        self.trailer_youtube_url = t_y
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
