import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': "https://reflexive.ai",
        'Report a bug': "https://reflexive.ai",
        'About': "# REFLEXIVE.AI\n ## VIRTUAL AGENTS TO HELP YOU GROW YOUR BUSINESS \nhttps://reflexive.ai"
    }
)

# Add custom CSS to hide the GitHub icon
# hide_github_icon = """
# #GithubIcon {
#   visibility: hidden;
# }
# """
# st.markdown(hide_github_icon, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Reflexive AI")
st.header("QA documents")
