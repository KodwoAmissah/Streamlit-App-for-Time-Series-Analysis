##Load libraries
import streamlit as st
import streamlit as st
from PIL import Image

# Display the c title
st.title("Learn About Team CapeCod")

##set team image
image = Image.open('Team logo/MicrosoftTeams-image (2).jpg.png')

# Set the desired size 
new_size = (1080, 722)

# Resize the image
resized_image = image.resize(new_size)

##set the image
st.image(resized_image)



##info about the team
st.write("Team cape cod is a team created by azubi africa consisting of 5 members namely: Kodwo Amissah-Mensah,Alvin Momoh,Regina Naa Dedei Crabbe,Aliyyah Adebayo and Leon Allen Maina")
st.write("This team consists of hardworking individuals dedicated in reaching and achieving the same goal.This app is as a product of our good communication,efficient collaboration and overall hardwork. ")

st.subheader("Below are the members")

##For members
st.header("Kodwo Amissah-Mensah: Data Analyst(Team Lead)")
st.info('Aspiring Data Analyst|Machine Learning|Python|SQL|Data Visualization')
lead=Image.open('Team photos/photo_2023-03-16_18-13-22.jpg')
size=(400,400)
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


## Regina's info

st.header("Regina Crabbe: Data Analyst")
st.info('Data Analyst|Lecturer|Researcher|PHD Student')
lead=Image.open('Team photos/WhatsApp Image 2023-09-28 at 12.19.59.jpg')
size=(400,400)
lead_image=lead.resize(size)
st.image(lead_image)
st.subheader("Connect with Regina:")


# Button to send an email
if st.button("Email"):
    st.markdown('<a href="mailto:rndcrabbe@gmail.com">Send Email</a>', unsafe_allow_html=True)

# Button to visit LinkedIn profile
if st.button("LinkedIn Profile"):
    st.markdown('<a href="http://www.linkedin.com/in/regina-crabbe-ab11a5284">LinkedIn</a>', unsafe_allow_html=True)

# Button to visit medium
if st.button("Medium"):
    st.markdown('<a href="https://medium.com/@rndcrabbe">Medium</a>', unsafe_allow_html=True)

# Button to github
if st.button("Github"):
    st.markdown('<a href="https://github.com/reginacrabbe">github</a>', unsafe_allow_html=True)


##Aliyyah's info
st.header("Aliyyah Adebayo: Data Analyst")
st.info('Computer science student|Data Analytic enthusiast|chess lover')
lead=Image.open('Team photos/photo_2023-09-28_16-55-16.jpg')
size=(400,400)
lead_image=lead.resize(size)
st.image(lead_image)
st.subheader("Connect with Aliyyah:")



# Button to send an email
if st.button("Send Email"):
    st.markdown('<a href="mailto:adebayoaliyyah2020@gmail.com">Send Email</a>', unsafe_allow_html=True)

# Button to visit LinkedIn profile
if st.button("LinkedIn"):
    st.markdown('<a href="https://www.linkedin.com/in/aliyyah-adebayo-88a540233">LinkedIn</a>', unsafe_allow_html=True)

# Button to visit medium
if st.button("Blog"):
    st.markdown('<a href="https://medium.com/@adebayoaliyyah2020/">Medium</a>', unsafe_allow_html=True)

# Button to github
if st.button("Github Repository"):
    st.markdown('<a href="https://github.com/Aliyyah22">github</a>', unsafe_allow_html=True)


##alvin's info

st.header("Alvin Momoh: Data Analyst")
st.info('Data Analyst || Data Analytics Professional')
lead=Image.open('Team photos/WhatsApp Image 2023-09-28 at 19.48.07.jpg')
size=(400,400)
lead_image=lead.resize(size)
st.image(lead_image)

st.subheader("Connect with Alvin:")


# Button to send an email
if st.button("Contact through email"):
    st.markdown('<a href="mailto:momohalvin3@gmail.com">Send Email</a>', unsafe_allow_html=True)

# Button to visit LinkedIn profile
if st.button("View LinkedIn Profile"):
    st.markdown('<a href="http://www.linkedin.com/in/alvinmomoh">LinkedIn</a>', unsafe_allow_html=True)

# Button to visit medium
if st.button("Article"):
    st.markdown('<a href="https://medium.com/@chipmnkal/">Medium</a>', unsafe_allow_html=True)

# Button to github
if st.button("Check out my github"):
    st.markdown('<a href="https://github.com/DaitaMonk">github</a>', unsafe_allow_html=True)


##leons's info

st.header("Leon Maina: Data Analyst")
st.info('Data Analytics || Cloud Computing || AI/ML || Quantum Computing')
lead=Image.open('Team photos/WhatsApp Image 2023-10-02 at 11.28.44.jpg')
size=(400,400)
lead_image=lead.resize(size)
st.image(lead_image)
st.subheader("Connect with Leon:")


# Button to send an email
if st.button("Personal email"):
    st.markdown('<a href="mailto:realeonallen@gmail.com">Send Email</a>', unsafe_allow_html=True)

# Button to visit LinkedIn profile
if st.button("LinkedIn_Profile"):
    st.markdown('<a href="https://LinkedIn.com/in/leo-allen">LinkedIn</a>', unsafe_allow_html=True)

# Button to visit medium
if st.button("Blog account"):
    st.markdown('<a href="https://medium.com/@leon.maina">Medium</a>', unsafe_allow_html=True)

# Button to github
if st.button("View github"):
    st.markdown('<a href="https://GitHub.com/realeonallen">github</a>', unsafe_allow_html=True)


