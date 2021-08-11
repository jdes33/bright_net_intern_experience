"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, title):
        self._title = title
        self._videos = []  # ids of videos in playlist

    def add_video(self, video_id):
        if video_id not in self._videos:
            self._videos.append(video_id)

    def contains_video(self, video_id):
        return video_id in self._videos
    
    @property
    def title(self):
        """Returns the title of a playlist."""
        return self._title
