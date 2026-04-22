import streamlit as st

# Esta configuracion oculta el menu, el pie de pagina y los botones de sistema
st.set_page_config(page_title="Calculadora UTEG", layout="centered")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    #stDecoration {display:none;}
    
    /* Quitar el espacio superior innecesario */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
    }
    
    /* Estilo de consola para los resultados */
    pre {
        background-color: #f0f2f6 !important;
        color: #1e1e1e !important;
        border: 1px solid #d1d1d1 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado simple
st.text("=====================================")
st.text(" CALCULADORA CALORIAS UTEG")
st.text("=====================================")

# Entradas de datos
peso = st.number_input("Peso (kg):", min_value=1.0, value=70.0)
edad = st.number_input("Edad:", min_value=1, value=25)
altura = st.number_input("Altura (cm):", min_value=1.0, value=170.0)
cintura = st.number_input("Medida de cintura (cm):", min_value=1.0, value=80.0)
sexo_label = st.selectbox("Sexo:", ["Hombre", "Mujer"])

if st.button("CALCULAR RESULTADOS"):
    # Lógica de cálculos
    sexo = 1 if sexo_label == "Hombre" else 2
    altura_m = altura / 100
    imc = peso / (altura_m ** 2)
    
    if imc < 18.5: clasificacion = "Bajo peso"
    elif imc < 25: clasificacion = "Peso normal"
    elif imc < 30: clasificacion = "Sobrepeso"
    else: clasificacion = "Obesidad"

    peso_ideal = 22 * (altura_m ** 2)
    bajar = peso - peso_ideal

    if sexo == 1:
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * edad)
    else:
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * edad)

    cal_mant = tmb * 1.2
    cal_bajar = cal_mant - 400

    # Bloque de salida estilo 'print'
    output = f"""
========== RESULTADOS ==========

IMC: {imc:.2f}
Clasificacion: {clasificacion}
"""
    if bajar > 0:
        output += f"Debes bajar aproximadamente: {bajar:.2f} kg\n"
    else:
        output += "Tu peso esta dentro del rango saludable\n"

    output += f"""
Peso ideal estimado: {peso_ideal:.2f} kg

Calorias:
Mantenimiento: {cal_mant:.0f} kcal/dia
Para bajar peso: {cal_bajar:.0f} kcal/dia

Evaluacion de cintura:
"""
    if (sexo == 1 and cintura > 102) or (sexo == 2 and cintura > 88):
        output += "Riesgo alto - Se recomienda reducir cintura\n"
    else:
        output += "Nivel de cintura saludable\n"

    output += "====================================="
    
    # Mostrar como bloque de codigo para mantener formato de consola
    st.code(output, language=None)
    st.text(" RESULTADO GENERADO POR UTEG")
