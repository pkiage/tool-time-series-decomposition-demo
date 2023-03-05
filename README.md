---
title: Time Series Decomposition Demo
emoji: 📈
colorFrom: indigo
colorTo: blue
sdk: streamlit
sdk_version: 1.17.0
app_file: app.py
pinned: false
license: openrail
---

# Time series decomposition tool

Tool demonstrating time series decomposition in Python.

Assumes uploaded data is clean.

## Built With

- [Streamlit](https://streamlit.io/)


## Local setup

### Obtain the repo locally and open its root folder

#### To potentially contribute

```shell
git clone https://github.com/pkiage/tool-time-series-decomposition-demo
```

or

```shell
gh repo clone pkiage/tool-time-series-autocorrelation-demo
```

#### Just to deploy locally

Download ZIP

### (optional) Setup virtual environment:

```shell
python -m venv venv
```

### (optional) Activate virtual environment:

#### If using Unix based OS run the following in terminal:

```shell
.\venv\bin\activate
```

#### If using Windows run the following in terminal:

```shell
.\venv\Scripts\activate
```

### Install requirements by running the following in terminal:

#### Required packages

```shell
pip install -r requirements.txt
```

## Build and install local package

```shell
python setup.py build
```

```shell
python setup.py install
```

### Run the streamlit app (app.py) by running the following in terminal (from repository root folder):

```shell
streamlit run src/app.py
```

## Hugging Face Tips

Initial Setup
- [When creating the Spaces Configuration Reference](https://huggingface.co/docs/hub/spaces-config-reference) ensure the [Streamlit Space](https://huggingface.co/docs/hub/spaces-sdks-streamlit) version (sdk_version) specified is supported by HF

```shell
git remote add space https://huggingface.co/spaces/pkiage/time_series_autocorrelation_demo

git push --force space main
```
- [When syncing with Hugging Face via Github Actions](https://huggingface.co/docs/hub/spaces-github-actions) the [User Access Token](https://huggingface.co/docs/hub/security-tokens) created on Hugging Face (HF) should have write access


## Demo Links
- Hugging Face Space: https://huggingface.co/spaces/pkiage/time_series_decomposition_demo
- Streamlit Community Cloud: https://pkiage-tool-time-series-autocorrelation-demo-app-l0umps.streamlit.app/


