from pathlib import Path

import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"



# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | John Doe"
PAGE_ICON = ":wave:"
NAME = "Kazi Moshiur Rahaman"
DESCRIPTION = """
Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "moshiur.mubin0@email.com"
SOCIAL_MEDIA = {
    # "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://www.linkedin.com/in/kazi-moshiur-rahaman-665360186/",
    "GitHub": "https://github.com/moshiurmubin",
    # "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience")
st.write(
    """
- ✔️ 3 Years expereince extracting actionable insights from big data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python(Tensorflow, Pandas,Numpy,Matplotlib),SQL, C
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Machine learning, Deep learning 
- 🗄️ Databases: MongoDB, MySQL
   
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst | Daraz Bangladesh Ltd** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  -April 2022 - December 2023")
st.write(" **KPIs:** Customer NPS,Reverse Leadtime,IPO")
st.write(" **Tools:** SQL,Python,Excel,Power BI") 
st.write(
    """
- ► Conduct meetings with TL and managers about the fluctuations of incoming cases in &nbsp;&nbsp;&nbsp;&nbsp;  database to decrease IPO (increased 187 from the previous)
- ► Try to increase Customer NPS by conducting surveys and other data driven solutions &nbsp;&nbsp;&nbsp;&nbsp;  (7% increased) and decreased Reverse leadtime by 1.4 day  
- ► Give data support to the team as well as other departments
- ► Convert big data into actionable insights by predicting and modelling future outcomes &nbsp;&nbsp;&nbsp;&nbsp; to enhance customer experience.
- ► Furnish insights, analytics to guide decisions for future projects.
- ► Developed BI Report and Dashboard using Alibaba's in-house Data Visualization &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Software and Power BI
- ► Run and Overseeing Customer Experience Projects, specifically working on &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;improvement of customer claim

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧","**Junior Developer | Flatknit International Ltd** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -Oct 2021 - Feb 2022")
st.write("**Projects:** Ecommerce Site, Website")
st.write("**Tools:** Wordpress,Excel,Google Analytics") 


st.write(
    """
- ► Worked with the developer team and build their website, e-commerce site
- ► Analyzed the social media market and regularly update on there 
- ► Communicated with customers, delivery team and vigilant over the store products
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Junior Developer & QA Engineer | ICS System Solution (Internship)** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -Jan 2021 - June 2021")
st.write("**Projects:** SCM software – Garment, Asset management software - Bank ")
st.write(
"""
- ►	Worked with the developing team as jr. developer 
- ► Met with authorities and end-users to know about their need and requirements
- ► Analyzed, designed, made documentation and submitted those to the developing team
- ►	Tested the regular update of software given by developer
- ►	Took training sessions on regular to explain the functions of the software to the clients &nbsp;&nbsp;&nbsp;&nbsp; and users 
	

"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Educations")
st.write("---")
st.write(
    """
- 🧑‍🎓 Masters in Applied Statistics & Data Science : Jahangirnagar University &nbsp;&nbsp;&nbsp;&nbsp; 2022-
- 🧑‍🎓 B.Sc. in Computer Science and Engineering : North South University &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	 - 2021 
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Specialized Trail - Artificial Intelligence
- 🧑‍🎓 Higher Secondary School Certificate (HSC) : Notre Dame College &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -2016
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	  Group – Science
- 🧑‍🎓  Secondary School Certificate (SSC) : Udayan Uchcha Madhyamik Bidyalaya &nbsp;&nbsp;&nbsp;&nbsp; -2014
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Group – Science
"""
)

