import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Pencil Sketch with OpenCV")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read file as a PIL image then to numpy
    pil_image = Image.open(uploaded_file).convert("RGB")
    image = np.array(pil_image)  # RGB order

    st.image(image, caption='Original Image', use_column_width=True)

    # OpenCV expects BGR
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray_image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

    # Invert grayscale
    inverted_image = 255 - gray_image

    # Blur the inverted image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred = 255 - blurred

    # Create the pencil sketch
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    # Show sketch
    st.image(pencil_sketch, caption='Pencil Sketch', use_column_width=True, channels='GRAY')

    # Optionally download sketch
    result = Image.fromarray(pencil_sketch)
    st.download_button(
        label="Download Sketch",
        data=result.tobytes(),
        file_name="pencil_sketch.png",
        mime="image/png"
    )
else:
    st.info("Upload an image to see the pencil sketch effect.")
