import requests
import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Unsplash Image Search", layout="wide")
st.title("Unsplash Image Search")
st.markdown(
    """Enter a search term to find images from Unsplash. Images will be displayed dynamically based on their sizes."""
)

# Get user input
user_input = st.text_input("Search for images:", "")

# Initialize a set to store unique image URLs
unsplash_links = set()

# Fetch images if user input is provided
if user_input:
    # Loop through pages to get results
    for i in range(1, 10,2):  # Fetching 5 pages of results
        link = f"https://unsplash.com/napi/search/photos?page=1&per_page={i}&query={user_input}"
        response = requests.get(link)

        if response.status_code == 200:
            data = response.json()
            # Parse the JSON data to extract image URLs
            if "results" in data:
                for item in data["results"]:
                    if "urls" in item and "raw" in item["urls"]:
                        unsplash_links.add(item["urls"]["full"])
        else:
            st.error(
                "Failed to fetch data from Unsplash. Please check your API key and try again."
            )
            break

    # Convert the set back to a list to display
    unsplash_links = list(unsplash_links)
    num_images = len(unsplash_links)
    num_rows = (num_images ) // 3
    st.subheader("Image Gallery")

    for i in range(num_rows):
        col1, col2, col3 = st.columns(3)
        with col1:
            index = i * 3
            if index < num_images:
                st.image(unsplash_links[index], use_column_width=True)
        with col2:
            index = i * 3 + 1
            if index < num_images:
                st.image(unsplash_links[index], use_column_width=True)
        with col3:
            index = i * 3 + 2
            if index < num_images:
                st.image(unsplash_links[index], use_column_width=True)
else:
    st.info("Type a search term and press Enter to see results.")
