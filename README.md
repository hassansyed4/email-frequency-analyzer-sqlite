# SQLite Email Counter

A Python and SQLite project that parses email log data from a text file, extracts sender email addresses, counts how many times each email appears, stores the results in a SQLite database, and displays the top 10 most frequent senders.

## Project Overview

This project demonstrates how to:

- Read and process structured text data using Python
- Extract email addresses from log-style input files
- Store processed results in a SQLite database
- Perform SQL queries to retrieve sorted results
- Combine Python logic with SQL operations for data analysis

It is a simple but practical example of data parsing, database interaction, and query-based reporting.

## Technologies Used

- Python
- SQLite
- SQLite DB Browser
- SQL
- VS Code
- Jupyter NoteBook
- Git & GitHub

## Features

- Reads email data from a text file
- Identifies valid sender lines starting with `From:`
- Extracts sender email addresses
- Stores email frequency counts in SQLite
- Updates counts dynamically if an email already exists
- Retrieves and displays the top 10 most frequent email senders

## File Structure

```bash
sqlite-email-counter/
├── main.py
├── mbox-short.txt
├── mbox.txt
├── emaildb.sqlite
├── requirements.txt
├── .gitignore
└── README.md
