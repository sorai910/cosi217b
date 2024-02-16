#Requirements
Python 3.10.9 is needed to run this program.
Use the following command to install required dependecies
```bash
$ pip install {dependency}
```
- dependeicies:
  - fastapi
  - uvicorn
  - json
  - pydantic
  - flask
  - pandas
  - streamlit
  - graphviz
  - spacy
  - spacy_streamlit
#How to run
- app_FastAPI.py
```bash
$ uvicorn app_FastAPI:app --reload
```
replace {filename} by actual filename
```bash
$ curl http://127.0.0.1:8000
$ curl http://127.0.0.1:8000/ner -H "Content-Type: application/json" -d@{filename}
$ curl http://127.0.0.1:8000/dep -H "Content-Type: application/json" -d@{filename}
```
- app_flask.py
```bash
$ python3 app_flask.pyV
```
- app_strealit.py
```bash
$ streamlit run app_streamlit.py
  ```