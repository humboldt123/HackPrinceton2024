import subprocess
import json







def get_youtube_chapters(video_id):
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
chapters = get_youtube_chapters("aircAruvnKk")
print(chapters)
