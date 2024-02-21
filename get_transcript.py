from youtube_transcript_api import YouTubeTranscriptApi
from pytube import Playlist, YouTube
import json
import re

def sanitize_filename(filename):
    """Sanitize the filename to avoid issues with file systems."""
    return re.sub(r'[\\/:*<>|]', "", filename)

def format_filename(title):
    """Format filename to include only the part of the title before a dash."""
    if '-' in title:
        # Split the title at the first dash and strip trailing spaces from the first part
        formatted_title = title.split('-', 1)[0].strip()
    else:
        formatted_title = title
    return sanitize_filename(formatted_title)

def fetch_transcripts(playlist_url):
    playlist = Playlist(playlist_url)
    all_transcripts = []

    for video_url in playlist.video_urls:
        yt = YouTube(video_url)  # Use pytube's YouTube object to access video details
        video_title = sanitize_filename(yt.title)  # Get the sanitized video title
        video_id = yt.video_id  # Get the video ID

        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            all_transcripts.append((video_title, transcript))
            print(f"Transcript fetched for video: {video_title}")
        except Exception as e:
            print(f"Could not fetch transcript for video {video_title} ({video_id}): {e}")

    return all_transcripts