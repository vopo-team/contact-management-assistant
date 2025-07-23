# contact-management-assistant

Command-line assistant bot that stores and manages contacts with names, addresses, phone numbers, emails, and birthdays; validates input; lists upcoming birthdays; supports search, editing, and deletion of contacts and text notes; ensures local data persistence.

## ! Before start please read SECURITY.md and CONTRIBUTING.md

## How to use:
After starting your application:
 1. Try start with following commands ```hello```, ```add```, ```find```, ```change```, ```delete```, ```birthdays```, ```find-notes```
 2. Use ```close``` or ```exit``` to safety close the application

### Clone project
```git clone https://github.com/vopo-team/contact-management-assistant.git```

### Create virtual environment
1. ```python -m venv .venv```
2. ```source .venv/bin/activate```

## Project structure

### Folders
```commands/``` - CLI commands
```models/``` - Model abstractions
```utils/``` - utilities, helper functions, constants

### Root files
```.env``` - File with important variables
```SECURITY.md``` - Security policy
```CONTRIBUTING.md``` - Contribution policy
```main.py``` - Entry point
```requirements.txt``` - Dependency list
```.gitignore``` - List of ignored files by git
