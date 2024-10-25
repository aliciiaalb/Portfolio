import streamlit as st 
import json
from PIL import Image
import os
import base64  # Add this line to import base64
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import plotly.graph_objects as go  # Ensure this is imported for Plotly tables

# Adding some CSS for styling
# Adding some CSS for styling
st.markdown(
    """
    <style>
    /* Apply background color to the whole page */
    body {
        background-color: #FDF6F3;
    }

    li {
    padding : 15px;
    }

    p {
        font-size : 25px; !important
    }

    /* Streamlit elements can have custom backgrounds */
    [data-testid="stAppViewContainer"] {
        background-color: #FDF6F3;
        max-width: 100vw;  /* Utilise toute la largeur de la fenêtre */
        padding-left: 0px;  /* Pas de marges à gauche */
        padding-right: 0px; /* Pas de marges à droite */
    }

    /* Conteneur principal */
    [data-testid="stMainBlockContainer"] {
        max-width: 90% !important;  /* Utiliser toute la largeur visible */
        margin-left: auto; 
        margin-right: auto;
        padding-left: 4rem;  /* Ajouter un peu de marge pour éviter que le texte touche les bords */
        padding-right: 4rem;
    }


    /* Styling the sidebar with a background color */
    [data-testid="stSidebar"] {
        background-color: #C38E77;
        width: 250px;  /* Assure que la sidebar prend bien toute la largeur possible */
        position: fixed;  /* Garde la sidebar en position fixe à gauche */
        left: 0;
        top: 0;
        height: 100vh;  /* Prend toute la hauteur */
        display : flex;
        flex-direction : column; !important
        justify-content: space-between; !important
        align-items: center; !important
    }

    /* Largeur maximale pour le contenu Markdown */
    .stMarkdown {
        max-width: 100% !important;  /* Forcer le contenu markdown à occuper toute la largeur */
        padding-left: 20px;  /* Petite marge pour éviter que le texte touche les bords */
        padding-right: 20px; /* Petite marge pour éviter que le texte touche les bords */
    }

    /* Style pour les images */
    .stImage {
        max-width: 100% !important;  /* Forcer les images à occuper toute la largeur */
    }

    .sidebar-title {
        font-size: 35px;
        font-weight: bold;
        text-align: center;
        color: white;
        margin-bottom: 20px;
    }

    .sidebar-button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        font-size: 24px; !important
        padding: 15px;
        margin-bottom: 15px;
        text-align: center;
    }

    .stButton button {
        font-size: 40px !important;  /* Cible les boutons générés par Streamlit */
        width: 100% !important;  /* Ajuste la largeur des boutons */
        padding: 15px !important;
        margin-bottom: 10px !important;
        border-radius: 12px !important;  /* Ajoute un arrondi pour un meilleur design */
        text-align: center; !important
    }

    
    .sidebar-button:hover {
        background-color: #45a049;
    }

    
    .profile-pic-top-right {
        position: absolute;
        top: 2px;
        right: 1px;
        border-radius: 10%;  /* Make the image rounded */
        width: 170px;
        height: 170px;
        overflow: hidden;
    }

    .profile-pic-top-right img {
        width: 100%;
        height: auto;
    }

    .download-resume a {
        display: inline-block;
        background-color: #007BFF;
        color: white;
        padding: 10px 15px;
        text-decoration: none;
        border-radius: 8px;
        font-weight: bold;
        font-size: 20px;
    }

    .download-resume a:hover {
        background-color: #0056b3;
    }

    .separator {
        height: 2px;
        background-color: #ddd;
        margin: 30px 0;
    }

    .section {
        margin-top: 20px;
    }

     .contact-section {
        font-size: 28px;  /* Increased font size */
        font-weight: bold;  /* Made the text bold */
        color: white;  /* Adjusted text color */
    }

    .icon-container2 {
        display: flex;
        justify-content: left;
        gap: 20px;
        margin-top: 30px;  /* Add space above icons */
        margin-bottom: 10px;  /* Added margin below the icons */
    }
    .icon-container2 a {
        text-decoration: none;
    }
    .icon-container2 img {
        width: 40px;
        height: 40px;
    }

    .email-text {
        font-size: 16px;
        color: white;
        margin-top: 10px;
    }

    .school-logo {
        margin-top: 15px;
        text-align: center;
        max-width: 150px;  /* Restrict the max width for better alignment */
    }
    </style>
    """, unsafe_allow_html=True
)

