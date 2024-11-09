import subprocess
import json
from youtube_transcript_api import YouTubeTranscriptApi
from prompts import example
import requests
from  openai_interactions import return_clips


def create_chapters(video_id):
    # transcript_dict = YouTubeTranscriptApi.get_transcript('aircAruvnKk') 
    # combined_text = ' '.join([f"{entry['text']} [{entry['start']}]" for entry in transcript_dict])
    print(return_clips(example))
    
    

def get_youtube_chapters(video_id): #if there  are  preexisting chapters like 3B1B
    try:
        # Run the JavaScript file with Node.js
        result = subprocess.run(
            ["node", "get_youtube_chapters.js", video_id],
            capture_output=True,
            text=True,
            check=True
        )

        # Parse the JSON output
        chapters = json.loads(result.stdout)
        return chapters

    except subprocess.CalledProcessError as e:
        print("Error fetching chapters:", e.stderr)
        return None

# Example usage
# chapters = get_youtube_chapters("aircAruvnKk")
# print(chapters)

create_chapters('aircAruvnKk')
