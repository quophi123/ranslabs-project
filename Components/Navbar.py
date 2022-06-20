import streamlit as st 



def Navbar():
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

  st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="http://localhost:8502" target="_blank">Rans Labs</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="http://localhost:8502" target="_self">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8502/EDA" target="_self">EDA</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8502/Visualization" target="_self">Visualization</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8502/Modulbuild" target="_self">Build Model</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8502/Prediction" target="_self">Make Prediction</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)