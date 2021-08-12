"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video_id = ""
        self._paused = False
        self._playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Shows all videos."""
        print("Here's a list of all available videos:")
        videos = sorted(self._video_library.get_all_videos(), key=lambda v: v.title)
        for video in videos:
            print(f"\t{video}")  ## utilises str dunder method of video object
        
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video:
            if video.flag_reason:
                print(f"Cannot play video: Video is currently flagged (reason: {video.flag_reason})")
            else:
                self.stop_current_video()
                self._current_video_id = video.video_id
                print(f"Playing video: {video.title}")
        else :
            print("Cannot play video: Video does not exist")       

    def stop_video(self):
        """Stops the current video."""
        if self._current_video_id:
            self.stop_current_video()
        else:
            print("Cannot stop video: No video is currently playing")
            
    def stop_current_video(self):
        """Helper function for self.stop_video(), created to avoid repetition of code in other areas"""
        if self._current_video_id:
            video_to_stop = self._video_library.get_video(self._current_video_id)
            print(f"Stopping video: {video_to_stop.title}")
            self._current_video_id = ""
            self._paused = False
            
    def play_random_video(self):
        """Plays a random video from the video library."""
        all_videos = self._video_library.get_all_videos()
        all_videos = list(filter(lambda v: not v.flag_reason, all_videos))  # only get videos that aren't flagged
        if all_videos:
            self.stop_current_video()
            video = all_videos[random.randint(0, len(all_videos) - 1)]
            self._current_video_id = video.video_id
            print(f"Playing video: {video.title}")
        else:
            print("No videos available")

    def pause_video(self):
        """Pauses the current video."""
        if self._paused:
            video = self._video_library.get_video(self._current_video_id)
            print(f"Video already paused: {video.title}")
        elif self._current_video_id:
            self._paused = True
            video = self._video_library.get_video(self._current_video_id)
            print(f"Pausing video: {video.title}")          
        else:
            print("Cannot pause video: No video is currently playing")
        
    def continue_video(self):
        """Resumes playing the current video."""
        if self._paused:
           self._paused = False
           video = self._video_library.get_video(self._current_video_id)
           print(f"Continuing video: {video.title}")
        elif self._current_video_id:
            print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        if self._current_video_id:
            video = self._video_library.get_video(self._current_video_id)
            paused_status = " - PAUSED" if self._paused else ""
            print(f"Currently playing: {video}{paused_status}")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        #lower_case_names = [playlist.title.lower() for playlist in self._playlists]
        lower_case_names = set(self._playlists.keys())
        if " " not in set(playlist_name):
            if playlist_name.lower() in lower_case_names:
                print("Cannot create playlist: A playlist with the same name already exists")
            else:
                # the _playlist dictionary uses the lower case version of the playlist name...
                # ... as the key, however the Playlist object stores the original name
                self._playlists[playlist_name.lower()] = Playlist(playlist_name)
                print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.lower() in set(self._playlists.keys()):
            video = self._video_library.get_video(video_id)
            if video:
                if not video.flag_reason:
                    playlist = self._playlists[playlist_name.lower()]
                    if playlist.contains_video(video_id):
                        print(f"Cannot add video to {playlist_name}: Video already added")
                    else:
                        playlist.add_video(video_id)
                        print(f"Added video to {playlist_name}: {video.title}")
                else:
                    print(f"Cannot add video to {playlist_name}: Video is currently flagged (reason: {video.flag_reason})")
            else:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
        else:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""
        if self._playlists:
            print("Showing all playlists:")
            sorted_playlists = sorted(list(self._playlists.keys()))
            for name in sorted_playlists:
                print(f"\t{self._playlists[name].title}")
                
        else:
            print("No playlists exist yet")

        
    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
            print(f"Showing playlist: {playlist_name}")
            playlist = self._playlists[playlist_name.lower()]
            if not playlist.empty():
                for video_id in playlist.videos:
                    video = self._video_library.get_video(video_id)
                    print(f"\t{video}")
            else:
                print("\tNo videos here yet")
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
            
    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name.lower() in self._playlists:
            playlist = self._playlists[playlist_name.lower()]
            if video_id in playlist._videos:
                video_title = self._video_library.get_video(video_id).title
                playlist.remove(video_id)
                print(f"Removed video from {playlist_name}: {video_title}")
            else:
                if self._video_library.get_video(video_id):
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
                else:
                    print(f"Cannot remove video from {playlist_name}: Video does not exist")
        else:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        
    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
            self._playlists[playlist_name.lower()].clear()
            print(f"Successfully removed all videos from {playlist_name}")
            
        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
            self._playlists.pop(playlist_name.lower())
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
            
    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        videos = self._video_library.get_all_videos()
        filtered_videos = list(filter(lambda video: search_term.lower() in video.title.lower(), videos))
        filtered_videos = list(filter(lambda video: not video.flag_reason, filtered_videos))
        filtered_videos.sort(key=lambda v: v.title)
        if filtered_videos:
            print(f"Here are the results for {search_term}:")
            for i in range(len(filtered_videos)):
                print(f"\t{i+1}) {filtered_videos[i]}")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")

            try:
                answer = int(input())
                if answer > 0 and answer <= len(filtered_videos):
                    self.play_video(filtered_videos[answer - 1].video_id)
                else:
                    raise ValueError
            except ValueError:
                pass  # didn't select valid video index

        else:
            print(f"No search results for {search_term}")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        videos = self._video_library.get_all_videos()
        filtered_videos = list(filter(lambda video: video_tag.lower() in video.tags, videos))
        filtered_videos = list(filter(lambda video: not video.flag_reason, filtered_videos))
        filtered_videos.sort(key=lambda v: v.title)
        if filtered_videos:
            print(f"Here are the results for {video_tag}:")
            for i in range(len(filtered_videos)):
                print(f"\t{i+1}) {filtered_videos[i]}")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")

            try:
                answer = int(input())
                if answer > 0 and answer <= len(filtered_videos):
                    self.play_video(filtered_videos[answer - 1].video_id)
                else:
                    raise ValueError
            except ValueError:
                pass  # didn't select valid video index

        else:
            print(f"No search results for {video_tag}")
    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        video = self._video_library.get_video(video_id)
        if video:
            if not video.flag_reason:
                
                if flag_reason:
                    video.flag_reason = flag_reason
                else:
                    video.flag_reason = "Not supplied"
                    
                if video_id == self._current_video_id:
                    self.stop_video()
                
                print(f"Successfully flagged video: {video.title} (reason: {video.flag_reason})")
            else:
                print("Cannot flag video: Video is already flagged")
        else:
            print("Cannot flag video: Video does not exist")
            
    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        video = self._video_library.get_video(video_id)
        if video:
            if video.flag_reason:
                video.flag_reason = ""
                print(f"Successfully removed flag from video: {video.title}")
            else:
                print("Cannot remove flag from video: Video is not flagged")
        else:
            print("Cannot remove flag from video: Video does not exist")
