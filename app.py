import streamlit as st

def main():
    title = "Herzlichen Dank!"
    subtitle = "Moon&Stars23"
    emoji = "&#10024;"
    title_color = "#000000"  # Black color
    subtitle_color = "#9c72a9"  # Hex color code for #9c72a9

    # st.title("")

    st.markdown(f"<h1 style='color:{title_color};'>{emoji} {title}</h1>", unsafe_allow_html=True)

    # st.subheader("Subtitle:")
    st.markdown(f"<h2 style='color:{subtitle_color};'>{subtitle}</h2>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
