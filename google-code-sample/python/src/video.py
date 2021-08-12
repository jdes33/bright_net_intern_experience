"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

        # If the video is flagged this will contain the reason for it being flagged.
        # The empty string indicates the video is not flagged.
        self._flag_reason = ""

    def __str__(self):
        """Returns a string that neatly presents video details"""
        formatted_tags = " ".join(self._tags)
        description = f"{self._title} ({self._video_id}) [{formatted_tags}]"
        if self._flag_reason:
            description += f" - FLAGGED (reason: {self._flag_reason})"
        return description

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags

    @property
    def flag_reason(self) -> str:
        """Returns the flag reason of a video (empty string indicates it's not flagged)."""
        return self._flag_reason
    
    @flag_reason.setter
    def flag_reason(self, value):
        self._flag_reason = value
