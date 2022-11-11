# Introduction
This project is called AutoML and it demonstrates how machine learning pipelines could be built inside of a web app. You'll be able to upload your datasets, explore the data using Streamlit Pandas Profiling, model your data, then save and download the best produced model to your machine.

This project is heavily inspired by Nicholas Renotte's video on Youtube (https://www.youtube.com/watch?v=xTKoyfCQiiU) - go check this guy out! Cheers buddy.

# Installation
First you need to clone the project. You probably want to have a virtual environment for this to work without affecting your main development environment.

`# mkdir -p /path/to/virtualenv/`

`# cd /path/to/virtualenv/`

`# python3 -m venv ./`

`# source bin/activate`

`# git clone https://github.com/sergani/auto-ml.git`

`# pip install -r requirements.txt`

To run the app, all you have to do is run app.py using streamlit:

`# streamlit run app.py`

If you get this in your browser then you're all good!

![Main page view](https://drive.google.com/file/d/1N39WP6WKQFgX4R5lyFT_X5xfi_8Lhw4W/view?usp=share_link)

To upload your dataset, just click on Browse files. You'll be able to upload single CSV files only.

![Upload dataset](https://drive.google.com/file/d/1BQVH9wfSR7-3cTPdDVcEGlXtJOyVII_P/view?usp=share_link)

To explore the data, go to the EDA tab on the left hand side, select one of the available datasets (the app stores preiously uploaded datasets!) and then click on "Run EDA!":

![EDA](https://drive.google.com/file/d/1jXXc1FAJrM4mCknAO9puaqXwXXwBSJC6/view?usp=share_link)

To apply machine learning, go to the right tab on the left hand side, for example, this Titanic dataset is a classification one and so that's what we select:

Once you're on this page, select one of the available datasets uploaded previously, and wait for the app to load the dataset. Afterwards, you have to select the target classification column and click on "Run Modelling!" as follows:

![ML Classification](https://drive.google.com/file/d/1vK4nbA71z88iozG4J1nN4vVLLQ0AGp1G/view?usp=share_link)

At this point, the modelling is done and the best model is chosen by the app after showing the different models' results and stored in the backend:

![ML Model Comparison](https://drive.google.com/file/d/1xW-oLIt6FYYq4SRsVTh4XDIG_CfZSlQr/view?usp=share_link)

If you want to download the model for future use in your data science pipeline, just go to Download and select the model you want to download:

![ML Model Download](https://drive.google.com/file/d/1dcfohutBL5PgXaseV7owmPtMMjGjKaS3/view?usp=share_link)

That's it! Hope this was informative.