import os
import pandas as pd
import pycaret.classification as pycc
import pycaret.regression as pycr
import streamlit as st
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

# some page configurations
st.set_page_config(page_title='AutoML Project', page_icon='random')

# create uploads directory
directory = 'uploads'
if not os.path.exists(directory):
    os.makedirs(directory)

# create models directory
directory = 'models'
if not os.path.exists(directory):
    os.makedirs(directory)

# if there's an uploaded file load it
uploaded_file = 'uploads/uploaded_dataset.csv'
if os.path.exists(uploaded_file):
    df = pd.read_csv(uploaded_file, index_col=None)

with st.sidebar:
    st.title('AutoML Project')
    st.image('https://www.pngkey.com/png/full/115-1159250_hey-machine-learning-logo-machine-learning-logo.png', output_format='PNG')
    choice = st.radio('Navigation', [
                      'Upload', 'EDA', 'ML - Classification', 'ML - Regression', 'Download'])
    st.info('This webapp allows you to create automated ML pipelines, using Python, Streamlit, and Pandas-Profiling. Code available on Github @ https://github.com/sergani/auto-ml.')

if choice == 'Upload':
    st.title('Upload data for profiling and modeling')
    file = st.file_uploader('Upload your CSV dataset here:',
                            accept_multiple_files=False, type='csv')
    if file:
        df = pd.read_csv(file)
        df.to_csv('uploads/uploaded_dataset.csv', index=None)
        st.dataframe(df)

if choice == 'EDA':
    st.title('Exploratory Data Analysis')
    st.text(f'Using file: {uploaded_file}')
    profile_df = df.profile_report()
    st_profile_report(profile_df)

if choice == 'ML - Classification':
    st.title('Modelling (Classification)')
    st.text(f'Using file: {uploaded_file}')

    # choose the classification target (y)
    y = st.selectbox('Choose the Target Column', df.columns)

    if st.button('Run Modelling'):
        # setup the models
        setup = pycc.setup(df, target=y)
        setup_df = pycc.pull()
        st.dataframe(setup_df)

        # compare and select the best model
        best_model = pycc.compare_models()
        compare_df = pycc.pull()
        st.dataframe(compare_df)

        # save the model to the models directory
        pycc.save_model(best_model, 'models/best_model_cls.mdl')

if choice == 'ML - Regression':
    st.title('Modelling (Regression)')
    st.text(f'Using file: {uploaded_file}')

    # choose the regression target (y)
    y = st.selectbox('Choose the Target Column', df.columns)

    if st.button('Run Modelling'):
        # setup the models
        setup = pycr.setup(df, target=y)
        setup_df = pycr.pull()
        st.dataframe(setup_df)

        # compare and select the best model
        best_model = pycr.compare_models()
        compare_df = pycr.pull()
        st.dataframe(compare_df)

        # save the model to the models directory
        pycr.save_model(best_model, 'models/best_model_reg.mdl')

if choice == 'Download':
    # get list of available files to download
    dl_file = st.radio('Available files to download:', os.listdir('models'))

    # download the selected model file
    with open('models/' + dl_file, 'rb') as f:
        st.download_button('Download Model', f, file_name=dl_file)
