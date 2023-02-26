import streamlit as st
import requests
from streamlit_lottie import st_lottie

# More emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='Mubarak Mayyeri', page_icon=':wink:', layout='wide')

# Assets
medical_anim = 'https://assets1.lottiefiles.com/packages/lf20_stukuo1f.json'

def load_lottie(url):
    req = requests.get(url)
    if req.status_code != 200:
        return None
    return req.json()

# Header Section
with st.container():
    st.subheader("Hi, I am Mubarak Mayyeri :wave:")
    st.title("Data Scientist | Python Developer | Web Designer")
    st.write("As a skilled data scientist with a passion for statistics, machine learning, and web development, I thrive on extracting insights from complex data sets."
            "I specialize in translating data into actionable insights for data-driven decisions,"
            "and help businesses make informed, data-driven decisions that lead to success.")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("[Connect with me on LinkedIn >](https://www.linkedin.com/in/mubarakmayyeri/)")
    with right_column:
        st.write("[Checkout my GitHub Profile >](https://github.com/mubarakmayyeri)")

# Projects
with st.container():
    st.write('---')
    st.title('Personal Projects')
    '''
    ### 1. Diagnosing whether Breast cancer using Machine Learning model
    '''
    left_column, right_column = st.columns((2, 1))
    with left_column:
        st.write('##')
        '''
        Cancer diagnosis is a critical and often challenging task that requires a high level of expertise and precision from medical professionals.
        So I developed a machine learning model for predicting whether breast cancer with some given observations is malignant or benign.
        * Collected data from for finding features affecting cancer's character
        * Did Exploratory Data Analysis for finding insights and understanding relations form the dataset using Pandas, Numpy, Matplotlib and Seaborn Libraries.
        * Cleaned and processed data for making it suitable for Machine Learning model.
        * Trained and evaluated Logistic regression and Random Tree Forest Classifier model for prediction.
        * Tuned hyperparameter of the model with highest accuracy for better performance.
        
        With the ability to quickly and accurately analyze a patient's medical data and provide a diagnosis, a machine learning model like this one could help doctors to make more informed decisions and improve the overall quality of cancer care.
        '''
        
    with right_column:
        st.write('##')
   
        st_lottie(load_lottie(medical_anim), height=250, key='Cancer')
    st.markdown('##### [GitHub Repository](https://github.com/mubarakmayyeri/breast-cancer-classification)')