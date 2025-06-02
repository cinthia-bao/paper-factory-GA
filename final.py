import streamlit as st

st.title("📄 Producción de Papel")

# Entradas del usuario
dias = st.number_input("Días de producción", min_value=1, value=5)
toneladas_por_dia = st.number_input("Toneladas por día", min_value=0.1, value=1.0)

st.subheader("📊 Porcentaje por tipo de color")
color_0 = st.slider("Color 0 (%)", 0, 100, 30)
color_1 = st.slider("Color 1 (%)", 0, 100, 50)
color_2 = st.slider("Color 2 (%)", 0, 100, 20)

st.subheader("📏 Porcentaje por grosor")
grosor_1 = st.slider("Grosor 1 (%)", 0, 100, 60)
grosor_2 = st.slider("Grosor 2 (%)", 0, 100, 40)

# Validación de porcentajes
if color_0 + color_1 + color_2 != 100 or grosor_1 + grosor_2 != 100:
    st.error("⚠️ Los porcentajes deben sumar 100% en cada categoría.")
else:
    if st.button("Calcular producción"):
        total_toneladas = dias * toneladas_por_dia
        st.success(f"✅ Producción total: {total_toneladas:.2f} toneladas")

        st.write("### 🧾 Distribución por color:")
        st.write(f"Color 0: {total_toneladas * color_0 / 100:.2f} toneladas")
        st.write(f"Color 1: {total_toneladas * color_1 / 100:.2f} toneladas")
        st.write(f"Color 2: {total_toneladas * color_2 / 100:.2f} toneladas")

        st.write("### 📏 Distribución por grosor:")
        st.write(f"Grosor 1: {total_toneladas * grosor_1 / 100:.2f} toneladas")
        st.write(f"Grosor 2: {total_toneladas * grosor_2 / 100:.2f} toneladas")

