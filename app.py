import streamlit as st

import requests
from PIL import Image
from io import BytesIO

def main():
    title = "Herzlichen Dank!"
    subtitle = "Moon&Stars23"
    emoji = "&#10024;"
    title_color = "#000000"  # Black color
    subtitle_color = "#9c72a9"  # Hex color code for #9c72a9

    # st.title("")

    st.markdown(f"<h1 style='color:{title_color}; text-align:center;'>{emoji} {title}</h1>", unsafe_allow_html=True)


    # st.subheader("Subtitle:")
    st.markdown(f"<h2 style='color:{subtitle_color}; text-align:center;'>{subtitle}</h2>", unsafe_allow_html=True)
    
    # Fetch the image from GitHub
    # "https://github.com/szweidler/Stuff/blob/main/photos/TitlePic.jpg"
    image_url = "https://raw.githubusercontent.com/szweidler/Stuff/main/photos/TitlePic.jpg"
    # image_url = "https://raw.githubusercontent.com/szweidler/Stuff/main/photos/mns.jpg"
    # image_url = "https://raw.githubusercontent.com/szweidler/workspaces/Stuff/main/photos/TitlePic.jpg"
    st.image(image_url, caption="Sample Image", use_column_width=True)
    
    # image = fetch_image(image_url)

    # if image is not None:
    #     st.image(image, use_column_width=True)


# def fetch_image(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return Image.open(BytesIO(response.content))
#     except Exception as e:
#         st.error(f"Error fetching the image: {e}")
#     return None

if __name__ == "__main__":
    main()
