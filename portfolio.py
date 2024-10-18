import streamlit as st
import json
from PIL import Image
import os

# Custom CSS for styling the page with a pale pink background for the entire page
st.markdown("""
    <style>
    /* Apply the pink background to the entire page */
    body {
        background-color: #FFE4E1;  /* Pale pink */
    }

    /* Sidebar title styling */
    .sidebar-title {
        text-align: center;
        font-size: 28px;
        color: #1F618D;
        margin-bottom: 40px;
        font-family: 'Arial', sans-serif;
    }

    /* Button Styles */
    .button {
        display: block;
        width: 90%;
        padding: 15px;
        margin: 15px auto;
        text-align: center;
        background-color: #2E86C1;
        color: white;
        border-radius: 30px;
        font-size: 18px;
        font-family: 'Arial', sans-serif;
        text-decoration: none;
        border: 2px solid transparent;
        transition: background-color 0.3s, transform 0.3s;
    }

    /* Hover effect for buttons */
    .button:hover {
        background-color: #1ABC9C;
        color: white;
        transform: scale(1.05);
        border-color: #148F77;
    }

    /* Custom styling for h1, h2, p */
    h1, h2 {
        font-family: 'Arial', sans-serif;
        color: black;
    }
    p {
        font-family: 'Verdana', sans-serif;
        color: black;
    }

    /* Profile picture centering */
    .profile-pic {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
    }

    /* Resume button styling */
    .download-resume {
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)


# Sidebar with buttons with a more creative design
st.sidebar.markdown("<div class='sidebar-title'>Alicia LE BRUN</div>", unsafe_allow_html=True)

# Buttons for navigation
nav = None
if st.sidebar.button("Projet 1", key="1", help="Classification du diabète"):
    nav = "Projet 1 : Classification du diabète"
if st.sidebar.button("Projet 2", key="2", help="Analyse socio-démographique des lycéens"):
    nav = "Projet 2 : Analyse socio-démographique des lycéens"
if st.sidebar.button("Projet 3", key="3", help="Analyse des données Uber"):
    nav = "Projet 3 : Uber"
if st.sidebar.button("About Me", key="4", help="Learn more about Alicia"):
    nav = "About Me"

# Default to 'About Me' if nothing is selected
if nav is None:
    nav = "About Me"

# Fonction pour lire et afficher le contenu d'un notebook avec insertion d'images à des endroits spécifiques
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
                image_path = image_map[cell_index]
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    st.image(image, caption=f"Résultat visuel {cell_index}", use_column_width=True)
            
            cell_index += 1  # Incrémenter le compteur de cellules

    except FileNotFoundError:
        st.error(f"Notebook non trouvé à l'emplacement {notebook_path}. Vérifiez le chemin d'accès.")

# Display the selected content
if nav == "About Me":
    st.title("Alicia LE BRUN")
    st.subheader("M1 Data Engineering Student")
    st.markdown("---")
    st.markdown("<div class='profile-pic'>", unsafe_allow_html=True)
    st.image("C:/Scolarité/Efrei/M1/DATAVIZ/Portfolio/profile_picture.jpg", width=150)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='download-resume'>
        <a href='C:/Scolarité/Efrei/M1/resume.pdf' download>Download Resume</a>
    </div>
    """, unsafe_allow_html=True)

# "Projet 1 : Classification du diabète"
elif nav == "Projet 1 : Classification du diabète":
    st.header("Projet 1 : Classification du diabète")
    st.markdown("Voici le contenu du projet sous forme de notebook Jupyter.")
    
    # Afficher le notebook (ajuste le chemin vers le notebook et les images si nécessaire)
    image_map_diabetes = {
        # Ajouter des images si nécessaire
    }
    afficher_notebook_avec_images("C:/Scolarité/Efrei/M1/ML/Notebook_Projet_ML_Alicia_LE_BRUN_I2_DE.ipynb", image_map_diabetes)

# "Projet 2 : Analyse socio-démographique des lycéens"
elif nav == "Projet 2 : Analyse socio-démographique des lycéens":
    st.header("Projet 2 : Analyse socio-démographique des lycéens (2020-2023)")
    st.markdown("""
        <div class='section'>
        ### Introduction
        Ce projet analyse les données des lycéens français sur plusieurs années pour mieux comprendre les tendances démographiques.
        Nous nous sommes concentrés sur la répartition géographique et l'évolution des inscriptions dans les différentes langues étrangères.
        
        ### Méthodologie
        L'analyse se base sur les données publiques et utilise des techniques de visualisation avancées pour illustrer les différences entre les régions.
        </div>
    """, unsafe_allow_html=True)

    # Séparation visuelle avant le début du projet
    st.markdown("<div class='separator'></div>", unsafe_allow_html=True)

    # Afficher le notebook avec des images
    image_map_lyceens = {
        5: "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\data_info.png",
        7: "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\columns.png",
        11: "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Proportion of Girls and Boys in the Dataset.png",
        15 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Radar Chart of Gender Proportion by Educational Level.png",  
        18 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Proportion of Girls and Boys by Educational Level.png",
        20 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Proportion of Girls and Boys by Educational Level2.png",
        22 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Proportion of Girls and Boys by Educational Level3.png",
        27 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Student population by sector.png",
        31 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Gender Proportions by Sector.png",
        39 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Total Number of Students in Urban vs. Rural Areas.png",
        44 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Proportion of Students in Public vs. Private Sector (Urban vs. Rural).png",
        50 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Aggregated Distribution of LV1 Language Students by Region.png",
        53 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Aggregated Distribution of LV1 (Spanish, German, and Other Languages) Students by Region.png",
        58 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Aggregated Distribution of LV2 Language Students by Region.png",
        61 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Aggregated Distribution of LV2 (English, German, Italian and Other Languages) Students by Region.png",
        65 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\map Total Other LV1 Languages.png",
        68 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\map Total Other LV2 Languages.png",
        72 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Evolution of LV1 Language Enrollment by Educational Level.png",
        74 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Evolution of LV1 Language Enrollment by Educational Level2.png",
        77 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Evolution of LV2 Language Enrollment by Educational Level.png",
        79 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Evolution of LV2 Language Enrollment by Educational Level2.png",
        82 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Evolution of LV1 Language Choices Over the Years.png",
        83 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Evolution of LV1 Language Choices Over the Years (Log Scale).png",
        85 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Evolution of LV1 Language Choices Over the Years2.png",
        88 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Evolution of LV2 Language Choices Over the Years.png",
        89 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Evolution of LV2 Language Choices Over the Years (Log Scale).png",
        91 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Evolution of LV2 Language Choices Over the Years2.png",
        94 : "C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\screens\Language Combinations (LV1 to LV2).png"
    }
    afficher_notebook_avec_images("C:\Scolarité\Efrei\M1\DATAVIZ\Portfolio\Project dataviz.ipynb", image_map_lyceens)

# "Projet 3 : Uber"
elif nav == "Projet 3 : Uber":
    st.header("Projet 3 : Analyse des données Uber")
    st.markdown("Ce projet analyse les trajets Uber à New York pour détecter des tendances temporelles et géographiques.")
    
    # Afficher le notebook (ajuste le chemin vers le notebook et les images si nécessaire)
    image_map_uber = {
        # Ajouter des images si nécessaire
    }
    afficher_notebook_avec_images("C:\\Scolarité\\Efrei\\M1\\Uber\\Uber_project.ipynb", image_map_uber)
