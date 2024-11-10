import subprocess
import json
from youtube_transcript_api import YouTubeTranscriptApi
from prompts import example
import requests
from  openai_interactions import return_clips, return_article


def create_chapter_objects(video_id):
    transcript_dict = get_transcript(video_id)
    chapters = create_chapters(transcript_dict)
    # chapters = return_clips(example)
    res = []
    for c in chapters[0]:
        chapter_dict = (c).copy()
        texts_in_interval = [entry['text'] for entry in transcript_dict if chapter_dict["start_time"] <= entry['start'] <= chapter_dict["end_time"]]
        chapter_dict["transcripts"] = texts_in_interval
        chapter_dict["video_id"] = video_id
        res.append(chapter_dict)
    return res
    

def get_transcript(video_id):
    transcript_dict = YouTubeTranscriptApi.get_transcript(video_id) 
    return transcript_dict

    # test = [
    #     {
    #         'text': 'Hey there',
    #         'start': 7.58,
    #         'duration': 6.13
    #     },
    #     {
    #         'text': 'how are you',
    #         'start': 14.08,
    #         'duration': 7.58
    #     },
    #     # ...
    # ]
    # return test

# Calls OPENAI
def create_chapters(transcript_dict):
    combined_text = ' '.join([f"{entry['text']} [{entry['start']}]" for entry in transcript_dict])
    return return_clips(combined_text)


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
    
def gen_article(transcript_dict, title, description, start, end):
    texts_in_interval = [entry['text'] for entry in transcript_dict if start <= entry['start'] <= end]
    joined_text = " ".join(texts_in_interval)
    res = return_article(title,description,joined_text)
    return res

    
    



# # Example usage
# # chapters = get_youtube_chapters("aircAruvnKk")
# # print(chapters)

# res = return_clips(example)
# print(res)
# print("-" * 100)
# first_chapter = res[0][0]
# title = first_chapter["title"]
# description = first_chapter['description']
# start = first_chapter['start_time']
# end = first_chapter['end_time']

# gen_article({},title,description,start,end)
