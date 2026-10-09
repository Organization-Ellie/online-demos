import base64
from pathlib import Path
import streamlit as st

import seccion_voz
ROOT = Path(__file__).parent
VIDEO_URL = "https://www.youtube.com/watch?v=ex0WYnK_UDY"  # Video del prototipo (Anexo 6 de la tesina)

st.set_page_config(
    page_title="Ellie · Compañía inteligente para personas mayores",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Estilo

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Young+Serif&display=swap');

:root {
  --ink: #1F3D36; --deep: #3F7D6B; --sage: #8DB5A0; --mist: #E2EDE6;
  --paper: #F3F7F4; --sun: #F5DFA6; --lilac: #C9B8E4;
}
html { scroll-behavior: smooth; }

/* Ocultar la interfaz de Streamlit */
#MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"] { visibility: hidden; height: 0; }

.stApp { background: var(--paper); }
.block-container { max-width: 1040px; padding: 5.2rem 1.5rem 3rem 1.5rem; }

html, body, p, li, span, label, div { font-family: 'Atkinson Hyperlegible', sans-serif; color: var(--ink); }
p, li { font-size: 1.12rem; line-height: 1.75; }
h1, h2, h3, .serif { font-family: 'Young Serif', serif !important; font-weight: 400 !important; color: var(--ink); letter-spacing: -0.01em; }
h2 { font-size: 2.1rem !important; margin: 0 0 .4rem 0 !important; padding: 0 !important; }
h3 { font-size: 1.35rem !important; }

/* Menú fijo */
.nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 999;
  display: flex; align-items: center; gap: 1.6rem; flex-wrap: wrap;
  padding: .85rem max(1.5rem, calc((100vw - 1040px) / 2));
  background: rgba(243, 247, 244, .94); backdrop-filter: blur(8px);
  border-bottom: 1px solid #d3e2d9;
}
.nav .logo { font-family: 'Young Serif', serif; font-size: 1.6rem; margin-right: auto; color: var(--ink); }
.nav a { color: var(--ink) !important; text-decoration: none; font-size: 1.02rem; padding: .3rem 0; border-bottom: 2px solid transparent; }
.nav a:hover { border-bottom-color: var(--deep); }
.nav a:focus-visible { outline: 3px solid #A28FCB; outline-offset: 3px; }
.sec { scroll-margin-top: 90px; padding-top: 3rem; }

/* Portada */
.hero { display: flex; gap: 2.5rem; align-items: center; justify-content: space-between; flex-wrap: wrap;
  padding: 3rem 3rem; border-radius: 44px 44px 44px 10px;
  background: radial-gradient(circle at 94% 8%, var(--sun) 0, var(--sun) 80px, transparent 81px),
              radial-gradient(circle at 4% 108%, var(--lilac) 0, var(--lilac) 120px, transparent 121px), #CFE3D6; }
.hero .txt { flex: 1 1 340px; }
.hero h1 { font-size: 3.1rem; line-height: 1.12; margin: 0 0 1rem 0; }
.hero p { max-width: 32rem; margin: 0 0 1.6rem 0; font-size: 1.2rem; }
.btn { display: inline-block; padding: .85rem 1.7rem; border-radius: 999px; background: var(--ink); color: #fff !important;
  text-decoration: none; font-weight: 700; font-size: 1.05rem; }
.btn:hover { background: var(--deep); }
.btn:focus-visible { outline: 3px solid #A28FCB; outline-offset: 3px; }
.btn.soft { background: transparent; color: var(--ink) !important; border: 2px solid var(--ink); margin-left: .6rem; }
.btn.soft:hover { background: rgba(255,255,255,.5); }
.portrait { flex: 0 0 250px; height: 300px; border-radius: 125px 125px 28px 28px; overflow: hidden;
  background: #F8FBF9; border: 6px solid #fff; display: flex; align-items: center; justify-content: center; }
.portrait img { width: 100%; height: 100%; object-fit: cover; }
.portrait .ph { font-family: 'Young Serif', serif; font-size: 6rem; color: var(--sage); }

/* Qué es */
.lead { font-size: 1.35rem; line-height: 1.6; max-width: 46rem; }

/* Pilares */
.pilar { border-left: 5px solid var(--sage); padding: .1rem 0 .1rem 1.3rem; margin: 1.5rem 0; max-width: 44rem; }
.pilar.b { border-color: #E3B957; } .pilar.c { border-color: #A28FCB; }
.pilar b { display: block; font-family: 'Young Serif', serif; font-weight: 400; font-size: 1.4rem; margin-bottom: .15rem; }

/* Plataforma */
.plat { display: flex; gap: 3rem; flex-wrap: wrap; align-items: flex-start; margin-top: 1.5rem; }
.plat .col { flex: 1 1 380px; }
.tv { background: #26403a; padding: 14px 14px 22px 14px; border-radius: 18px; }
.tv .screen { background: #FBF3DE; border-radius: 8px; padding: 14px; display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.tv .face { grid-row: span 2; background: #CFE3D6; border-radius: 10px; display: flex; align-items: center; justify-content: center;
  font-family: 'Young Serif', serif; font-size: 3rem; color: var(--deep); min-height: 130px; }
.tv .opt { background: #fff; border-radius: 10px; padding: .8rem .4rem; text-align: center; font-weight: 700; font-size: .98rem; }
.phone { width: 210px; background: #26403a; padding: 12px; border-radius: 30px; margin-bottom: 1rem; }
.phone .screen { background: #fff; border-radius: 20px; padding: 1.1rem .9rem; text-align: center; min-height: 250px; }
.phone .screen b { font-family: 'Young Serif', serif; font-weight: 400; font-size: 1.1rem; display: block; margin-bottom: .8rem; }
.phone .pill { background: var(--deep); color: #fff; border-radius: 999px; padding: .45rem .6rem; margin: .5rem 0; font-size: .9rem; }
.phone .pill.alt { background: var(--mist); color: var(--ink); }
.cap { font-size: 1rem; margin-top: .8rem; }

/* Cuidadoras */
.band { background: #fff; border-radius: 32px; padding: 2rem 2.2rem; margin-top: 1.5rem; }
.bar { margin: 1.1rem 0; }
.bar .lbl { display: flex; justify-content: space-between; gap: 1rem; font-size: 1.05rem; }
.bar .lbl b { white-space: nowrap; }
.bar .track { height: 14px; background: var(--mist); border-radius: 999px; margin-top: .35rem; overflow: hidden; }
.bar .fill { height: 100%; background: var(--deep); border-radius: 999px; }
.note { font-size: .98rem; opacity: .85; margin-top: 1rem; }

/* Aviso IA y espacios del equipo */
.aviso { background: #F7EBC8; border-radius: 16px; padding: .85rem 1.2rem; font-size: 1rem; margin: 1rem 0; }
.foot { margin-top: 4rem; padding: 2rem 0 0 0; border-top: 1px solid #cfe0d6; font-size: .98rem; }
.foot p { font-size: .98rem; margin: .2rem 0; }

@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
@media (max-width: 700px) {
  .hero { padding: 2rem 1.4rem; } .hero h1 { font-size: 2.3rem; }
  .nav { gap: .9rem; } .nav a { font-size: .92rem; } .portrait { flex-basis: 100%; }
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# Utilidades

def img_b64(path: Path):
    if path.exists():
        mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
        return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()
    return None


def read_md(name: str) -> str:
    p = ROOT / "content" / name
    return p.read_text(encoding="utf-8") if p.exists() else "*Esta sección se llenará cuando el equipo agregue su archivo.*"


def show_outputs(folder: str):
    base = ROOT / "output" / folder
    if not base.exists():
        return
    for f in sorted(p for p in base.iterdir() if p.is_file() and p.name != ".gitkeep"):
        ext = f.suffix.lower()
        if ext in (".mp4", ".webm"):
            st.video(str(f))
        elif ext in (".wav", ".mp3", ".ogg", ".m4a"):
            st.audio(str(f))
        elif ext in (".png", ".jpg", ".jpeg", ".gif", ".webp"):
            st.image(str(f))


def bar(label: str, n: int, total: int = 7) -> str:
    pct = round(n / total * 100)
    return (f'<div class="bar"><div class="lbl"><span>{label}</span><b>{n} de {total}</b></div>'
            f'<div class="track"><div class="fill" style="width:{pct}%"></div></div></div>')


# Menú fijo

st.markdown(
    '<nav class="nav"><span class="logo">Ellie</span>'
    '<a href="#que-es" target="_self">Qué es</a>'
    '<a href="#ayuda" target="_self">Cómo ayuda</a>'
    '<a href="#plataforma" target="_self">Plataforma</a>'
    '<a href="#demo" target="_self">Demo</a>'
    '<a href="#cuidadoras" target="_self">Lo que aprendimos</a>'
    '<a href="#equipo" target="_self">Avances</a></nav>',
    unsafe_allow_html=True,
)

# Portada

avatar_src = img_b64(ROOT / "assets" / "avatar.png") or img_b64(ROOT / "assets" / "avatar.jpg")
portrait = f'<img src="{avatar_src}" alt="Avatar de Ellie">' if avatar_src else '<span class="ph">E</span>'

st.markdown(
    '<div class="hero"><div class="txt">'
    "<h1>Compañía cercana para quienes pasan el día solos</h1>"
    "<p>Ellie busca acompañar a personas mayores desde la televisión, con el rostro y la voz de alguien que quieren, "
    "y darle tranquilidad a quien las cuida.</p>"
    '<a class="btn" href="#demo" target="_self">Ver el prototipo</a>'
    '<a class="btn soft" href="#que-es" target="_self">Conocer más</a></div>'
    f'<div class="portrait">{portrait}</div></div>',
    unsafe_allow_html=True,
)

# Qué es

st.markdown(
    '<section class="sec" id="que-es"><h2>Qué es Ellie</h2>'
    '<p class="lead">Ellie es una propuesta de acompañamiento con inteligencia artificial para personas mayores que viven solas '
    "o pasan gran parte del día sin compañía. Se ve en la televisión, un aparato que ya conocen, y se configura desde el celular "
    "de quien las cuida.</p>"
    '<p class="lead">Su objetivo es tender un puente entre la persona mayor y su red de apoyo: que se sienta acompañada, '
    "que no olvide sus medicamentos y que su familia pueda saber cómo está.</p></section>",
    unsafe_allow_html=True,
)

# Cómo ayuda

st.markdown(
    '<section class="sec" id="ayuda"><h2>En qué puede ayudar</h2>'
    '<div class="pilar"><b>Un rostro conocido</b>Un gemelo digital de la persona cuidadora, con su imagen y su voz, '
    "para que la compañía se sienta familiar.</div>"
    '<div class="pilar b"><b>Medicamentos, citas y rutinas</b>Recordatorios que la cuidadora configura una vez '
    "y que se adaptan a cómo responde la persona mayor.</div>"
    '<div class="pilar c"><b>Atención al ánimo</b>Se proyecta que, a partir del tono de voz, Ellie pueda notar cambios y '
    "proponer una actividad. Es una señal de apoyo para quien cuida, no un diagnóstico.</div></section>",
    unsafe_allow_html=True,
)

# Plataforma

st.markdown(
    '<section class="sec" id="plataforma"><h2>Dos pantallas, una compañía</h2>'
    '<div class="plat">'
    '<div class="col"><div class="tv"><div class="screen">'
    '<div class="face">E</div><div class="opt">Recordatorios</div><div class="opt">Fotos</div>'
    '<div class="opt">Centro de actividades</div><div class="opt">Ayuda</div></div></div>'
    '<h3 style="margin-top:1rem">Para la persona mayor: televisión</h3>'
    '<p class="cap">Botones grandes, audio claro y comandos de voz simples o control remoto.</p></div>'
    '<div class="col"><div class="phone"><div class="screen"><b>Es hora de crear tu avatar</b>'
    '<div class="pill">Tomar foto</div><div class="pill">Grabar voz</div><div class="pill alt">Continuar</div></div></div>'
    '<h3>Para quien cuida: celular</h3>'
    '<p class="cap">Sube una foto y su voz, carga los recordatorios y las preferencias de la persona mayor.</p></div>'
    "</div></section>",
    unsafe_allow_html=True,
)


# Demo
st.markdown('<section class="sec" id="demo"><h2>El prototipo en video</h2>'
            "<p>Así se ve el primer prototipo: la cuidadora crea el avatar y la persona mayor lo encuentra en la televisión. "
            "El avatar de esta versión tiene estilo de dibujo.</p></section>", unsafe_allow_html=True)
st.video(VIDEO_URL)
st.markdown('<div class="aviso">El avatar y la voz de Ellie se generan con inteligencia artificial. No son la persona real.</div>',
            unsafe_allow_html=True)

# Lo que aprendimos
st.markdown(
    '<section class="sec" id="cuidadoras"><h2>Lo que nos contaron las cuidadoras</h2>'
    "<p>Conversamos con 8 cuidadoras en el Centro de Vida Saludable de la Universidad de Concepción. "
    "Siete respondieron un cuestionario.</p>"
    '<div class="band">'
    + bar("La persona mayor olvida medicamentos o rutinas", 5)
    + bar("Necesita apoyo para usar dispositivos", 5)
    + bar("Cree que una solución así aliviaría su carga", 5)
    + bar("Valora el efecto en la calidad de vida de la persona mayor", 6)
    + '<p class="note">Es una muestra pequeña y solo de mujeres, así que son una primera señal y no una conclusión. '
    "Aún no probamos Ellie con personas mayores: es el siguiente paso.</p></div></section>",
    unsafe_allow_html=True,
)


# Avances del equipo
st.markdown('<section class="sec" id="equipo"><h2>Avances del equipo</h2>'
            "<p>Trabajo del equipo  "
           # "en <code>output/</code>.</p></section>"
            , unsafe_allow_html=True)

for titulo, archivo, carpeta in [
    ("Avatar", "avatar.md", "avatar"),
    ("Voz", "voz.md", "voz"),
    ("Conversación, recordatorios y ánimo", "motor.md", "motor"),
]:
    with st.expander(titulo):
        st.markdown(read_md(archivo))
        show_outputs(carpeta)

with st.expander("Emoción en la voz (resultado preliminar)"):
    seccion_voz.mostrar()
    
# Pie

st.markdown(
    '<div class="foot"><p><b>Ellie</b> es un proyecto de innovación en etapa conceptual, aún no es un producto disponible.</p>'
    "<p> Universidad de Concepción. </p></div>",
    unsafe_allow_html=True,
)

