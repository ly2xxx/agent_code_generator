import streamlit as st

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ("Comments", "New Page"))

# Comments Page
if page == "Comments":
    st.title("Comments")

    # Like button
    if 'likes' not in st.session_state:
        st.session_state.likes = 0

    if st.button("Like"):
        st.session_state.likes += 1

    st.write(f"Likes: {st.session_state.likes}")

    # Comment input
    if 'comments' not in st.session_state:
        st.session_state.comments = []

    comment = st.text_input("Add a comment...")

    if st.button("Comment"):
        if comment:
            st.session_state.comments.append(comment)
            st.success("Comment added!")
        else:
            st.warning("Please enter a comment.")

    # Display comments
    st.subheader("Comments:")
    for c in st.session_state.comments:
        st.write(f"- {c}")

    # Share button (placeholder)
    if st.button("Share"):
        st.info("Share functionality coming soon!")

# New Page
elif page == "New Page":
    st.title("New Page Title")

    # Add content for the new page here
    st.write("This is a new page based on the design in your screenshot.")
    # Add further elements as needed (e.g., text fields, buttons)