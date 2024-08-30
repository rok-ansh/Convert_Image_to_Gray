import streamlit as st
from PIL import Image

# with st.expander("Start Camera"):
#     # Start the camera
#     camera_image = st.camera_input("Start Camera")

upload_image = st.file_uploader("Upload Image")

if upload_image:
    # Create a pillow image instance
    img = Image.open(upload_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render(Display) the graysacle image  on the webpage
    st.image(gray_img)