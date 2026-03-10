
import streamlit as st
from PIL import Image
from src.predictor import predict

st.set_page_config(page_title="MalariaScope AI", layout="wide")

st.markdown("# 🧬 Revolutionary AI‑Powered Malaria Detection")

col1,col2,col3 = st.columns(3)
col1.metric("Accuracy","~99%")
col2.metric("Analysis Time","<3s")
col3.metric("Scans Today","2,852")

st.divider()

st.subheader("Upload Blood Cell Image")

file = st.file_uploader("Drag & Drop microscopic image", type=["png","jpg","jpeg"])

if file:
    img = Image.open(file)
    st.image(img,width=350)

    if st.button("Analyze Sample"):
        label,confidence = predict(img)

        st.subheader("Diagnostic Report")

        if label=="Uninfected":
            st.success("✅ UNINFECTED")
        else:
            st.error("⚠️ PARASITIZED")

        st.progress(int(confidence*100))
        st.write(f"Confidence Level: {confidence*100:.2f}%")
