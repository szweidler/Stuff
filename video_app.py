import streamlit as st
from moviepy.editor import VideoFileClip

def main():
    st.title("Video App with Streamlit")
    st.subheader("Welcome to the video app! Please upload and view your videos below:")

    # File upload widget to upload videos
    uploaded_files = st.file_uploader("Upload videos", type=["mp4", "avi", "mov"], accept_multiple_files=True)

    if uploaded_files:
        for file in uploaded_files:
            # Display the video title
            st.subheader(f"Video: {file.name}")

            # Process and display the video
            video_bytes = file.read()
            st.video(video_bytes)

            # Show video details (optional)
            video_duration = get_video_duration(file)
            st.write(f"Duration: {video_duration:.2f} seconds")

def get_video_duration(file):
    # Use moviepy to get video duration
    video_clip = VideoFileClip(file)
    duration = video_clip.duration
    video_clip.close()
    return duration

if __name__ == "__main__":
    main()
