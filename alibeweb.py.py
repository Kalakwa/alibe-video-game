from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title='Alibe', page_icon=':unamused:', layout='wide')


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as fi:
        st.markdown(f"<style>{fi.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Load assets
lottie_coding = load_lottieurl(
    'https://assets9.lottiefiles.com/packages/lf20_y2nlvxyz.json')
lottie_manny = Image.open('Pictures/manny.gif')
# header section
with st.container():
    st.title('Alibe')
    st.subheader('Where dreams meet reality...')
    st.write('On a Planet formed from combining the Lands of Physical, Spiritual, Space, Time, Light, '
             'and Sound, to become the 6 realms of consciousness, you decide the fate of the Planet Alibe... ')

# Features of Alibe
with st.container():
    st.write('-------------')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Includes')
        st.write('- A fluid and intangible sense of ideas to manifest a sense of upliftment and '
                 'encouragement within each player through a world of magic and adventure gameplay.')
        st.write(
            '- Explore 6 different realms and mysterious caves within Alibe, magic at hand.')
        st.write('- Create the ultimate sanctuary in a liberated world using a variety of tools to '
                 'restore the land with different vegetation, including ingredients for Alchemy and cooking! ')
        st.write('- Find the right way to express yourself in Alibe with over 500 customization options '
                 'for your character!')
        st.write('- Learn about living in Alibe with the mastery of 11 different classes to choose from, including the Sigil of '
                 'the Knights, Gardners, Geocachers, Snorkelers and more!')

        st.write('I wish you the best, and please reach out to my email \(found at the bottom\) '
                 'with any questions regarding the video game project. I have placed a request for information '
                 'at the bottom where you may enter your name, email, and add some notes or comments '
                 'you wish to share directly with me, the dev. I hope you are ready to make a powerful '
                 'impact in the world we Libb. Follow along my social media pages and turn on notifications '
                 'to get ready for Alibe: Libb Like Me!')
    with right_column:
        st_lottie(lottie_coding, height=300, key='coding')


with st.container():
    st.write('~~~~~~~~~')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(lottie_manny)


contact_form = """
<form action="https://formsubmit.co/mortapolis@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()

# art stuff
