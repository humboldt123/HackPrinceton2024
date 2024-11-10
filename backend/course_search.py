from googleapiclient.discovery import build
import re
import os


# Get the value of google api key


# Returns list of videos in order, each video represented by a dict [{video_id: string, title: string, description: string}]
def search_courses(topicString, results = 3,type="playlist"):
    API_KEY = os.environ.get('GOOGLE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    search_string = topicString + " Course"
    request = youtube.search().list(
        q=search_string,  # Search term
        part='snippet',  # Include snippet (title, description, etc.)
        maxResults=results,  # Maximum number of results
        type=type,  # Only search for videos (exclude playlists and channels)
    )

    response = request.execute()

    res = []

    for item in response['items']:
        title = item['snippet']['title']
        description = item['snippet']['description']
        channelTitle = item['snippet']['channelTitle']
        playlist_id = item['id']['playlistId']
        playlist_url = f'https://www.youtube.com/playlist?list={playlist_id}'
        res.append({"id": playlist_id, "title": title, "description": description, "channelTitle": channelTitle})
    
    return res

# Returns list of videos in order, each video represented by a dict [{video_id: string, title: string, description: string}]
def get_playlist(playlistId):
    API_KEY = os.environ.get('GOOGLE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    request_playlist = youtube.playlistItems().list(
        playlistId=playlistId,
        part='snippet',
        maxResults = 10,
    )

    response_playlist = request_playlist.execute()

    res2 = []
    for item in response_playlist['items']:
        video_id = (item['snippet']['resourceId']['videoId'])
        title = item['snippet']['title']
        description = item['snippet']['description']
        res2.append({"video_id": video_id, "title": title, "description": description})

    return res2

## Video Chapters, returns list of [{timestamp:string, title: string}]
def get_chapters(video_id):
    request_for_chapters = youtube.videos().list(
        id=video_id,  # Search term
        part='snippet',  # Include snippet (title, description, etc.)
    )

    response_for_chapters = request_for_chapters.execute()

    res = []

    for video in response_for_chapters['items']:
        description = video['snippet']['description']

        # Find chapters (timestamps in description)
        chapters = re.findall(r'(\d{2}:\d{2}) - (.+)', description)

        # Print out the chapters
        for timestamp, title in chapters:
            res.append((timestamp,title))
    
    return res


