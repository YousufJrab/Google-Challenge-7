"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id
        self._playing = False
        self._paused = False
        self._flagged = False
        self._reason = ""

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

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
    def playing(self) -> bool:
        """Returns a boolean if video is playing."""
        return self._playing

    @property
    def paused(self) -> bool:
        """Returns a boolean if video is playing."""
        return self._paused

    @property
    def flagged(self) -> bool:
        """Returns a boolean if video is flagged."""
        return self._flagged

    @property
    def reason(self) -> str:
        """Returns reason when flagged."""
        return self._reason

    def switch_playing_state(self):
        """Switches video playing state between playing and stopped."""
        if self._playing:
            self._playing = False
        else:
            self._playing = True

    def switch_paused_state(self):
        """Switches video paused state between paused and playing."""
        if self._paused:
            self._paused = False
        else:
            self._paused = True

    def switch_flagged_state(self, reason: str):
        """Switches video flagged state between flagged and not flagged."""
        if self._flagged:
            self._flagged = False
        else:
            self._flagged = True

        self._reason = reason
