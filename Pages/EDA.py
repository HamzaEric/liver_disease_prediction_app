import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components
def main():
    st.set_page_config(layout="wide")
    st.title('Exploratory Data Analysis And Machine Learning Implementation')
    st.markdown('---')
    st.write('''
    Random Forest Classifier builds many decision trees on random parts of the data. 
    Each tree makes a prediction, and the final result is based on the majority vote. 
    This makes it accurate, stable, and good at handling complex data.
    ''')
    st.markdown('---')
    html_file=Path('Liver_Disease_Classification.html')
    components.html(html_file.read_text(encoding='utf-8',errors='replace'),height=1000,scrolling=True)
if __name__ == '__main__':
    main()
