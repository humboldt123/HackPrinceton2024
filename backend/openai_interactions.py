from enum import Enum
from typing import List
from pydantic import BaseModel
from openai import OpenAI
import json
import os
from prompts import transcript_to_clip

class Table(str, Enum):
    clips = "clips"

class Column(str, Enum):
    title = "title"
    description = "description"
    start_time = "start time"
    end_time = "end time"

class VideoClip(BaseModel):
    title: str
    description: str
    start_time: int  # in seconds
    end_time: int  # in seconds

class VideoDecomposition(BaseModel):
    video_transcript: str
    clip_duration: int = 180

def return_clips(transcript: str) -> List[VideoClip]:
    client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY')
    )
    
    if not client.api_key:
        raise ValueError("No API key found. Set the OPENAI_API_KEY environment variable.")

    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that processes video transcripts into structured clips."
            },
            {
                "role": "user",
                "content": transcript_to_clip + "\t" + transcript
            }
        ],
        functions=[{
            "name": "process_clips",
            "description": "Process video transcript into clips",
            "parameters": {
                "type": "object",
                "properties": {
                    "clips": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "description": {"type": "string"},
                                "start_time": {"type": "integer"},
                                "end_time": {"type": "integer"}
                            },
                            "required": ["title", "description", "start_time", "end_time"]
                        }
                    }
                },
                "required": ["clips"]
            }
        }],
        function_call={"name": "process_clips"},
        temperature=0.7
    )

    # Extract the function call response
    function_response = response.choices[0].message.function_call
    # Parse the JSON string arguments into a Python dictionary
    clips_dict = json.loads(function_response.arguments)
    # Convert each clip dictionary into a VideoClip object
    clips = [clips_dict["clips"]]
    
    return clips

# Example usage
if __name__ == "__main__":
    sample_transcript = "Your transcript text here"
    clips = return_clips(sample_transcript)
    for clip in clips:
        print(f"Title: {clip.title}")
        print(f"Description: {clip.description}")
        print(f"Time: {clip.start_time}s - {clip.end_time}s\n")