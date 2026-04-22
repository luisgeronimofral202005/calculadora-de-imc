import streamlit as st

# Configuracion de la pagina
st.set_page_config(page_title="Calculadora Calorias UTEG", layout="centered")

# Estilo profesional con CSS
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #1a3a5a;
        color: white;
        font-weight: bold;
        border: none;
    }
    div[data-testid="stMetricValue"] {
        font-size: 28px;
        color: #1a3a5a;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("CALCULADORA CALORIAS UTEG")
st.markdown("---")
st.write("Analisis antropometrico y requerimientos energeticos.")

# Formulario de entrada de datos
col1, col2 = st.columns(2)

with col1:
    peso = st.number_input("Peso actual (kg):", min_value=1.0, value=70.0, step=0.1)
    edad = st.number_input("Edad (años):", min_value=1, max_value=120, value=25, step=1)
    sexo = st.selectbox("Sexo:", ["Hombre", "Mujer"])

with col2:
    altura = st.number_input("Altura (cm):", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
    cintura = st.number_input("Circunferencia de cintura (cm):", min_value=20.0, value=80.0, step=0.1)

st.markdown(" ")

if st.button("PROCESAR ANALISIS"):
    # CALCULOS TECNICOS
    altura_m = altura / 100
    imc = peso / (altura_m ** 2)
    
    # Clasificacion IMC
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif imc < 25:
        clasificacion = "Peso normal"
    elif imc < 30:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"

    # Peso Ideal (IMC 22 como referencia)
    peso_ideal = 22 * (altura_m ** 2)
    diferencia_peso = peso - peso_ideal

    # Tasa Metabolica Basal (Harris-Benedict)
    if sexo == "Hombre":
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * edad)
        riesgo_cintura = cintura > 102
    else:
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * edad)
        riesgo_cintura = cintura > 88

    # Calorias de mantenimiento (Actividad ligera x1.2)
    cal_mant = tmb * 1.2
    cal_bajar = cal_mant - 400

    # SECCION DE RESULTADOS
    st.markdown("---")
    st.subheader("RESULTADOS DEL ANALISIS")
    
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        st.metric("IMC", f"{imc:.2f}")
        st.write(f"Estado: **{clasificacion}**")
        st.write(f"Peso Ideal: **{peso_ideal:.2f} kg**")

    with res_col2:
        st.write("**Metas Diarias:**")
        st.info(f"Mantenimiento: {cal_mant:.0f} kcal")
        st.success(f"Objetivo Perdida: {cal_bajar:.0f} kcal")

    st.markdown(" ")
    
    # EVALUACION DE SALUD
    if diferencia_peso > 0:
        st.warning(f"Diferencia respecto al peso ideal: {diferencia_peso:.2f} kg")
    else:
        st.info("Su peso actual se encuentra en rangos saludables.")

    if riesgo_cintura:
        st.error("Alerta: Perimetro de cintura fuera de rango saludable.")
    else:
        st.success("Perimetro de cintura dentro de rangos normales.")

    st.markdown("---")
    st.caption("SISTEMA GENERADO POR UTEG ")
