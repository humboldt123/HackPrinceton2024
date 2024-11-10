const videos = [
    {
        src: '/dummy/1.mp4',
        username: 'Awesome Sauce',
        description: 'Video 1 description',
        profilePic: 'https://bigrat.monster/media/bigrat.jpg'
    },
    {
        src: '/dummy/2.mp4',
        username: 'Aeesome Sauce',
        description: 'Video 2 description',
        profilePic: 'https://bigrat.monster/media/bigrat.jpg'
    },
    {
        src: '/dummy/3.mp4',
        username: 'Aeesome Sauce',
        description: 'Video 2 description',
        profilePic: 'https://bigrat.monster/media/bigrat.jpg'
    },
    {
        src: '/dummy/4.mp4',
        username: 'Aeesome Sauce',
        description: 'Video 2 description',
        profilePic: 'https://bigrat.monster/media/bigrat.jpg'
    },
    {
        src: '/dummy/5.mp4',
        username: 'Aeesome Sauce',
        description: 'Video 2 description',
        profilePic: 'https://bigrat.monster/media/bigrat.jpg'
    },
];

const videoContainer = document.getElementById('videoContainer');
let currentVideoIndex = 0;

function createVideoElement(videoData) {
    const wrapper = document.createElement('div');
    wrapper.className = 'video-wrapper';
    
    wrapper.innerHTML = `
        <div class="video-content">
            <video src="${videoData.src}" loop></video>
        </div>
        <div class="video-overlay">
            <div class="right-controls">
                <div class="control-button like-button">
                    <i class="fas fa-heart"></i>
                    <span>0</span>
                </div>
                <div class="control-button share-button">
                    <i class="fas fa-share"></i>
                    <span>Share</span>
                </div>
            </div>
            <div class="video-info">
                <div class="profile-section">
                    <img class="profile-pic" src="${videoData.profilePic}" alt="Profile">
                    <span class="username">${videoData.username}</span>
                    
                </div>
                <div class="video-description">
                    ${videoData.description}
                </div>
            </div>
        </div>
    `;

    // <button class="follow-button">Follow</button> 

    // Add event listeners
    const likeButton = wrapper.querySelector('.like-button');
    likeButton.addEventListener('click', (e) => {
        e.stopPropagation();
        const icon = likeButton.querySelector('i');
        const count = likeButton.querySelector('span');
        icon.classList.toggle('liked');
        count.textContent = icon.classList.contains('liked') ? '1' : '0';
    });

    const shareButton = wrapper.querySelector('.share-button');
    shareButton.addEventListener('click', (e) => {
        e.stopPropagation();
        // Add share functionality here
        alert('Share functionality coming soon!');
    });

    const video = wrapper.querySelector('video');
    wrapper.addEventListener('click', () => {
        toggleVideo(video);
    });

    return wrapper;
}

function toggleVideo(video) {
    if (video.paused) {
        video.play();
    } else {
        video.pause();
    }
}
videos.forEach(videoData => {
    const videoElement = createVideoElement(videoData);
    videoContainer.appendChild(videoElement);
});

// handle nav
function navigateToVideo(index) {
    if (index < 0 || index >= videos.length) return;
    
    currentVideoIndex = index;
    const newPosition = -currentVideoIndex * window.innerHeight;
    videoContainer.style.transform = `translateY(${newPosition}px)`;
    
    // play current vid, pause others
    const videoElements = document.querySelectorAll('video');
    videoElements.forEach((video, idx) => {
        if (idx === currentVideoIndex) {
            video.play().catch(e => console.log('Playback failed:', e));
        } else {
            video.pause();
            video.currentTime = 0;
        }
    });
}

document.addEventListener('keyup', event => {
    const currentVideo = document.querySelectorAll('video')[currentVideoIndex];
    
    if (event.code === 'Space') {
        event.preventDefault();
        toggleVideo(currentVideo);
    } else if (event.code === 'ArrowDown') {
        navigateToVideo(currentVideoIndex + 1);
    } else if (event.code === 'ArrowUp') {
        navigateToVideo(currentVideoIndex - 1);
    }
});

// prevent scroll
document.addEventListener('keydown', event => {
    if (event.code === 'Space') {
        event.preventDefault();
    }
});

// initial vid
window.addEventListener('DOMContentLoaded', () => {
    const firstVideo = document.querySelector('video');
    firstVideo.play().catch(e => console.log('Initial playback failed:', e));
});