import streamlit as st
from datetime import datetime

# ----------- CONFIGURACIÓN GENERAL -----------
st.set_page_config(page_title="Clasificación Triage", page_icon="🩺", layout="centered")

st.markdown("""
    <style>
    .title {
        font-size:40px !important;
        color:#004d99;
        font-weight: bold;
        text-align: center;
    }
    .sub {
        font-size:18px;
        color:#444;
        text-align: center;
    }
    .stButton > button {
        background-color: #004d99;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ----------- TÍTULO Y DESCRIPCIÓN -----------
st.markdown('<div class="title">🩺 Sistema de Clasificación Triage</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Determina el nivel de atención médica que requiere un paciente según sus síntomas clínicos.</div><br>', unsafe_allow_html=True)

# ----------- FORMULARIO DE ENTRADA -----------
with st.form("formulario_triage"):
    st.header("📝 Datos del Paciente")
    col1, col2 = st.columns(2)

    with col1:
        frecuencia_cardiaca = st.number_input("❤️ Frecuencia cardíaca (latidos/min)", min_value=0, value=80)
        frecuencia_respiratoria = st.number_input("💨 Frecuencia respiratoria (respiraciones/min)", min_value=0, value=16)
        saturacion_oxigeno = st.slider("🫁 Saturación de oxígeno (%)", 50, 100, 97)
    
    with col2:
        temperatura_corporal = st.number_input("🌡️ Temperatura corporal (°C)", value=36.5)
        nivel_dolor = st.slider("🤕 Nivel de dolor (0 = sin dolor, 10 = máximo)", 0, 10, 3)

    st.markdown("### Síntomas adicionales")
    col3, col4 = st.columns(2)
    with col3:
        heridas_graves = st.checkbox("🩸 Heridas graves o sangrado")
        infeccion_severa = st.checkbox("🔥 Infección severa (fiebre alta, septicemia)")
    with col4:
        dificultad_respiratoria = st.checkbox("😮‍💨 Dificultad respiratoria")
        estado_mental = st.selectbox("🧠 Estado mental", ["Alerta", "Letárgico", "Inconsciente"])

    enviar = st.form_submit_button("🔍 Evaluar Nivel de Triage")

# ----------- LÓGICA DE TRIAGE -----------
if enviar:
    nivel_triage = 5
    recomendacion = "El paciente no requiere atención urgente, pero debe seguir un tratamiento adecuado."

    if (
        frecuencia_cardiaca > 130 or
        frecuencia_respiratoria > 40 or
        saturacion_oxigeno < 85 or
        temperatura_corporal > 40 or
        dificultad_respiratoria or
        estado_mental == "Inconsciente"
    ):
        nivel_triage = 1
        recomendacion = "¡El paciente requiere atención inmediata en una sala de urgencias!"

    elif (
        110 <= frecuencia_cardiaca <= 130 or
        30 <= frecuencia_respiratoria <= 40 or
        85 <= saturacion_oxigeno <= 90 or
        39 <= temperatura_corporal <= 40 or
        heridas_graves or
        estado_mental == "Letárgico"
    ):
        nivel_triage = 2
        recomendacion = "El paciente debe recibir atención en menos de 30 minutos."

    elif (
        100 <= frecuencia_cardiaca < 110 or
        21 <= frecuencia_respiratoria < 30 or
        91 <= saturacion_oxigeno <= 94 or
        nivel_dolor >= 7 or
        infeccion_severa
    ):
        nivel_triage = 3
        recomendacion = "El paciente requiere atención urgente en las próximas horas."

    elif (
        95 <= frecuencia_cardiaca < 100 or
        16 <= frecuencia_respiratoria <= 20 or
        95 <= saturacion_oxigeno <= 97 or
        37.5 <= temperatura_corporal < 39 or
        nivel_dolor >= 4
    ):
        nivel_triage = 4
        recomendacion = "El paciente puede esperar atención, pero debe ser evaluado."

    # ----------- RESULTADOS -----------
    st.markdown("---")
    st.header(f"🔎 Nivel de Triage: {nivel_triage}")

    if nivel_triage == 1:
        st.error(recomendacion)
    elif nivel_triage == 2:
        st.warning(recomendacion)
    elif nivel_triage == 3:
        st.info(recomendacion)
    elif nivel_triage == 4:
        st.info(recomendacion)
    elif nivel_triage == 5:
        st.success(recomendacion)

    # ----------- RESUMEN -----------
    st.markdown("### 📋 Resumen del paciente:")
    st.markdown(f"- Frecuencia cardíaca: {frecuencia_cardiaca} latidos/min")
    st.markdown(f"- Frecuencia respiratoria: {frecuencia_respiratoria} respiraciones/min")
    st.markdown(f"- Saturación de oxígeno: {saturacion_oxigeno}%")
    st.markdown(f"- Temperatura corporal: {temperatura_corporal} °C")
    st.markdown(f"- Nivel de dolor: {nivel_dolor}/10")
    st.markdown(f"- Estado mental: {estado_mental}")
    st.markdown(f"- Heridas graves: {'Sí' if heridas_graves else 'No'}")
    st.markdown(f"- Infección severa: {'Sí' if infeccion_severa else 'No'}")
    st.markdown(f"- Dificultad respiratoria: {'Sí' if dificultad_respiratoria else 'No'}")