# Amortization Automation

This program provides sales upload, amortization compilation and pivoting automation.  The mid month amortization method applies to time-base subscription of monthly sales file.  Multiple sales files are allowed to upload and compiled into one master amortization schedule.

## Amortization Demo
https://user-images.githubusercontent.com/95498383/178642553-2cf9a253-8e01-4cca-aaa4-b6f9f75eb7e6.mp4

## Technologies

This project leverages python 3.7 with the following packages:


* [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) - For Series, DataFrame, and plots

* [streamlit](https://docs.streamlit.io/library/get-started) - For deploying data apps

* [datetime](https://docs.python.org/3/library/datetime.html) - For manipulating dates and times.

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install pandas
  pip install streamlit
```

## Usage

To use the fintech finder, simply clone the all the files from the respository, open CLI and run **amort_app.py** with:

```python
streamlit run amort_app.py
```

## Contributors

Brought to you by Eunice Huang

---


## License

MIT
