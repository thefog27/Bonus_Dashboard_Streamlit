import streamlit as st


st.set_page_config(layout="wide")


logo = st.secrets['logo']

st.logo(logo)
st.sidebar.markdown("Made by thefog27")
st.sidebar.markdown(
    '[🗂️ Link to my GitHub Account](https://github.com/thefog27)',
    unsafe_allow_html=True
)


# --- Page Setup ---
project_1_page = st.Page(
    'views/Bonus_Dashboard.py',
    title="Bonus Dashboard",
    icon = '📊'
)
project_2_page = st.Page(
    "views/Explanation.py",
    title="Explanation",
    icon='❓'
)


# --- Navigation Setup ---
pg = st.navigation(pages=[project_1_page, project_2_page])


# --- Run Page ---
pg.run()