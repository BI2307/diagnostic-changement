import streamlit as st

st.set_page_config(page_title="Diagnostic de Résistance au Changement", layout="centered")

st.title("🧭 Diagnostic de Résistance au Changement")
st.write("Répondez aux 5 questions suivantes pour évaluer la posture face au changement.")

questions = {
    "comprehension": "Je comprends les raisons du changement.",
    "confiance": "J'ai confiance dans les porteurs du changement.",
    "implication": "Je me sens impliqué(e) dans ce processus.",
    "competence": "Je me sens capable de faire face aux nouvelles exigences.",
    "emotions": "Je ressens positivement ce changement."
}

scores = {}
with st.form("diagnostic_form"):
    for key, question in questions.items():
        scores[key] = st.slider(question, 1, 5, 3)
    submitted = st.form_submit_button("Analyser")

if submitted:
    moyenne = sum(scores.values()) / len(scores)
    st.subheader("Résultat")
    st.write(f"Score moyen : {moyenne:.2f}/5")

    if moyenne >= 4:
        st.success("🌟 Très bon niveau d'engagement.")
    elif moyenne >= 3:
        st.warning("⚠️ Résistance modérée détectée.")
    else:
        st.error("🚨 Forte résistance. Un accompagnement est conseillé.")