# Sidebar with buttons with a more creative design
st.sidebar.markdown("<div class='sidebar-title'>Alicia LE BRUN</div>", unsafe_allow_html=True)

# Navigation buttons: 'About Me' first, followed by the projects
nav = "About Me"  # Default to 'About Me' if nothing is selected

if st.sidebar.button("About Me", key="4", help="Learn more about Alicia"):
    nav = "About Me"
if st.sidebar.button("Educational landscape", key="1", help="Analyse socio-démographique des lycéens"):
    nav = "Projet 1 : Analyse socio-démographique des lycéens"
if st.sidebar.button("Diabetes classification", key="2", help="Classification du diabète"):
    nav = "Projet 2 : Classification du diabète"

# Add separator before contacts
st.sidebar.markdown("<div class='separator'></div>", unsafe_allow_html=True)

st.sidebar.markdown('<div style="font-size: 28px; font-weight: bold; color: white;"><u>Contacts</u></div>', unsafe_allow_html=True)

# Display email
st.sidebar.markdown(f"""
    <div class="email-text">📧 Email: alicia.le-brun@efrei.net</div>
""", unsafe_allow_html=True)

# Icons for LinkedIn, GitHub, email, and school logo
st.sidebar.markdown("""
<div class="icon-container2">
    <a href="https://www.linkedin.com/in/alicia-le-brun-457315218/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
    </a>
    <a href="https://github.com/aliciiaalb" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
    </a>
</div>
""", unsafe_allow_html=True)


# Add separator before contacts
st.sidebar.markdown("<div class='separator'></div>", unsafe_allow_html=True)

# School logo at the bottom
school_logo_path = 'logo.png'  # Assuming you uploaded your school logo here
if os.path.exists(school_logo_path):
    school_logo = Image.open(school_logo_path)
    st.sidebar.image(school_logo, use_column_width=True)

# Default to 'About Me' if nothing is selected
if nav is None:
    nav = "About Me"

# Encode the image in base64 to embed in HTML
def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Function to create the download link with custom styling
def create_download_button(pdf_file, label):
    with open(pdf_file, "rb") as file:
        pdf_data = file.read()
    b64 = base64.b64encode(pdf_data).decode('utf-8')
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{pdf_file}">' \
        f'<button style="background-color: #007BFF; color: white; padding: 10px 20px; ' \
        f'border: none; border-radius: 8px; font-size: 20px;">{label}</button></a>'
    return href
    
def afficher_notebook_avec_images(notebook_path, image_map):
    try:
        # Lecture du notebook
        with open(notebook_path, "r", encoding='utf-8') as f:
            notebook_content = json.load(f)

        cell_index = 0  # Compteur de cellules

        # Affichage des cellules 'markdown' et 'code'
        for cell in notebook_content['cells']:
            if cell['cell_type'] == 'markdown':
                st.markdown(''.join(cell['source']))
            elif cell['cell_type'] == 'code':
                st.code(''.join(cell['source']), language='python')

            # Affichage d'images après des cellules spécifiques
            if cell_index in image_map:
                image_info = image_map[cell_index]  # Get the dictionary with path and width
                image_path = image_info['path']  # Extract the path
                width = image_info.get('width', None)  # Extract the width if provided, otherwise None

                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    st.image(image, caption=f"Résultat visuel {cell_index}", width=width)  # Display image with specified width
            
            cell_index += 1  # Incrémenter le compteur de cellules

    except FileNotFoundError:
        st.error(f"Notebook non trouvé à l'emplacement {notebook_path}. Vérifiez le chemin d'accès.")

