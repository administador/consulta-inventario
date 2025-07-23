as
import streamlit as st
import pandas as pd

# Configuración de página
st.set_page_config(page_title="Consulta de Inventario", layout="centered")

st.title("🔒 Consulta de Inventario")
st.caption("Ingrese la contraseña para acceder a la app.")

# Campo de contraseña
password = st.text_input("Contraseña", type="password")

# Contraseña esperada (puedes cambiarla aquí)
correct_password = "inventario2025"

if password != correct_password:
    st.warning("Debe ingresar la contraseña correcta para continuar.")
    st.stop()

st.success("✅ Acceso concedido")
st.caption("Ingrese el código del producto para ver el detalle y saldo disponible.")

# Enlace al archivo en Dropbox (modo directo)
dropbox_url = "https://www.dropbox.com/scl/fi/0tulypcrt0kgc7ydxwp5c/Inventarioventas.xlsx?rlkey=wnq9i8m6532gnbs4lv61ee5l8&st=jebvl180&dl=1"

# Entrada de usuario
codigo_input = st.text_input("Código del producto", placeholder="Ej. 401-0036")

# Cargar el archivo desde Dropbox cuando se presione el botón
if st.button("Buscar"):
    try:
        df = pd.read_excel(dropbox_url, sheet_name="Inv 2025", skiprows=5)
        df.columns = ['CODIGO', 'CD', 'DETALLE', 'Saldo Anterior', 'Entradas', 'Salidas', 'Saldo Actual', 'PROD']
        df = df[df['CODIGO'].notna() & df['DETALLE'].notna()]

        resultado = df[df['CODIGO'].astype(str) == codigo_input.strip()]
        if not resultado.empty:
            detalle = resultado.iloc[0]['DETALLE']
            saldo = resultado.iloc[0]['Saldo Actual']
            st.success(f"🧾 Detalle: {detalle}\n💼 Saldo Actual: {saldo}")
        else:
            st.warning("❌ Código no encontrado en el inventario.")
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
