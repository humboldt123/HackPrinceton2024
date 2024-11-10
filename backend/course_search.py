from googleapiclient.discovery import build
import re


## Youtube Search
API_KEY = ''
youtube = build('youtube', 'v3', developerKey=API_KEY)


# Returns list of videos in order, each video represented by a dict [{video_id: string, title: string, description: string}]
def search_courses(youtube,topicString, results = 1,type="playlist"):
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
def get_playlist(youtube,playlistId):
    request_playlist = youtube.playlistItems().list(
        playlistId=playlistId,
        part='snippet',
        maxResults = 100,
    )

    response_playlist = request_playlist.execute()

    res2 = []
    for item in response_playlist['items']:
        video_id = (item['snippet']['resourceId']['videoId'])
        title = item['snippet']['title']
        description = item['snippet']['description']
        res2.append({"video_id": video_id, "title": title, "description": description})

    return res2