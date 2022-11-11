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
        df.to_csv('uploads/' + file.name, index=None)
        st.dataframe(df)

if choice == 'EDA':
    st.title('Exploratory Data Analysis')
    file_list = []

    for fname in os.listdir('uploads'):
        if fname.endswith(('.csv', '.CSV', '.Csv')):
            file_list.append(fname)

    if len(file_list) > 0:
        dataset = st.selectbox(
            'Choose one of the following available files', file_list)
        
        if st.button('Run EDA!'):
            st.text(f'Using file: {dataset}')
            df = pd.read_csv(f'uploads/{dataset}')
            profile_df = df.profile_report()
            st_profile_report(profile_df)
    else:
        st.text('Please upload a dataset first!')
        st.text('It will then appear here..')

if choice == 'ML - Classification':
    st.title('Modelling (Classification)')
    file_list = []

    for fname in os.listdir('uploads'):
        if fname.endswith(('.csv', '.CSV', '.Csv')):
            file_list.append(fname)

    if len(file_list) > 0:
        dataset = st.selectbox(
            'Choose one of the following available files:', file_list)
        
        df = pd.read_csv(f'uploads/{dataset}')

        y = st.selectbox('Choose the target classification column:', df.columns)
        
        if st.button('Run Modelling!'):
            # setup the models
            setup = pycc.setup(df, target=y)
            setup_df = pycc.pull()
            st.text('Model setup and description:')
            st.dataframe(setup_df)

            # compare and select the best model
            best_model = pycc.compare_models()
            compare_df = pycc.pull()
            st.text('Model comparison:')
            st.dataframe(compare_df)

            # save the model to the models directory
            pycc.save_model(best_model, 'models/best_model_cls')
    else:
        st.text('Please upload a dataset first!')
        st.text('It will then appear here..')

if choice == 'ML - Regression':
    st.title('Modelling (Regression)')
    file_list = []

    for fname in os.listdir('uploads'):
        if fname.endswith(('.csv', '.CSV', '.Csv')):
            file_list.append(fname)

    if len(file_list) > 0:
        dataset = st.selectbox(
            'Choose one of the following available files:', file_list)
        
        df = pd.read_csv(f'uploads/{dataset}')

        y = st.selectbox('Choose the target regression column:', df.columns)
        
        if st.button('Run Modelling!'):
            # setup the models
            setup = pycr.setup(df, target=y)
            setup_df = pycr.pull()
            st.text('Model setup and description:')
            st.dataframe(setup_df)

            # compare and select the best model
            best_model = pycr.compare_models()
            compare_df = pycr.pull()
            st.text('Model comparison:')
            st.dataframe(compare_df)

            # save the model to the models directory
            pycr.save_model(best_model, 'models/best_model_reg')
    else:
        st.text('Please upload a dataset first!')
        st.text('It will then appear here..')

if choice == 'Download':
    # get list of available files to download
    file_list = []

    for fname in os.listdir('models'):
        if fname.endswith(('.pkl')):
            file_list.append(fname)
    
    if len(file_list) > 0:
        dl_file = st.radio('Available files to download:', file_list)
        # download the selected model file
        if dl_file:
            with open('models/' + dl_file, 'rb') as f:
                st.download_button('Download', f, file_name=dl_file)
    
    else:
        st.text('Please model a dataset first!')
        st.text('It will then appear here..')