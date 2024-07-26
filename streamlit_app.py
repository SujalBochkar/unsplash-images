import requests
from bs4 import BeautifulSoup
import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Unsplash Image Search", layout="wide")

# Add a title and a description
st.title("Unsplash Image Search")
st.markdown(
    "Enter a search term to find images from Unsplash. Your search results will be displayed in a grid format."
)

# Input from user
user_input = st.text_input("Search for images:", "")

data = set()
if user_input:
    # Construct the URL and fetch the page
    link = f"https://unsplash.com/s/photos/{user_input}"
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "html.parser")

    # Find all 'img' tags with the specified class
    for img_tag in soup.find_all("img", class_="I7OuT DVW3V L1BOa"):
        if len(data) > 1000:
            break
        img_url = img_tag.get("src")
        if img_url:
            data.add(img_url)

    data = list(data)
    # Show a message if no images were found
    if len(data) == 0:
        st.warning("No images found. Please try a different search term.")
    else:
        st.success(f"Found {len(data)} images!")

        # Display images in a grid layout
        num_images = len(data)
        num_rows = (num_images + 2) // 3

        st.subheader("Image Results")

        for i in range(num_rows):
            col1, col2, col3 = st.columns(3)
            with col1:
                index = i * 3
                if index < num_images:
                    st.image(data[index], use_column_width=True, caption=f"Image {index + 1}")
            with col2:
                index = i * 3 + 1
                if index < num_images:
                    st.image(data[index], use_column_width=True, caption=f"Image {index + 1}")
            with col3:
                index = i * 3 + 2
                if index < num_images:
                    st.image(data[index], use_column_width=True, caption=f"Image {index + 1}")

        # Use HTML to display images dynamically
        # st.subheader("Image Gallery")
        # html_content = """
        # <style>
        # .image-grid {
        #     display: grid;
        #     grid-template-columns: repeat(3, 1fr); /* 3 columns */
        #     gap: 20px; /* Space between images */
        # }
        # .image-grid img {
        #     width: 100%; /* Fixed width for columns */
        #     height: auto; /* Flexible height */
        #     object-fit: cover; /* Cover to maintain aspect ratio */
        # }
        # </style>
        # <div class='image-grid'>
        # """
        # for img_url in data:
        #     html_content += f"<img src='{img_url}' />"
        # html_content += "</div>"

        # st.markdown(html_content, unsafe_allow_html=True)
else:
    # Display a default message if no search term is entered
    st.info("Type a search term and press Enter to see results.")
