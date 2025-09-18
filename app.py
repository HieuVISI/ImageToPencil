import streamlit as st
from PIL import Image, ImageOps, ImageFilter
import numpy as np

st.title("Pencil Sketch")

uploaded_file = st.file_uploader("Upload image", type=["jpg","jpeg","png"])
if uploaded_file:
    pil_image = Image.open(uploaded_file).convert("L")  # grayscale
    inverted = ImageOps.invert(pil_image)
    blurred = inverted.filter(ImageFilter.GaussianBlur(10))
    inverted_blurred = ImageOps.invert(blurred)
    sketch = Image.fromarray(
        np.array(pil_image, dtype=np.float32) /
        (np.array(inverted_blurred, dtype=np.float32) + 1e-5) * 255.0
    ).convert("L")

    st.image(sketch, caption="Sketch")
