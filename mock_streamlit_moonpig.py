import streamlit as st

# Title and Search Bar
st.title("Personalised Wedding Cards")
st.text_input("Search...", placeholder="Search...")

# Filters
st.sidebar.header("Filters")
filter_options = ["For Her", "For Him", "Friend", "Colleague", "Couple", 
                  "Son and Partner", "Brother and Partner", "Daughter and Partner", 
                  "Sister and Partner", "Best Friend", "Dad and Partner"]
selected_filters = st.sidebar.multiselect("Choose Filters", filter_options)

# Sort By
sort_options = ["Popularity", "Price", "Newest"]
selected_sort = st.sidebar.selectbox("Sort By", sort_options)

# Card Display Section
st.header("Cards")
cards = [
    {"title": "Happy Wedding Day", "image": "image1.png"},
    {"title": "Cheers to the Couple", "image": "image2.png"},
    {"title": "Congratulations!", "image": "image3.png"},
    # Add more cards as needed
]

cols = st.columns(3)
for i, card in enumerate(cards):
    with cols[i % 3]:
        st.image(card["image"], use_column_width=True)
        st.write(card["title"])
        st.button("❤️ Add to Basket")

# Footer Section
st.sidebar.header("My Moonpig")
footer_links = ["Create Account", "Sign In", "Offers", "Moonpig Plus", 
                "Group Cards", "Balloons", "Need Some Help?", 
                "About Us", "The Small Details"]
for link in footer_links:
    st.sidebar.write(link)

st.sidebar.header("Payment Methods")
st.sidebar.image("payment_methods.png")  # Replace with actual image path

st.sidebar.header("Keep in Touch")
social_links = ["Facebook", "Twitter", "Instagram"]
for link in social_links:
    st.sidebar.write(link)

# Images: Replace "image1.png", "image2.png", etc., with the actual paths to your card images.
# Payment Methods: Replace "payment_methods.png" with the path to your payment methods image.
# Styling: Streamlit has limited styling options. For advanced styling, you may need to integrate CSS or use custom components.
# Functionality: This is a static representation. For dynamic content or interactions, you can connect to a backend or database.