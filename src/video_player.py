"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playlist_library = Playlist()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")

        videos_list = self._video_library.get_all_videos()
        videos_id_list = []

        for video in videos_list:
            videos_id_list.append(video.video_id)

        for sorted_video_id in sorted(videos_id_list):
            sorted_video = self._video_library.get_video(sorted_video_id)
            sorted_video_tags = sorted_video.tags
            sorted_video_tags_concatenated = ""
            count = 0

            for tag in sorted_video_tags:
                count += 1
                sorted_video_tags_concatenated += tag
                if count != len(sorted_video_tags):
                    sorted_video_tags_concatenated += " "

            if self._video_library.get_video(sorted_video_id).flagged:
                print(" " + sorted_video.title + " (" + sorted_video.video_id + ")" + " [" + sorted_video_tags_concatenated + "] - FLAGGED (reason: " + self._video_library.get_video(sorted_video_id).reason + ")")
            else:
                print(" " + sorted_video.title + " (" + sorted_video.video_id + ")" + " [" + sorted_video_tags_concatenated + "]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        videos_list = self._video_library.get_all_videos()

        video_id_found = False
        for video in videos_list:
            if video.video_id == video_id:
                video_id_found = True

        if video_id_found:
            if not self._video_library.get_video(video_id).flagged:
                for video in videos_list:
                    if video.playing:
                        video.switch_playing_state()
                        print("Stopping video: " + video.title)

                    if video.paused:
                        video.switch_paused_state()
                        print("Stopping video: " + video.title)

                print("Playing video: " + self._video_library.get_video(video_id).title)
                self._video_library.get_video(video_id).switch_playing_state()

            else:
                print("Cannot play video: Video is currently flagged (reason: " + self._video_library.get_video(video_id).reason + ")")

        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        videos_list = self._video_library.get_all_videos()

        video_was_playing = False
        for video in videos_list:
            if video.playing:
                video.switch_playing_state()
                video_was_playing = True
                print("Stopping video: " + video.title)

            if video.paused:
                video.switch_paused_state()
                video_was_playing = True
                print("Stopping video: " + video.title)

        if not video_was_playing:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        videos_list = self._video_library.get_all_videos()

        video_list_unflagged = []
        for video in videos_list:
            if not video.flagged:
                video_list_unflagged.append(video)

        if len(video_list_unflagged) == 0:
            print("No videos available")

        else:
            for video in video_list_unflagged:
                if video.playing:
                    video.switch_playing_state()
                    print("Stopping video: " + video.title)

            random_video = random.choice(video_list_unflagged)
            print("Playing video: " + random_video.title)
            random_video.switch_playing_state()

    def pause_video(self):
        """Pauses the current video."""

        videos_list = self._video_library.get_all_videos()

        video_was_playing = False
        for video in videos_list:
            if video.paused:
                video_was_playing = True
                print("Video already paused: " + video.title)

            if video.playing:
                video.switch_playing_state()
                video.switch_paused_state()
                video_was_playing = True
                print("Pausing video: " + video.title)

        if not video_was_playing:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        videos_list = self._video_library.get_all_videos()

        video_was_paused = False
        for video in videos_list:
            if video.playing:
                video_was_paused = True
                print("Cannot continue video: Video is not paused")

            if video.paused:
                video.switch_paused_state()
                video.switch_playing_state()
                video_was_paused = True
                print("Continuing video: " + video.title)

        if not video_was_paused:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        videos_list = self._video_library.get_all_videos()

        video_was_playing_or_paused = False
        for video in videos_list:
            video_tags = video.tags
            video_tags_concatenated = ""
            count = 0
            for tag in video_tags:
                count += 1
                video_tags_concatenated += tag
                if count != len(video_tags):
                    video_tags_concatenated += " "

            if video.playing:
                video_was_playing_or_paused = True
                print("Currently playing: " + video.title + " (" + video.video_id + ")" + " [" + video_tags_concatenated + "]")

            if video.paused:
                video_was_playing_or_paused = True
                print("Currently playing: " + video.title + " (" + video.video_id + ")" + " [" + video_tags_concatenated + "] - PAUSED")

        if not video_was_playing_or_paused:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        can_create_playlist = True
        for playlist_title in self._playlist_library.titles:
            if playlist_title.lower() == playlist_name.lower():
                can_create_playlist = False
                print("Cannot create playlist: A playlist with the same name already exists")

        if can_create_playlist:
            self._playlist_library.create_playlist(playlist_name)
            print("Successfully created new playlist: " + playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        playlist_found = False
        for playlist_title in self._playlist_library.titles:
            if playlist_title.lower() == playlist_name.lower():
                playlist_found = True

        video_found = False
        videos_list = self._video_library.get_all_videos()
        for video in videos_list:
            if video.video_id == video_id:
                video_found = True

        video_in_playlist = False
        if playlist_found:
            for video in self._playlist_library.get_videos_from_playlist(playlist_name):
                if video == video_id:
                    video_in_playlist = True

        if not playlist_found:
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")

        elif not video_found:
            print("Cannot add video to " + playlist_name + ": Video does not exist")

        elif video_in_playlist and not self._video_library.get_video(video_id).flagged:
            print("Cannot add video to " + playlist_name + ": Video already added")

        else:
            if not self._video_library.get_video(video_id).flagged:
                self._playlist_library.add_videos_to_playlist(playlist_name, video_id)
                print("Added video to " + playlist_name + ": " + self._video_library.get_video(video_id).title)

            else:
                print("Cannot add video to " + playlist_name + ": Video is currently flagged (reason: " + self._video_library.get_video(video_id).reason + ")")

    def show_all_playlists(self):
        """Display all playlists."""

        if len(self._playlist_library.titles) == 0:
            print("No playlists exist yet")

        else:
            print("Showing all playlists:")

            for playlist_title in sorted(self._playlist_library.titles):
                print(" " + playlist_title)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        playlist_found = False
        for playlist_title in self._playlist_library.titles:
            if playlist_title.lower() == playlist_name.lower():
                playlist_found = True

        if not playlist_found:
            print("Cannot show playlist " + playlist_name + ": Playlist does not exist")

        elif len(self._playlist_library.get_videos_from_playlist(playlist_name)) == 0:
            print("Showing playlist: " + playlist_name)
            print(" No videos here yet")

        else:
            print("Showing playlist: " + playlist_name)

            for video_title in self._playlist_library.get_videos_from_playlist(playlist_name):
                video = self._video_library.get_video(video_title)
                video_tags = video.tags
                video_tags_concatenated = ""
                count = 0
                for tag in video_tags:
                    count += 1
                    video_tags_concatenated += tag
                    if count != len(video_tags):
                        video_tags_concatenated += " "

                if video.flagged:
                    print(" " + video.title + " (" + video.video_id + ")" + " [" + video_tags_concatenated + "] - FLAGGED (reason: " + video.reason + ")")

                else:
                    print(" " + video.title + " (" + video.video_id + ")" + " [" + video_tags_concatenated + "]")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        playlist_found = False
        for playlist_title in self._playlist_library.titles:
            if playlist_title.lower() == playlist_name.lower():
                playlist_found = True

        video_found = False
        videos_list = self._video_library.get_all_videos()
        for video in videos_list:
            if video.video_id == video_id:
                video_found = True

        video_in_playlist = False
        if playlist_found:
            for video in self._playlist_library.get_videos_from_playlist(playlist_name):
                if video == video_id:
                    video_in_playlist = True

        if not playlist_found:
            print("Cannot remove video from " + playlist_name + ": Playlist does not exist")

        elif not video_found:
            print("Cannot remove video from " + playlist_name + ": Video does not exist")

        elif not video_in_playlist:
            print("Cannot remove video from " + playlist_name + ": Video is not in playlist")

        else:
            self._playlist_library.remove_video_from_playlist(playlist_name, video_id)
            print("Removed video from " + playlist_name + ": " + self._video_library.get_video(video_id).title)

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        playlist_found = False
        for playlist_title in self._playlist_library.titles:
            if playlist_title.lower() == playlist_name.lower():
                playlist_found = True

        if not playlist_found:
            print("Cannot clear playlist " + playlist_name + ": Playlist does not exist")

        else:
            self._playlist_library.clear_playlist(playlist_name)
            print("Successfully removed all videos from " + playlist_name)

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        playlist_found = False
        for playlist_title in self._playlist_library.titles:
            if playlist_title.lower() == playlist_name.lower():
                playlist_found = True

        if not playlist_found:
            print("Cannot delete playlist " + playlist_name + ": Playlist does not exist")

        else:
            self._playlist_library.delete_playlist(playlist_name)
            print("Deleted playlist: " + playlist_name)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """

        videos_list = self._video_library.get_all_videos()
        videos_id_list = []
        sorted_videos_list =[]
        counter = 0
        show_once = False

        video_list_unflagged = []
        for video in videos_list:
            if not video.flagged:
                video_list_unflagged.append(video)

        for video in video_list_unflagged:
            videos_id_list.append(video.video_id)

        for sorted_video_id in sorted(videos_id_list):
            sorted_videos_list.append(self._video_library.get_video(sorted_video_id))

        for video in sorted_videos_list:
            video_tags = video.tags
            video_tags_concatenated = ""
            count = 0
            for tag in video_tags:
                count += 1
                video_tags_concatenated += tag
                if count != len(video_tags):
                    video_tags_concatenated += " "

            if search_term.lower() in video.title.lower():
                counter += 1
                if not show_once:
                    print("Here are the results for " + search_term + ":")
                    show_once = True

                print(" " + str(counter) + ") " + video.title + " (" + video.video_id + ")" + " [" + video_tags_concatenated + "]")

        if counter > 0:
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")

            number = input()
            if number.isnumeric():
                number = int(number)
            else:
                number = 0

        if counter > 0:
            for i in range(counter):
                if number == (i + 1):
                    self.play_video(sorted_videos_list[number - 1].video_id)
        else:
            print("No search results for " + search_term)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """

        videos_list = self._video_library.get_all_videos()
        videos_id_list = []
        sorted_videos_list = []
        counter = 0
        show_once = False

        video_list_unflagged = []
        for video in videos_list:
            if not video.flagged:
                video_list_unflagged.append(video)

        for video in video_list_unflagged:
            videos_id_list.append(video.video_id)

        for sorted_video_id in sorted(videos_id_list):
            sorted_videos_list.append(self._video_library.get_video(sorted_video_id))

        for video in sorted_videos_list:
            video_tags = video.tags
            video_tags_concatenated = ""
            count = 0
            for tag in video_tags:
                count += 1
                video_tags_concatenated += tag
                if count != len(video_tags):
                    video_tags_concatenated += " "

            if (video_tag.lower() in video_tags_concatenated.lower()) and ("#" in video_tag):
                counter += 1
                if not show_once:
                    print("Here are the results for " + video_tag + ":")
                    show_once = True

                print(" " + str(
                    counter) + ") " + video.title + " (" + video.video_id + ")" + " [" + video_tags_concatenated + "]")

        if counter > 0:
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")

            number = input()
            if number.isnumeric():
                number = int(number)
            else:
                number = 0

        if counter > 0:
            for i in range(counter):
                if number == (i + 1):
                    self.play_video(sorted_videos_list[number - 1].video_id)
        else:
            print("No search results for " + video_tag)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """

        reason = ""
        if flag_reason == "":
            reason = "Not supplied"
        else:
            reason = flag_reason

        video_found = False
        videos_list = self._video_library.get_all_videos()
        for video in videos_list:
            if video.video_id == video_id:
                video_found = True

        if not video_found:
            print("Cannot flag video: Video does not exist")

        elif self._video_library.get_video(video_id).flagged:
            print("Cannot flag video: Video is already flagged")

        else:
            if self._video_library.get_video(video_id).playing or self._video_library.get_video(video_id).paused:
                self.stop_video()

            self._video_library.get_video(video_id).switch_flagged_state(reason)
            print("Successfully flagged video: " + self._video_library.get_video(video_id).title + " (reason: " + reason + ")")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """

        video_found = False
        videos_list = self._video_library.get_all_videos()
        for video in videos_list:
            if video.video_id == video_id:
                video_found = True

        if not video_found:
            print("Cannot remove flag from video: Video does not exist")

        elif not self._video_library.get_video(video_id).flagged:
            print("Cannot remove flag from video: Video is not flagged")

        else:
            self._video_library.get_video(video_id).switch_flagged_state("")
            print("Successfully removed flag from video: " + self._video_library.get_video(video_id).title)
