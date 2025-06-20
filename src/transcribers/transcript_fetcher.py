"""
Initially for the sake of working, I'm going to fetch the transcript using YouTubeTranscriptApi.

But Eventually the following will be implemented:
1)Use Beautiful soup to get html of a give YouTube URL
2)scrape the relevant transcript part through analysing css formats, getting all the relevant data like
time stamps and the transcript for that time stamp
3) write in a clean json file and return the json file

"""

"""
OKAY..  so youtube transcript API doesn't work anymore

It's cause AI companies were putting too much load on youtube's servers
by millions of requests, so youtube fought back and now we can't use it

Guess the user will have to manually copy paste transcripts,
which is still faster

ALSO:
Many requests can cause IP bans, so this method is generally risky

Though we can work around that using multiple proxy servers.


"""

import json
import re
import sys
from typing import List, Dict, Any

import requests
from bs4 import BeautifulSoup

def fetch_transcript_bsoup(youtube_url: str, output_json_path: str = "transcript_bsoup.json") -> List[Dict[str, Any]]:
    """
    Fetches the transcript from a YouTube video page using BeautifulSoup.
    Args:
        youtube_url (str): The URL of the YouTube video.
        output_json_path (str): Path to save the output JSON file.
    Returns:
        List[Dict[str, Any]]: List of transcript entries with 'start' and 'text'.
    """
    response = requests.get(youtube_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the transcript data in the HTML (YouTube renders it in a script tag as JSON)
    transcript_json = None
    for script in soup.find_all('script'):
        if script.string and '"transcriptRenderer"' in script.string:
            match = re.search(r'({\"transcriptRenderer.*?}}}})', script.string)
            if match:
                try:
                    transcript_json = json.loads(match.group(1))
                    break
                except Exception:
                    continue
    if not transcript_json:
        print("Transcript not found in the HTML.")
        return []

    # Parse transcript lines
    transcript_lines = []
    try:
        cues = transcript_json['transcriptRenderer']['body']['transcriptBodyRenderer']['cueGroups']
        for cue in cues:
            cue_renderer = cue['transcriptCueGroupRenderer']['cues'][0]['transcriptCueRenderer']
            start = cue_renderer['startOffsetMs']
            text = cue_renderer['cue']['simpleText']
            transcript_lines.append({
                'start': int(start) / 1000,  # convert ms to seconds
                'text': text
            })
    except Exception as e:
        print(f"Error parsing transcript: {e}")
        return []

    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(transcript_lines, f, ensure_ascii=False, indent=2)
    return transcript_lines


def fetch_transcript_youtube_transcript_api(youtube_url: str, output_json_path: str = "transcript_youtube_api.json") -> List[Dict[str, Any]]:
    """
    Fetches the transcript using youtube-transcript-api.
    Args:
        youtube_url (str): The URL of the YouTube video.
        output_json_path (str): Path to save the output JSON file.
    Returns:
        List[Dict[str, Any]]: List of transcript entries with 'start' and 'text'.
    """
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        from youtube_transcript_api.formatters import JSONFormatter
    except ImportError:
        print("youtube-transcript-api is not installed. Please install it with 'pip install youtube-transcript-api'.")
        return []

    # Extract video ID from URL
    # Support more YouTube URL formats
    video_id = None
    patterns = [
        r"(?:v=|vi=)([\w-]{11})",  # https://www.youtube.com/watch?v=VIDEO_ID
        r"youtu\.be/([\w-]{11})",  # https://youtu.be/VIDEO_ID
        r"youtube\.com/embed/([\w-]{11})",  # https://www.youtube.com/embed/VIDEO_ID
    ]
    for pat in patterns:
        match = re.search(pat, youtube_url)
        if match:
            video_id = match.group(1)
            print(f"Extracted video ID: {video_id}")
            break
    if not video_id:
        print("Invalid YouTube URL. Could not extract video ID.")
        return []

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        print("If the video has no transcript or is auto-generated in another language, try editing the languages list.")
        return []

    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(transcript, f, ensure_ascii=False, indent=2)
    return transcript


def main():
    print("YouTube Transcript Fetcher")
    youtube_url = input("Enter the YouTube video URL: ").strip()
    print("Choose method:")
    print("1. BeautifulSoup HTML scraping")
    print("2. youtube-transcript-api")
    method = input("Enter 1 or 2: ").strip()
    if method == '1':
        result = fetch_transcript_bsoup(youtube_url)
        print(f"Transcript fetched using BeautifulSoup. Saved to transcript_bsoup.json. {len(result)} lines found.")
    elif method == '2':
        result = fetch_transcript_youtube_transcript_api(youtube_url)
        print(f"Transcript fetched using youtube-transcript-api. Saved to transcript_youtube_api.json. {len(result)} lines found.")
    else:
        print("Invalid method selected.")

if __name__ == "__main__":
    main()


