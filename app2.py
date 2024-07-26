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

        # st.subheader("Image Results")

        # for i in range(num_rows):
        #     col1, col2, col3 = st.columns(3)
        #     with col1:
        #         index = i * 3
        #         if index < num_images:
        #             st.image(data[index], use_column_width=True, caption=f"Image {index + 1}")
        #     with col2:
        #         index = i * 3 + 1
        #         if index < num_images:
        #             st.image(data[index], use_column_width=True, caption=f"Image {index + 1}")
        #     with col3:
        #         index = i * 3 + 2
        #         if index < num_images:
        #             st.image(data[index], use_column_width=True, caption=f"Image {index + 1}")
        # Use HTML to display images dynamically
        st.subheader("Image Gallery")
        html_content = """
        <style>
        .image-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr); /* 3 columns */
            gap: 20px; /* Space between images */
        }
        .image-grid img {
            width: 100%; /* Fixed width for columns */
            height: auto; /* Flexible height */
            object-fit: cover; /* Cover to maintain aspect ratio */
        }
        </style>
        <div class='image-grid'>
        """
        for img_url in data:
            html_content += f"<img src='{img_url}' />"
        html_content += "</div>"

        st.markdown(html_content, unsafe_allow_html=True)
else:
    # Display a default message if no search term is entered
    st.info("Type a search term and press Enter to see results.")


# import requests
# from bs4 import BeautifulSoup
# import streamlit as st

# # Set up the page configuration
# st.set_page_config(page_title="Unsplash Image Search", layout="wide")

# # Add a title and description
# st.title("Unsplash Image Search")
# st.markdown(
#     """
#     Enter a search term to find images from Unsplash. Images will be displayed dynamically based on their sizes.
#     """
# )

# # Input from user
# user_input = st.text_input("Search for images:", "")

# if user_input:
#     # Construct the URL and fetch the page
#     link = f"https://unsplash.com/napi/search/photos?page=2&per_page=20&query={user_input}"
#     unsplash_link = f"https://unsplash.com/s/photos/{user_input}"
#     st.markdown(f"**Link to Unsplash:** [Click here]({unsplash_link})")
#     res = requests.get(link)
#     soup = BeautifulSoup(res.text, "html.parser")
#     # Extract image URLs
#     image_links = []
#     for img_tag in soup.find_all("img", class_="I7OuT DVW3V L1BOa"):
#         img_url = img_tag.get("src")
#         if img_url:
#             image_links.append(img_url)

#     if len(image_links) == 0:
#         st.warning("No images found for the search term. Please try a different term.")
#     else:
#         st.success(f"Found {len(image_links)} images!")

#         # Use HTML to display images dynamically
#         st.subheader("Image Gallery")
#         html_content = "<div style='display: flex; flex-wrap: wrap; gap: 10px;'>"
#         for img_url in image_links:
#             html_content += f"<img src='{img_url}' style='width: auto; height: 300px; object-fit: cover; max-width: 100%;' />"
#         html_content += "</div>"

#         st.markdown(html_content, unsafe_allow_html=True)

# else:
#     st.info("Type a search term and press Enter to see results.")

# num_columns = 3
# columns = st.columns(num_columns)


# for index, img_url in enumerate(data):
#     col_index = index % num_columns
#     columns[col_index].image(img_url, use_column_width=True)

# import requests
# import streamlit as st

# # Set up the page configuration
# st.set_page_config(page_title="Unsplash Image Search", layout="wide")

# # Add a title and description
# st.title("Unsplash Image Search")
# st.markdown(
#     """
#     Enter a search term to find images from Unsplash. Images will be displayed dynamically based on their sizes.
#     """
# )

# # Input from user
# user_input = st.text_input("Search for images:", "")

# if user_input:
#     # Construct the URL for Unsplash API and Unsplash page link
#     api_link = f"https://unsplash.com/napi/search/photos?page=1&per_page=20&query={user_input}"
#     unsplash_link = f"https://unsplash.com/s/photos/{user_input}"

#     # Display the Unsplash link
#     st.markdown(f"**Link to Unsplash:** [Click here]({unsplash_link})")

#     # Fetch data from Unsplash API
#     try:
#         response = requests.get(api_link)
#         response.raise_for_status()  # Raise an error for bad responses
#         data = response.json()

#         # Extract image URLs from JSON response
#         image_links = []
#         for photo in data.get('results', []):
#             img_url = photo.get('urls', {}).get('regular', '')
#             if img_url:
#                 image_links.append(img_url)

#         if not image_links:
#             st.warning("No images found for the search term. Please try a different term.")
#         else:
#             st.success(f"Found {len(image_links)} images!")

#             # Display images dynamically
#             st.subheader("Image Gallery")
#             html_content = "<div style='display: flex; flex-wrap: wrap; gap: 10px;'>"
#             for img_url in image_links:
#                 html_content += f"<img src='{img_url}' style='width: auto; height: 300px; object-fit: cover; max-width: 100%;' />"
#             html_content += "</div>"

#             st.markdown(html_content, unsafe_allow_html=True)

#     except requests.exceptions.RequestException as e:
#         st.error(f"An error occurred: {e}")
# else:
#     st.info("Type a search term and press Enter to see results.")
