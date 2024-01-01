from pages import twitter, intro, app
import streamlit as st

# Page config 
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

# Session state test
if "shared" not in st.session_state:
   st.session_state["shared"] = True


# ============================== 


# def main() -> None:
#     # user_name = intro.get_name()

#     # Title 
#     st.title('🦜️🔗 Youtube Script generator (GPT)')
#     # Say Hello 
#     st.write("Hello acnd welcome to the site.")

#     # Get username 
#     user_name = st.text_input('Please type in your name: ')
#     output = twitter.run_search(user_name)

# if __name__ == "__main__":
#     main()