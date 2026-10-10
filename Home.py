import streamlit as st

st.set_page_config(
    page_title="World Cities",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 World Cities")
st.write("Welcome to the World Cities Streamlit App!")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    ### About This App
    Explore and discover cities from around the world. 
    Navigate to the **Cities** page to get started!
    """)
    
    if st.button("Go to Cities App →", key="main_button", use_container_width=True):
        st.switch_page("pages/app.py")

st.divider()
st.markdown("""
---
*Discover the world, one city at a time* 🚀
""")
