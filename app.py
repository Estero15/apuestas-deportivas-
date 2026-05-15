import streamlit as st
import pandas as pd

# ⚙️ CONFIGURACIÓN
st.set_page_config(
    page_title="Apuestas Deportivas | Fútbol",
    page_icon="⚽",
    layout="wide"
)

# 🎨 TÍTULO PRINCIPAL
st.title("⚽ Sistema de Pronósticos y Apuestas Deportivas")
st.markdown("---")

# 📌 MENÚ DE LIGAS Y TORNEOS
ligas = [
    "🇲🇽 Liga MX",
    "🇩🇪 Bundesliga",
    "🇫🇷 Liga Francesa (Ligue 1)",
    "🇮🇹 Liga Italiana (Serie A)",
    "🏆 UEFA Champions League",
    "🌎 Mundial de Fútbol 2026",
    "🇺🇸 MLS (Major League Soccer)"
]

liga_seleccionada = st.selectbox("📋 Selecciona la Liga o Torneo:", ligas)
st.subheader(f"✅ Mostrando partidos: {liga_seleccionada}")
st.markdown("---")

# 📋 DATOS DE PARTIDOS Y CUOTAS
datos = pd.DataFrame({
    'Partido': [
        "Chivas vs América", "Bayern vs Dortmund", "PSG vs Olympique",
        "Inter vs Juventus", "Real Madrid vs Arsenal",
        "México vs Estados Unidos", "LA Galaxy vs Inter Miami"
    ],
    'Fecha': [
        "18 Mayo 2026", "18 Mayo 2026", "19 Mayo 2026",
        "19 Mayo 2026", "20 Mayo 2026",
        "21 Jun 2026", "22 Mayo 2026"
    ],
    'Cuota Local': [1.90, 1.75, 1.60, 2.05, 1.85, 2.10, 1.70],
    'Cuota Empate': [3.30, 3.60, 3.80, 3.25, 3.40, 3.50, 3.70],
    'Cuota Visita': [3.90, 4.10, 4.50, 3.70, 4.00, 3.40, 4.20]
})

st.dataframe(datos, use_container_width=True)

# 🧮 CALCULADORA DE GANANCIAS
st.header("🧮 Calculadora de Apuesta")

monto = st.number_input("💰 Monto a apostar ($):", min_value=0.0, step=10.0)
cuota_elegida = st.number_input("📊 Ingresa la cuota:", min_value=1.0, step=0.05)

if st.button("💵 Calcular Ganancia"):
    if monto > 0 and cuota_elegida > 1:
        total = round(monto * cuota_elegida, 2)
        ganancia_neta = round(total - monto, 2)
        st.success(f"""
        ✅ Pago total: **${total}**
        📈 Ganancia neta: **${ganancia_neta}**
        """)
    else:
        st.error("⚠️ Ingresa valores correctos")

# 📊 ESTADÍSTICAS
st.header("📊 Estadísticas de Equipos")
estadisticas = pd.DataFrame({
    'Equipo': ["América", "Bayern", "PSG", "Juventus", "México", "Inter Miami"],
    'Partidos Ganados': [14, 18, 16, 12, 11, 9],
    'Goles Promedio': [2.1, 2.8, 2.5, 1.7, 1.9, 2.2]
})

st.bar_chart(estadisticas, x="Equipo", y="Partidos Ganados", color="#2ECC71")

st.markdown("---")
st.info("📌 Versión completa con todas tus ligas solicitadas 🚀")