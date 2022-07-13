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

The MIT License (MIT)

Copyright (c) 2022 Eunice Huang

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
