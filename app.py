import streamlit as st

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="The Waffle Bar",
    page_icon="🧇",
    layout="wide"
)

# ---------------- LOAD CSS ---------------- #
with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Hide Streamlit default menu
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------- NAVBAR ---------------- #

col1, col2, col3 = st.columns([2,5,2])

with col1:
    st.markdown("<h2 class='logo'>🧇 The Waffle Bar</h2>", unsafe_allow_html=True)

with col2:
    st.markdown(
        """
        <div class='nav'>
        🏠 Home &nbsp;&nbsp;&nbsp;
        📖 Menu &nbsp;&nbsp;&nbsp;
        ☕ About &nbsp;&nbsp;&nbsp;
        📞 Contact
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.button("👤 Login")
    st.button("📝 Register")

st.divider()

# ---------------- HERO SECTION ---------------- #

st.markdown(
"""
<div class="hero">

# 🍫 Freshly Crafted Waffles

### Every Bite Tells A Sweet Story ❤️

Welcome to **The Waffle Bar**, where delicious waffles are made fresh every day.

</div>
""",
unsafe_allow_html=True
)

st.write("")

center = st.columns([2,1,2])

with center[1]:
    st.button("🧇 Explore Menu", use_container_width=True)

st.write("")
st.write("")

# ---------------- POPULAR WAFFLES ---------------- #

st.markdown("## ⭐ Popular Waffles")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class='card'>
    <h3>🧇 Belgian Waffle</h3>
    <p>Golden Crispy</p>
    <h4>₹120</h4>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card'>
    <h3>🍫 Nutella Waffle</h3>
    <p>Chocolate Loaded</p>
    <h4>₹180</h4>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='card'>
    <h3>🍓 Strawberry Waffle</h3>
    <p>Fresh Fruits</p>
    <h4>₹170</h4>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- ABOUT ---------------- #

st.markdown("""
<div class="about">

## ☕ About Us

The Waffle Bar is dedicated to serving premium waffles with
fresh ingredients, delicious toppings, and lots of love.

</div>
""", unsafe_allow_html=True)

st.write("")
st.divider()

# ---------------- FOOTER ---------------- #

st.markdown("""
<div class="footer">

### 🧇 The Waffle Bar

📍 Rajkot, Gujarat

📞 +91 9876543210

❤️ Fresh Waffles | Fresh Happiness

© 2026 The Waffle Bar

</div>
""", unsafe_allow_html=True)