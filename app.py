import streamlit as st

st.set_page_config(page_title="מנתח מניות", layout="wide")

st.title("מנתח מניות אישי")
st.write("האפליקציה פועלת בהצלחה!")

ticker = st.text_input("הכנס סימול מניה", "MSFT")
st.write("המניה שנבחרה:", ticker)

