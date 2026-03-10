
# Malaria Detection using Deep Learning

This is a Streamlit web application for detecting malaria parasites from microscopic blood cell images using a CNN model.

## Steps to Run

1. Install requirements
pip install -r requirements.txt

2. Download malaria dataset from NIH and extract into:
dataset/cell_images/

3. Train model
python train_model.py

4. Run web app
streamlit run app.py

## Dataset
NIH Malaria Dataset (~27k images)

Classes:
Parasitized
Uninfected
