import streamlit as st
import os
from classifier import categorize_image
from PIL import Image

st.set_page_config(page_title="Smart Screenshot Organizer", page_icon="📂")

st.title("📂 Smart Screenshot Organizer")
st.write("Upload a screenshot and automatically organize it using OCR.")

st.divider()

# Upload Screenshot
uploaded_file = st.file_uploader("Upload Screenshot", type=["png","jpg","jpeg"])

if uploaded_file is not None:

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    file_path = os.path.join("screenshots", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    category = categorize_image(file_path)

    folder = os.path.join("categorized", category)

    if not os.path.exists(folder):
        os.makedirs(folder)

    new_path = os.path.join(folder, uploaded_file.name)

    # Prevent duplicate filenames
    base, ext = os.path.splitext(uploaded_file.name)
    counter = 1

    while os.path.exists(new_path):
        new_path = os.path.join(folder, f"{base}_{counter}{ext}")
        counter += 1

    os.rename(file_path, new_path)

    txt_old = file_path + ".txt"
    txt_new = new_path + ".txt"

    if os.path.exists(txt_old):
        os.rename(txt_old, txt_new)

    st.success(f"Screenshot moved to {category}")

    image = Image.open(new_path)
    st.image(image, caption="Processed Screenshot", use_container_width=True)

st.divider()

# Category Filter
st.subheader("Filter Screenshots")

categories = ["All","Coding","Study","Shopping","Social","Others"]

selected_category = st.selectbox("Select Category", categories)

st.divider()

# Search
st.subheader("Search Screenshots")

search = st.text_input("Search text inside screenshots")

st.divider()

# Gallery
st.subheader("Screenshot Gallery")

cols = st.columns(3)
i = 0

base_folder = "categorized"

if selected_category == "All":
    folders = ["Coding","Study","Shopping","Social","Others"]
else:
    folders = [selected_category]

for category in folders:

    folder_path = os.path.join(base_folder, category)

    if not os.path.exists(folder_path):
        continue

    for file in os.listdir(folder_path):

        if file.endswith((".png",".jpg",".jpeg")):

            image_path = os.path.join(folder_path, file)

            # Search filter
            if search:
                txt_path = image_path + ".txt"

                if os.path.exists(txt_path):
                    with open(txt_path,"r",errors="ignore") as f:
                        text = f.read().lower()

                    if search.lower() not in text:
                        continue

            with cols[i % 3]:

                st.image(image_path, use_container_width=True)

                # Download button
                with open(image_path,"rb") as f:
                    st.download_button(
                        "Download",
                        f,
                        file_name=file,
                        key=f"download_{file}_{i}"
                    )

                # Delete button
                if st.button(f"Delete {file}", key=f"delete_{file}_{i}"):

                    os.remove(image_path)

                    txt_file = image_path + ".txt"
                    if os.path.exists(txt_file):
                        os.remove(txt_file)

                    st.warning("Screenshot deleted")
                    st.rerun()

            i += 1
