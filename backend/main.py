## THIS IS THE FLASK SERVER
from flask import Flask, request, jsonify
from course_search import search_courses, get_playlist
from course_creator import get_youtube_chapters

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def home():
    return 'Hello, World'

# returns three options for courses, given a search term
# Params: "query": a string for the search query
# Returns: json object 
@app.route('/api/getoptions', methods=['GET'])
def get_data():
    query = request.args.get('query')
    data = search_courses(query)

    # Return the data as JSON using jsonify
    return jsonify(data)

@app.route('/api/getvideos',methods=['GET'])
def get_data2():
    playlistId = request.args.get("playlistid")
    videos = get_playlist(playlistId)
    print(videos)
    data = [get_youtube_chapters(v['video_id']) for v in videos]
    return jsonify(data)


# Start the server when this file is run directly
if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)