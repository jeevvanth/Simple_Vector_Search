# PDF Query System with ChromaDB
## Overview

This project allows you to verify PDF documents, store their content as vector embeddings, and ask natural language questions against them. The system retrieves the most relevant information from the stored PDFs and returns results based on semantic similarity.

## Prerequisites
* Python 3.9 or higher

* pip installed

* Virtual environment support

## Create and Activate Virtual Environment
### Create venv
```bash
python -m venv venv
```

## Activate venv
### On Linux / macOS
``` bash
source venv/bin/activate
```
### On Windows
```bash
venv\Scripts\activate
```
## Install Dependencies

Make sure your virtual environment is active, then run:
```bash
pip install -r requirements.txt

```

## PDF Verification and Storage

* PDF files are processed and converted into text

* The text is transformed into embeddings using a pretrained language model

* These embeddings are stored locally in a persistent Chroma database

* This allows fast similarity-based retrieval later

##Asking Queries

* You can enter questions in natural language

* The system searches the vector database for the most relevant PDF chunks

* The top matching results are returned for analysis

* This enables contextual understanding instead of keyword matching

## How It Works (High-Level Explanation)

* A language model converts text into numerical vectors that capture meaning

* All document vectors are stored in a local vector database

* When a query is entered, it is converted into the same vector format

* The database compares vectors and finds the closest matches

* The most relevant document sections are returned for further reasoning or analysis

## Persistent Storage

* All processed data is saved locally

* You do not need to reprocess PDFs every time

* Data remains available across multiple runs

## Notes

Ensure PDFs are verified and processed before querying

The quality of answers depends on the content of the documents

This setup is suitable for document analysis, Q&A systems, and research workflows
