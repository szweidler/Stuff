import streamlit as st

def main():
    st.title("Streamlit Website with Title and Subtext")

    # Get user input for title, subtext, color, and emoji
    title = st.text_input("Enter the title:")
    subtext = st.text_area("Enter the subtext:")
    color = st.color_picker("Choose a color for the title", "#000000")
    emoji = st.text_input("Insert an emoji for the title (e.g., :smile:):")

    # Display the title with the selected color and emoji (if provided)
    title_with_emoji = f"{emoji} {title}" if emoji else title
    st.markdown(f"<h1 style='color:{color};'>{title_with_emoji}</h1>", unsafe_allow_html=True)

    # Display the subtext
    st.subheader("Subtext:")
    st.write(subtext)

if __name__ == "__main__":
    main()
