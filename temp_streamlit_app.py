import streamlit as st

# Set the page config
st.set_page_config(page_title="Plans & Billing", layout="wide")

# Sidebar
with st.sidebar:
    st.header("Your organization")
    st.write("Members")
    st.write("Plans & billing")
    st.write("Rate limits")
    st.write("API keys")
    st.write("Logs")

# Main content
st.title("Plans & Billing")

# Notification banner
st.markdown(
    '<div style="background-color: #D72B2B; color: white; padding: 10px; border-radius: 5px;">'
    'To get started with Console, please ensure you have upgraded your plan and purchased credits, or claim your free credits.'
    '</div>',
    unsafe_allow_html=True,
)

# Plan section
st.subheader("Your plan")
st.selectbox("Select Plan", ["Evaluation", "Basic", "Pro"])

st.write("You have limited access right now. Please select a plan to use Claude in commercial applications.")

# Credit balance section
st.subheader("Credit balance")
st.write("Your credit balance will be consumed with API and Workbench usage.")

# Credit card image placeholder
st.image("https://via.placeholder.com/300x150.png?text=US$5", caption="US$5", use_column_width=True)

# Claim free credits button
if st.button("Claim free credits"):
    st.success("You have claimed your free credits!")
    st.write("Get started testing Claude with US$5 in free credits. These credits expire 14 days after being claimed.")