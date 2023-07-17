import streamlit as st

import requests
from PIL import Image
from io import BytesIO

"""
the idea of this project is to create a webpage where one can see the visual impressions of moon and stars festival 23 in Locarno.
the site can be found under: https://moonnstars23.streamlit.app/
to make changes on the webiste, make changes in this file, push ut to git and run 'streamlit run app.py' in the command line
"""
def main():
    custom_css = """
        <style>
            body {
                background-color: #A17BA2 /* Replace this with the desired background color */
            }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    title = "Vielen Herzlichen Dank!"
    subtitle = "&#127769;" + "Moon&Stars Locarno 2023" + "&#127776;"
    emoji = "&#10024;"
    title_color = "#000000"  # Black color
    subtitle_color = "purple"#9c72a9"  # Hex color code for #9c72a9
   

    st.markdown(f"<h1 style='color:{title_color}; text-align:center;'>{emoji} {title} {emoji}</h1>", unsafe_allow_html=True)
    image_url1 = "https://raw.githubusercontent.com/szweidler/Stuff/main/photos/mns.jpg"
    st.image(image_url1, use_column_width = True)

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
   


if __name__ == "__main__":
    main()
