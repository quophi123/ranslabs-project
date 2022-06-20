import streamlit as st




def Config():
    st.set_page_config(layout="wide")
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            .css-1k0ckh2{display:none}
            .css-9s5bis{display:none}
            .css-k0sv6k{display:none}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    margins_css = """
        <style>
            .main > div {
                padding-left: 0rem;
                padding-right: 0rem;
            }
        </style>
    """

    # st.markdown(margins_css, unsafe_allow_html=True)

    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)