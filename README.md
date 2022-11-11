# Introduction
This project is called AutoML and it demonstrates how machine learning pipelines could be built inside of a web app. You'll be able to upload your datasets, explore the data using Streamlit Pandas Profiling, model your data, then save and download the best produced model to your machine.

This project is heavily inspired by Nicholas Renotte's video on Youtube (https://www.youtube.com/watch?v=xTKoyfCQiiU) - go check this guy out! Cheers buddy.

# Installation
First you need to clone the project. You probably want to have a virtual environment for this to work without affecting your main development environment.

`mkdir -p /path/to/virtualenv/`

`cd /path/to/virtualenv/`

`python3 -m venv ./`

`source bin/activate`

`pip install -r requirements.txt`

`git clone https://github.com/sergani/auto-ml.git`

To run the app, all you have to do is run app.py using streamlit:

`streamlit run app.py`