# About Me section
if nav == "About Me":

    # Use the uploaded image
    image_path = "profile_picture.jpg"  # Path to your uploaded image
    image_base64 = get_image_base64(image_path)

    # Display the rounded profile picture at the top right
    st.markdown(f"""
        <div class='profile-pic-top-right'>
            <img src="data:image/png;base64,{image_base64}" alt="Profile Picture">
        </div>
    """, unsafe_allow_html=True)

        
    st.title("Alicia LE BRUN")
    st.subheader("M1 Data Engineering Student")
    
    st.markdown("---")


    # Add some engaging text
    st.markdown("""
    **Welcome to my portfolio!** \n
                
Where some see rows of numbers and columns of data, I see stories waiting to be told. Since I entered the world of data, I’ve discovered that behind every dataset lie answers, discoveries.\n

As an M1 Data Engineering student at Efrei Paris, I’ve had the opportunity to learn a great deal about the world of computer science, digital technology, and data...\n

My journey is driven by a thirst to understand the unseen, to explore the infinite potential of information and reveal what is hidden from the naked eye. Whether it’s predicting trends, understanding behaviors, or optimizing processes, each project is a new adventure for me. I like to think that when data is truly understood, it can become a compass, guiding us in a complex and ever-changing world.\n

In this portfolio, you’ll find various projects completed throughout my studies, combining data visualization, machine learning...\n

Enjoy !

---            
""", unsafe_allow_html=True)
    
    st.markdown("""
    ### My current situation

    I am currently in the middle of my 7th semester, at the end of which I will have the opportunity to join [CREDOC](https://www.credoc.fr/) (Centre de Recherche pour l'Étude et l'Observation des Conditions de vie) for a 21-week Data Management internship.
    """, unsafe_allow_html=True)

    st.markdown("""
    ---

    ### Interests and Hobbies
    - Psychology
    - Dance
    - Animals
    - Mathematics

    ---""", unsafe_allow_html=True)

    # Create a DataFrame for your soft and hard skills with the required columns
    skills_data = {
        'Skill Type': ['Hard Skill', 'Soft Skill', 'Soft Skill', 'Soft Skill', 'Soft skill', 'Soft Skill', 'Soft skill', 'Soft skill', 'Hard skill', 'Hard skill', 'Hard skill', 'Soft skill', 'Hard skill'],
        'Skill Name': ['PL-SQL', 'Communication', 'Adaptability', 'Project management', 'Intellectual curiosity', 'Writing', 'Pressure management', 'Autonomy', 'C', 'Web programming', 'Data Vizualisation', 'People understanding', 'Linux'],
        'Tools': ['MySQL, PostgreSQL', '', '', 'Discord, Github', '', '', '', '', 'CLion', 'HTML, CSS, JS, ViewJS', 'Matplotlib, Seaborn, Streamlit', '', 'Ubuntu'],
        'Proficiency (/5)': ['4.5', '5', '4', '4', '5', '4', '4', '3.5', '3.5', '3.5', '3.5', '5', '4']
    }
    skills_df = pd.DataFrame(skills_data)

    def generate_streamlit_table():
        st.markdown("### My Soft and Hard Skills")
        st.dataframe(skills_df)

    generate_streamlit_table()

    st.markdown("---")

    
    # Include a progress bar for skills
    st.markdown("### Languages")
    skills = {"French (Native)": 100, "English (C1)": 80, "Espagnol (B2)": 55, "Portuguese (A1)": 15}
    
    for skill, level in skills.items():
        st.markdown(f"**{skill}:**")
        st.progress(level / 100)
    

    # Interactive project section using expanders
    st.markdown("---")
    st.markdown("### School Projects & Data Science")

    with st.expander("**Spotihub** (October 2024)"):
        st.image("spotihub.png", width=100) 
        st.markdown("""
        - **Team Size**: 4 students
        - **Description**: Simple and intuitive interface which displays individual statistics (the most listened-to artists and tracks), offers a global ranking of the 50 most popular songs at the moment and generates tailored recommendation based on the users' music listening habits.""")

    with st.expander("**PatentSense** (June 2024 - July 2024)"):
        st.image("patentsense.png", width=100)  
        st.markdown("""
    - **Team Size**: 5 students
    - **Description**: Responded to a tender launched by the company LIPSTIP.
    - **Tech Stack**: Used **RoBERTa** with an F1 score of 0.78.
    - **Features**:
        - Predicts the patent class based on its description.
        - Highlights important words for interpretability.
        - Automatically generates a summary of the patent.
    """)

    with st.expander("**KityTracker** (January 2024 - May 2024)"):
        st.image("kitytracker.png", width=100)  
        st.markdown("""
        - **Team Size**: 6 students
        - **Description**: Creation of a device to integrate into cat harnesses.
        - **Details**: Connected to a website, it can track the cat’s real-time movements, alert when it goes out of a certain zone, and calculate the distance traveled per day by the cat.
        """)

    st.markdown("---")

    st.markdown("### Achievements")

    # Top achievements section
    st.markdown("""
    - **TOEIC :** 915/990.
    - **Projet Voltaire :** 785/1000.
    """)
  
    st.markdown("---")

    # Display the download button with the custom style
    label = "**Download Resume**"
    st.markdown(create_download_button("CV.pdf", label), unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(
    """
    <style>
    .icon-container {
        display: flex;
        justify-content: left;
        gap: 20px;
    }
    .icon-container a {
        text-decoration: none;
    }
    .icon-container img {
        width: 40px;
        height: 40px;
    }
    </style>
    <div class="icon-container">
        <a href="https://www.linkedin.com/in/alicia-le-brun-457315218/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
        </a>
        <a href="https://github.com/aliciiaalb" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
        </a>
    </div>
    """, unsafe_allow_html=True
    )

# ----------------------------------------------------------------------------

# "Projet 1 : Analyse socio-démographique des lycéens"
elif nav == "Projet 1 : Analyse socio-démographique des lycéens":
    st.markdown("# EXPLORATION OF THE EDUCATIONAL LANDSCAPE: A MULTIDIMENSIONAL ANALYSIS")
    st.markdown("""This project takes you on a fascinating journey through the demographic data of French high school students, aiming to decode educational and linguistic patterns. Indeed, it allows us to explore the evolution of foreign language enrollments among students, understand why certain languages dominate in specific regions, and how these trends transform over time...

Starting with raw data from national observations, we analyzed enrollments in first and second foreign languages over a three-year period. In doing so, we sought to reveal regional trends, the evolution of language choices, and how these decisions might reflect cultural and economic realities.

But behind each number lies a story. Every language learning decision reflects an aspiration, a culture, or even an economic opportunity. This project allows you to visualize and better understand these dynamics, offering a fresh perspective on the French educational landscape.""")

    # Use the uploaded image
    image_path = "demography.png"  
    image_base64 = get_image_base64(image_path)

    # Display the rounded profile picture at the top right
    st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{image_base64}" alt="Diabetes Diagnosis with Machine Learning" style="width: 400px;">
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    # Afficher le notebook avec des images
    image_map_lyceens = {
        5: {'path': r"data_info.png", 'width': 500},
        7: {'path': r"columns.png", 'width': 600},
        11: {'path': r"Proportion of Girls and Boys in the Dataset.png", 'width': 600},
        15: {'path': r"Radar Chart of Gender Proportion by Educational Level.png", 'width': 600},  
        18: {'path': r"Proportion of Girls and Boys by Educational Level.png", 'width': 1200},
        20: {'path': r"Proportion of Girls and Boys by Educational Level2.png", 'width': 1200},
        22: {'path': r"Proportion of Girls and Boys by Educational Level3.png", 'width': 1200},
        27: {'path': r"Student population by sector.png", 'width': 650},
        31: {'path': r"Gender Proportions by Sector.png", 'width': 1000},
        39: {'path': r"Total Number of Students in Urban vs. Rural Areas.png", 'width': 900},
        44: {'path': r"Proportion of Students in Public vs. Private Sector (Urban vs. Rural).png", 'width': 900},
        50: {'path': r"Aggregated Distribution of LV1 Language Students by Region.png", 'width': 1400},
        53: {'path': r"Aggregated Distribution of LV1 (Spanish, German, and Other Languages) Students by Region.png", 'width': 1400},
        58: {'path': r"Aggregated Distribution of LV2 Language Students by Region.png", 'width': 1400},
        61: {'path': r"Aggregated Distribution of LV2 (English, German, Italian and Other Languages) Students by Region.png", 'width': 1400},
        65: {'path': r"map Total Other LV1 Languages.png", 'width': 1700},
        68: {'path': r"map Total Other LV2 Languages.png", 'width': 1700},
        72: {'path': r"Evolution of LV1 Language Enrollment by Educational Level.png", 'width': 1000},
        74: {'path': r"Evolution of LV1 Language Enrollment by Educational Level2.png", 'width': 1000},
        77: {'path': r"Evolution of LV2 Language Enrollment by Educational Level.png", 'width': 1000},
        79: {'path': r"Evolution of LV2 Language Enrollment by Educational Level2.png", 'width': 1000},
        82: {'path': r"Evolution of LV1 Language Choices Over the Years.png", 'width': 1400},
        83: {'path': r"Evolution of LV1 Language Choices Over the Years (Log Scale).png", 'width': 1400},
        85: {'path': r"Evolution of LV1 Language Choices Over the Years2.png", 'width': 1400},
        88: {'path': r"Evolution of LV2 Language Choices Over the Years.png", 'width': 1400},
        89: {'path': r"Evolution of LV2 Language Choices Over the Years (Log Scale).png", 'width': 1400},
        91: {'path': r"Evolution of LV2 Language Choices Over the Years2.png", 'width': 1400},
        94: {'path': r"Language Combinations (LV1 to LV2).png", 'width': 1300}
    }
    afficher_notebook_avec_images(r"Project dataviz.ipynb", image_map_lyceens)

    st.markdown("---")

    # Display the download button with the custom style
    label = "**Download Notebook**"
    st.markdown(create_download_button("Project dataviz.ipynb", label), unsafe_allow_html=True)

    # ------------------------------------------------------------------------------------------------------------------
    
# "Projet 1 : Classification du diabète"
elif nav == "Projet 2 : Classification du diabète":
    st.markdown("# A JOURNEY THROUGH DATA TO DIAGNOSE DIABETES")
    st.markdown("Imagine a world where, from simple medical data, we can accurately predict whether a person has diabetes or not. This project follows that approach: using the power of Machine Learning to offer quick and reliable diagnoses.\n\nWe took a real dataset from a study on Pima Indian patients, containing information such as age, blood pressure, and many other medical characteristics. From these variables, the goal is to build a model capable of predicting whether a patient has diabetes.\n\nBeyond the numbers, each line in this dataset represents a life, a story. This project allows us to explore the impact of data in healthcare and to understand how artificial intelligence can become a vital ally in the early detection of diseases.")

    # Use the uploaded image
    image_path = "diabetes.png"  # Path to your uploaded image
    image_base64 = get_image_base64(image_path)

    # Display the rounded profile picture at the top right
    st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{image_base64}" alt="Diabetes Diagnosis with Machine Learning" style="width: 500px;">
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    image_map_diabetes={}
    
    afficher_notebook_avec_images(r"Notebook_Projet_ML_Alicia_LE_BRUN_I2_DE.ipynb", image_map_diabetes)

    st.markdown("---")

    # Display the download button with the custom style
    label = "**Download Notebook**"
    st.markdown(create_download_button("Project dataviz.ipynb", label), unsafe_allow_html=True)

