"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist library."""

    def __init__(self):
        """Playlist library constructor."""
        self._titles = []
        self._playlists = []

    @property
    def titles(self) -> str:
        """Returns the titles of Playlists from the Playlist library."""
        return self._titles

    def create_playlist(self, playlist_title: str):
        """Creates a Playlist in the Playlist library."""
        self._titles.append(playlist_title)
        self._playlists.append([])

    def add_videos_to_playlist(self, playlist_title: str, video_id: str):
        """Adds videos to Playlist."""
        playlist_index = -1
        count = -1
        for playlist in self._titles:
            count += 1
            if playlist.lower() == playlist_title.lower():
                playlist_index = count

        self._playlists[playlist_index].append(video_id)

    def get_videos_from_playlist(self, playlist_title: str):
        """Gets videos from Playlist."""
        playlist_index = -1
        count = -1
        for playlist in self._titles:
            count += 1
            if playlist.lower() == playlist_title.lower():
                playlist_index = count

        return self._playlists[playlist_index]

    def remove_video_from_playlist(self, playlist_title: str, video_id: str):
        """Removes video from Playlist."""
        playlist_index = -1
        count = -1
        for playlist in self._titles:
            count += 1
            if playlist.lower() == playlist_title.lower():
                playlist_index = count

        return self._playlists[playlist_index].remove(video_id)

    def clear_playlist(self, playlist_title: str):
        """Clears Playlist."""
        playlist_index = -1
        count = -1
        for playlist in self._titles:
            count += 1
            if playlist.lower() == playlist_title.lower():
                playlist_index = count

        self._playlists[playlist_index] = []

    def delete_playlist(self, playlist_title: str):
        """Deletes Playlist."""
        playlist_index = -1
        count = -1
        for playlist in self._titles:
            count += 1
            if playlist.lower() == playlist_title.lower():
                playlist_index = count

        del self._playlists[playlist_index]
        self._titles.remove(playlist_title)
