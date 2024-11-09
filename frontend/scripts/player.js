// Array of video paths - replace with your video paths
const videos = [
    '/dummy/1.mp4',
    '/dummy/2.mp4',
    '/dummy/3.mp4',
    '/dummy/4.mp4',
    '/dummy/5.mp4',
    '/dummy/6.mp4',
];

const videoContainer = document.getElementById('videoContainer');
let currentVideoIndex = 0;
let startY = 0;
let currentY = 0;

// Create video elements
videos.forEach(videoSrc => {
    const wrapper = document.createElement('div');
    wrapper.className = 'video-wrapper';
    
    const video = document.createElement('video');
    video.src = videoSrc;
    video.controls = false;
    video.loop = true;
    video.muted = true; // Start muted to allow autoplay
    
    const overlay = document.createElement('div');
    overlay.className = 'video-overlay';
    
    overlay.addEventListener('click', () => {
        if (video.paused) {
            video.play();
        } else {
            video.pause();
        }
    });
    
    wrapper.appendChild(video);
    wrapper.appendChild(overlay);
    videoContainer.appendChild(wrapper);
});

// Prevent default touch behaviors
document.body.addEventListener('touchmove', (e) => {
    e.preventDefault();
}, { passive: false });

// Touch event handlers
let isDragging = false;

videoContainer.addEventListener('touchstart', (e) => {
    isDragging = true;
    startY = e.touches[0].clientY;
    videoContainer.style.transition = 'none';
}, { passive: true });

videoContainer.addEventListener('touchmove', (e) => {
    if (!isDragging) return;
    
    const deltaY = e.touches[0].clientY - startY;
    currentY = -currentVideoIndex * window.innerHeight + deltaY;
    videoContainer.style.transform = `translateY(${currentY}px)`;
}, { passive: true });

videoContainer.addEventListener('touchend', (e) => {
    if (!isDragging) return;
    isDragging = false;
    
    const deltaY = e.changedTouches[0].clientY - startY;
    
    if (Math.abs(deltaY) > 50) { // Reduced threshold for easier swiping
        if (deltaY > 0 && currentVideoIndex > 0) {
            currentVideoIndex--;
        } else if (deltaY < 0 && currentVideoIndex < videos.length - 1) {
            currentVideoIndex++;
        }
    }

    currentY = -currentVideoIndex * window.innerHeight;
    videoContainer.style.transition = 'transform 0.3s ease-out';
    videoContainer.style.transform = `translateY(${currentY}px)`;

    // Play current video and pause others
    const videoElements = document.querySelectorAll('video');
    videoElements.forEach((video, index) => {
        if (index === currentVideoIndex) {
            video.play().catch(e => console.log('Playback failed:', e));
        } else {
            video.pause();
            video.currentTime = 0;
        }
    });
});

// Initialize first video
window.addEventListener('DOMContentLoaded', () => {
    const firstVideo = document.querySelector('video');
    firstVideo.play().catch(e => console.log('Initial playback failed:', e));
});