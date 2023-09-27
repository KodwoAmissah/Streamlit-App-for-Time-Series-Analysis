##Load libraries
import streamlit as st
import streamlit as st
from PIL import Image

# Display the c title
st.title("Learn About Team CapeCod")

##set team image
image = Image.open('C:\\Users\\User\\Pictures\\Camera Roll\\MicrosoftTeams-image (2).jpg.png')

# Set the desired size 
new_size = (750, 400)

# Resize the image
resized_image = image.resize(new_size)

##set the image
st.image(resized_image)

##info about the team
st.write("Team cape cod is a team created by azubi africa consisting of 5 members namely: Kodwo Amissah-Mensah,Alvin Momoh,Regina Naa Dedei Crabbe,Aliyyah Adebayo and Leon Allen Maina")
st.write("This team consists of hardworking individuals dedicated in reaching and achieving the same goal.This app is as a product of our good communication,efficient collaboration and overall hardwork. ")

st.subheader("Below are the members")

st.header("Kodwo Amissah-Mensah: Data Analyst(Team Lead)")
st.info('Aspiring Data Analyst|Machine Learning|Python|SQL|Data Visualization')
lead=Image.open('c:\\Users\\User\\Desktop\\Work photo\\photo_2023-03-16_18-13-22.jpg')
size=(750,850)
lead_image=lead.resize(size)
st.image(lead_image)

st.subheader("Connect with Kodwo:")



# Button to send an email
if st.button("Contact Me via Email"):
    st.markdown('<a href="mailto:kodwoam@gmail.com">Send Email</a>', unsafe_allow_html=True)

# Button to visit LinkedIn profile
if st.button("Visit My LinkedIn Profile"):
    st.markdown('<a href="https://www.linkedin.com/in/kodwoamissahmensah">LinkedIn</a>', unsafe_allow_html=True)

# Button to visit medium
if st.button("Read my blogs"):
    st.markdown('<a href="https://medium.com/@kodwoam">Medium</a>', unsafe_allow_html=True)

# Button to github
if st.button("Check out my github repositories"):
    st.markdown('<a href="https://github.com/KodwoAmissah">github</a>', unsafe_allow_html=True)

