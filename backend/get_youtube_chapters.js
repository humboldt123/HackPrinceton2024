const YoutubeChaptersGetter = require('youtube-chapters-finder').default

async function getChapters(videoId) {
  try {
    const chapters = await YoutubeChaptersGetter.getChapter(videoId);
    console.log(JSON.stringify(chapters));  // Output as JSON for Python
  } catch (error) {
    console.error('Error fetching chapters:', error);
    process.exit(1);
  }
}

// Get video ID from command line arguments
const videoId = process.argv[2];
getChapters(videoId);
