import streamlit as st
from langchain_helper import generate_restaurant_name_and_items

st.set_page_config(page_title="Restaurant Name and Menu Generator", page_icon="🍽️",layout="centered")

st.title("🍽️ Restaurant Name and Menu Generator")
st.markdown("""
            Select a cuisine type and generate a fancy restaurant name **unique restaurant name** along with a list of popular dishes!
            """)
#sidebar
st.sidebar.image("https://media.istockphoto.com/id/981368726/vector/restaurant-food-drinks-logo-fork-knife-background-vector-image.jpg?s=612x612&w=0&k=20&c=9M26CBkCyEBqUPs3Ls5QCjYLZrB9sxwrSFmnAmNCopI=",width="stretch")
st.sidebar.title("About")

#cuisine selection dropdown
cuisine = st.selectbox(
    "Select Cuisine Type:",
    ("Italian", "Chinese", "Mexican", "Indian", "French", "Japanese", "Mediterranean", "Thai", "Spanish", "Greek","Russian")
)

if cuisine:
    with st.spinner(f"Generating restaurant name and menu for {cuisine} cuisine..."):
        try:
            response = generate_restaurant_name_and_items(cuisine)
            st.divider()
            st.markdown(f"### 🍴 Restaurant Name:")
            st.success(f"### 🍴 Restaurant Name: {response['restaurant_name']}")

            st.markdown(f"### 📜 Menu Items:")
            menu_items = response['menu_items'].split(',')
            for item in menu_items:
                st.write(f"- {item.strip()}")

        except Exception as e:
            st.error(f"An error occurred: {e}")

st.markdown("---")
st.markdown("Developed by Satyabrata Pradhan")