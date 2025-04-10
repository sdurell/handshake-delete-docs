# Handshake Document Deleter

A simple script to automate deleting documents from your Handshake account.

## Requirements
- Python 3.6+
- Selenium
- Chrome browser and ChromeDriver

## Installation
```bash
pip install selenium
```

## Usage
1. Run `python delete_docs.py`
2. Log into your Handshake account when the browser opens
3. The script will automatically delete all documents and show a count when finished

## How It Works
The script opens Handshake, waits for your login, then systematically deletes each document by navigating through the document deletion workflow until no documents remain.

## Note
Manual login is required due to Handshake's authentication system.