import streamlit as st

import requests
from PIL import Image
from io import BytesIO

# from IPython.display import YouTubeVideo

def main():
    title = "Vielen Herzlichen Dank!"
    subtitle = "Moon&Stars Locarno 2023"
    emoji = "&#10024;"
    title_color = "#000000"  # Black color
    subtitle_color = "purple"#9c72a9"  # Hex color code for #9c72a9

    # st.title("")

    st.markdown(f"<h1 style='color:{title_color}; text-align:center;'>{emoji} {title} {emoji}</h1>", unsafe_allow_html=True)
    image_url1 = "https://raw.githubusercontent.com/szweidler/Stuff/main/photos/mns.jpg"
    st.image(image_url1, use_column_width = True)

    # st.subheader("Subtitle:")
    st.markdown(f"<h2 style='color:{subtitle_color}; text-align:center;'>{subtitle}</h2>", unsafe_allow_html=True)
    
    # in order that the pictures and videos are shown the repository has to be public
    image_url2 = "https://raw.githubusercontent.com/szweidler/Stuff/main/photos/TitlePic.jpg"
    # video_url1 = "https://raw.githubusercontent.com/szweidler/Stuff/main/photos/IMG_1815.MOV"


    st.image(image_url2, caption="Ryan Tedder (15.7.23)", use_column_width=True)

    # st.write('Some impressions of Saturday night at Moon and Stars festival 2023 ()')
    st.markdown('<p style="text-align: center; font-size: 20px;">Some impressions of Saturday night at Moon and Stars festival 2023</p>', unsafe_allow_html=True)
    # Hyperlink with markdown
    st.markdown("[Mishaal Tamer](https://youtube.com/shorts/3MZHcmfJTqE?feature=share)")
    # st.video(youtube_url1)
    st.markdown("[Tom Gregory](https://youtube.com/shorts/kCYew_fPfnc?feature=share)")

    st.markdown("[One Republic, I ain't worried ](https://youtube.com/shorts/LnqMYc8MFVA?feature=share)")

    st.markdown("[One Republic, thats what i want](https://youtube.com/shorts/KSf4IjgxLUU?feature=share)")

    st.markdown("[One Republic, Halo](https://youtu.be/KcrSluLfHO0)")

    st.markdown("[One Republic, Secrets](https://youtu.be/kOjtYCvmWbo)")
    # youtube_url2 =  "https://youtube.com/shorts/kCYew_fPfnc"
    # st.write("Tom Gregory:")
    # st.video(youtube_url2)
    
   

    # st.title("List of YouTube Videos")

#     # Define the list of video links and descriptions
#     video_data = [
#         {
#             "url": "https://youtube.com/shorts/3MZHcmfJTqE",
#             "description": "Mishaal Tamer"
#         },
#         {
#             "url": "https://youtube.com/shorts/kCYew_fPfnc",
#             "description": "Tom Gregory - Never Let me Down"
#         },
#         # Add more videos with their URLs and descriptions here
#     ]

#     for i, video_info in enumerate(video_data):
#         st.write(f"Video {i + 1}")
#         st.write(f"Description: {video_info['description']}")
#         st.write("YouTube Video:")
#         video_url = video_info['url']
#         video_id = extract_video_id(video_url)
#         YouTubeVideo(video_id)


# def extract_video_id(video_url):
#     # Extract the video ID from the YouTube URL
#     video_id = None
#     if "youtube.com/watch" in video_url or "youtu.be/" in video_url:
#         if "youtube.com/watch" in video_url:
#             video_id = video_url.split("v=")[1]
#         else:
#             video_id = video_url.split("/")[-1]
#         video_id = video_id.split("&")[0]
#     else:
#         raise ValueError("Invalid YouTube URL")
#     return video_id


if __name__ == "__main__":
    main()
