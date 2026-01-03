import streamlit as st
import random

st.set_page_config(page_title="Test de Talents Inconscients", layout="centered")
st.title("🎯 Test de Talents Inconscients")
st.write("Ce test explore vos forces profondes à travers des images et des réactions spontanées.")

# Phase 1 : Image projective
st.header("Étape 1 : Choisissez l'image qui vous attire le plus")

images = {
    "forêt": "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
    "ville": "https://images.unsplash.com/photo-1461716836226-2c9bcdc69a24",
    "océan": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "montagne": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
    "désert": "https://images.unsplash.com/photo-1583337130417-3346a1be7dee"
}

selected_image = st.radio("Quelle image vous attire intuitivement ?", list(images.keys()))
st.image(images[selected_image], use_column_width=True)

# Phase 2 : Réaction spontanée
st.header("Étape 2 : Choix spontané")
choice = st.radio("Si vous pouviez tout faire demain, que choisiriez-vous ?", [
    "Créer un projet de A à Z",
    "Explorer un lieu inconnu",
    "Aider quelqu'un à transformer sa vie",
    "Inventer un concept inédit",
    "Rassembler des personnes autour d'une vision"
])

# Phase 3 : Mini questionnaire
st.header("Étape 3 : Vous concernant")
q1 = st.slider("Je préfère improviser plutôt que planifier à l'avance", 1, 5, 3)
q2 = st.slider("Je ressens facilement l'ambiance d'un groupe", 1, 5, 3)
q3 = st.slider("Je m'adapte très vite aux imprévus", 1, 5, 3)
q4 = st.slider("Je suis plus à l'aise dans la création que dans l'exécution", 1, 5, 3)
q5 = st.slider("Je réfléchis souvent à des alternatives aux méthodes classiques", 1, 5, 3)

# Soumission
if st.button("Analyser mes résultats"):
    score_creatif = (q1 + q4 + q5) / 3
    score_empathique = (q2 + q3) / 2
    st.subheader("🧠 Résultat")
    if score_creatif >= 4:
        st.write("✨ Vous avez un profil de **créateur stratégique** : vos idées sortent du cadre.")
    elif score_empathique >= 4:
        st.write("💡 Vous êtes un **facilitateur empathique** : vous percevez les besoins implicites des autres.")
    else:
        st.write("🔍 Vous êtes un **explorateur adaptable** : vous testez, ajustez, progressez en mouvement.")

    st.info("Ce test donne une tendance. Une discussion avec un coach peut enrichir la lecture.")
