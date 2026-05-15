import streamlit as st
import pandas as pd
import random
from datetime import datetime

# ⚙️ CONFIGURACIÓN
st.set_page_config(
    page_title="Calendario Fútbol | 14 Mayo 2026",
    page_icon="📅",
    layout="wide"
)

# 🎨 ESTILO
st.markdown("""
<style>
.titulo-seccion {font-size:18px; font-weight:bold; color:#2C3E50;}
.fecha {color:#27AE60; font-weight:bold;}
.hora {color:#2980B9; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# 🎉 TÍTULO
st.title("📅 CALENDARIO DE PARTIDOS - 14 DE MAYO 2026")
st.markdown("<p class='fecha'>🗓️ Fecha actual: Jueves 14 de Mayo de 2026</p>", unsafe_allow_html=True)
st.markdown("---")

# 📋 MENÚ DE LIGAS
ligas = [
    "🇲🇽 Liga MX | SEMIFINALES",
    "🇩🇪 Bundesliga",
    "🇫🇷 Liga Francesa (Ligue 1)",
    "🇮🇹 Liga Italiana (Serie A)",
    "🏆 UEFA Champions League",
    "🌎 Mundial Fútbol 2026",
    "🇺🇸 MLS"
]
liga_seleccionada = st.selectbox("🔽 Selecciona Torneo / Liga:", ligas)
st.subheader(f"✅ Mostrando: {liga_seleccionada}")
st.markdown("---")

# 📆 PARTIDOS CON FECHA Y HORA (ACTUALIZADO AL 14 MAYO 2026)
calendario = {
    "🇲🇽 Liga MX | SEMIFINALES": [
        {"partido": "Tigres 🆚 Santos", "fecha": "14 Mayo 2026", "hora": "19:00 hrs"},
        {"partido": "América 🆚 Cruz Azul", "fecha": "14 Mayo 2026", "hora": "21:00 hrs"},
        {"partido": "Santos 🆚 Tigres", "fecha": "17 Mayo 2026", "hora": "19:00 hrs"},
        {"partido": "Cruz Azul 🆚 América", "fecha": "17 Mayo 2026", "hora": "21:00 hrs"}
    ],
    "🇩🇪 Bundesliga": [
        {"partido": "Bayern Munich 🆚 Borussia Dortmund", "fecha": "15 Mayo 2026", "hora": "13:30 hrs"},
        {"partido": "Bayer Leverkusen 🆚 RB Leipzig", "fecha": "15 Mayo 2026", "hora": "16:30 hrs"},
        {"partido": "Frankfurt 🆚 Mönchengladbach", "fecha": "16 Mayo 2026", "hora": "14:00 hrs"}
    ],
    "🇫🇷 Liga Francesa (Ligue 1)": [
        {"partido": "PSG 🆚 Olympique Lyon", "fecha": "15 Mayo 2026", "hora": "14:00 hrs"},
        {"partido": "Mónaco 🆚 Marsella", "fecha": "15 Mayo 2026", "hora": "17:00 hrs"},
        {"partido": "Lille 🆚 Niza", "fecha": "16 Mayo 2026", "hora": "12:00 hrs"}
    ],
    "🇮🇹 Liga Italiana (Serie A)": [
        {"partido": "Inter de Milán 🆚 Juventus", "fecha": "14 Mayo 2026", "hora": "15:45 hrs"},
        {"partido": "Napoli 🆚 AC Milan", "fecha": "15 Mayo 2026", "hora": "18:00 hrs"},
        {"partido": "Roma 🆚 Atalanta", "fecha": "16 Mayo 2026", "hora": "16:00 hrs"}
    ],
    "🏆 UEFA Champions League": [
        {"partido": "Real Madrid 🆚 Arsenal", "fecha": "16 Mayo 2026", "hora": "20:00 hrs"},
        {"partido": "Manchester City 🆚 PSG", "fecha": "17 Mayo 2026", "hora": "20:00 hrs"}
    ],
    "🌎 Mundial Fútbol 2026": [
        {"partido": "México 🆚 Estados Unidos", "fecha": "11 Junio 2026", "hora": "19:00 hrs"},
        {"partido": "Argentina 🆚 Francia", "fecha": "12 Junio 2026", "hora": "21:00 hrs"},
        {"partido": "Brasil 🆚 España", "fecha": "13 Junio 2026", "hora": "18:00 hrs"}
    ],
    "🇺🇸 MLS": [
        {"partido": "Inter Miami 🆚 LA Galaxy", "fecha": "14 Mayo 2026", "hora": "20:30 hrs"},
        {"partido": "NYC FC 🆚 Seattle Sounders", "fecha": "15 Mayo 2026", "hora": "19:30 hrs"},
        {"partido": "Atlanta United 🆚 Austin FC", "fecha": "16 Mayo 2026", "hora": "17:00 hrs"}
    ]
}

# 📋 MOSTRAR TABLA DE PARTIDOS
df_calendario = pd.DataFrame(calendario[liga_seleccionada])
st.dataframe(df_calendario, use_container_width=True, hide_index=True)

# 🧠 FUNCIÓN PREDICCIÓN (Ganador + Goles)
def predecir_partido(equipo1, equipo2):
    fuerza = {
        "Tigres":80, "Santos":74, "América":82, "Cruz Azul":76,
        "Bayern":91, "Dortmund":85, "PSG":88, "Lyon":79,
        "Inter":87, "Juventus":83, "Real Madrid":89, "Arsenal":84,
        "México":79, "Estados Unidos":76, "Argentina":92, "Francia":90,
        "Brasil":93, "España":88, "Inter Miami":77, "LA Galaxy":73
    }

    f1 = fuerza.get(equipo1.split(" ")[0], 70)
    f2 = fuerza.get(equipo2.split(" ")[0], 70)

    # Probabilidades
    prob_local = round(f1/(f1+f2)*100, 1)
    prob_empate = round((100 - abs(f1-f2))/4, 1)
    prob_visita = round(f2/(f1+f2)*100, 1)

    # Goles estimados
    g1 = round(random.uniform(0.7, 3.0) * (f1/100))
    g2 = round(random.uniform(0.5, 2.7) * (f2/100))

    # Resultado
    if g1 > g2:
        ganador = f"✅ GANA: {equipo1.split(' ')[0]}"
    elif g2 > g1:
        ganador = f"✅ GANA: {equipo2.split(' ')[0]}"
    else:
        ganador = "🤝 EMPATE"

    total_goles = g1 + g2
    marcador = f"{g1} - {g2}"

    return ganador, marcador, total_goles, prob_local, prob_empate, prob_visita

# 🔮 SELECCIONAR Y PREDECIR
st.markdown("---")
st.subheader("🔎 ELIGE PARTIDO PARA VER PRONÓSTICO")
lista_partidos = [p["partido"] for p in calendario[liga_seleccionada]]
partido_elegido = st.selectbox("📌 Partido:", lista_partidos)

if st.button("⚽ VER QUIÉN GANA Y GOLES", use_container_width=True):
    eq1, eq2 = partido_elegido.split(" 🆚 ")
    ganador, marcador, goles_totales, pl, pe, pv = predecir_partido(eq1, eq2)

    st.markdown("---")
    st.header("📊 RESULTADO PRONOSTICADO")
    st.success(f"🏆 {ganador}")
    st.info(f"📌 MARCADOR FINAL: {marcador}")
    st.warning(f"⚽ GOLES TOTALES: {goles_totales} goles en el partido")

    col1, col2, col3 = st.columns(3)
    with col1: st.metric("🔵 Local", f"{pl} %")
    with col2: st.metric("⚪ Empate", f"{pe} %")
    with col3: st.metric("🔴 Visita", f"{pv} %")

# 🧮 CALCULADORA DE APUESTA
st.markdown("---")
st.header("🧮 CALCULA TU GANANCIA")
monto = st.number_input("💰 Monto ($):", min_value=0.0)
cuota = st.number_input("📊 Cuota:", min_value=1.1)
if st.button("💵 CALCULAR GANANCIA"):
    ganancia = round(monto * cuota, 2)
    neta = round(ganancia - monto, 2)
    st.success(f"✅ Recibes: ${ganancia} | Ganancia neta: ${neta}")

st.markdown("---")
st.caption("📌 Calendario actualizado al 14 de Mayo de 2026 | Incluye Semifinales Liga MX ✅")