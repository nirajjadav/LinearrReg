import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Advertising Spends Prediction using Machine Learning")
st.markdown("This Model Identify total spends on advertising")

st.header("Advertising Spend on various Media ")
col1,col2 = st.columns(2)

with col1:
	st.text("TV")
	tv = st.slider("Adver. Spends on TV", 1.0, 10000.0, 0.5)
	st.text("Radio")
	rd = st.slider("Adver. Spends on Radio", 1.0, 10000.0, 0.5)
	st.text("NewsPaper")
	newspaper = st.slider("Adver. Spends on NewsPaper", 1.0,10000.0,0.5)

clf = pickle.load(open("mymodel.pkl","rb"))

def predict(data):
	return clf.predict(data)
	
st.text('')
if st.button("Seles Prediction "):
    result = clf.predict(np.array([[tv,rd,newspaper]]))
    st.text(result[0])

st.markdown("Developed By Avinash Pawar at NIELIT Daman")
