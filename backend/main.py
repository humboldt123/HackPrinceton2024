## THIS IS THE FLASK SERVER
from flask import Flask, request, jsonify
from course_search import search_courses, get_playlist
from course_creator import get_youtube_chapters,get_transcript,create_chapter_objects,gen_article
from openai_interactions import return_article

# Create an instance of the Flask class
app = Flask(__name__)


# returns three options for courses, given a search term
# Params: "query": a string for the search query
# Returns: json object 
@app.route('/api/getoptions',methods=["GET"])
def get_data():
    query = request.args.get('query')
    data = search_courses(query)
    # Return the data as JSON using jsonify
    return jsonify(data)


# returns list of all clips, given a playlist id
# Params: "playlistid": a string for playlist id
# Returns: json object, array of clips [{title:string, description:string, transcripts: string[], start_time: int, end_time: int, video_id: string}]
# returns list in order. Params start_time and end_time are the start and end times in the video
@app.route('/api/getvideos',methods=['GET'])
def get_data2():
    playlist_id = request.args.get('playlistid')
    videos = get_playlist(playlist_id)
    res = []
    for v in videos:
        video_id = v["video_id"]
        data = create_chapter_objects(video_id)
        print(data)
        for d in data:
            res.append(d)
    return jsonify(res)

# returns a article text in markdown for a clip, given the title, description, and transcript
# Params: "title": string for title, "description": string for description, "transcript": string for transcript
# Returns: a string, the article text, in markdown
@app.route('/api/getarticle',methods=['GET'])
def get_data3():
    title = request.args.get('title')
    description = request.args.get('description')
    transcript = request.args.get('transcript')
    print(title,description,transcript)
    data = return_article(title,description,transcript)
    return data



# Start the server when this file is run directly
if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)