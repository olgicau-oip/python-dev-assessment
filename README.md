# Python Developer Assessment

This repository contains Python exercises completed as part of a developer assessment. The project covers Git workflow, code style and linting, basic data structures and algorithms, object-oriented programming, error handling, and API interaction.

## Completed Tasks

- **Task 1.2: Git Basics**
  - Branch management and repository workflow
- **Task 1.3: Code Style & Linting**
  - File: `bad_style.py`
  - Used `flake8` and `black` to fix style issues and ensure clean code
- **Task 2.1: Basic Data Structures & Algorithms**
  - File: `dsa_challenges.py`
  - Implemented `filter_and_sort_evens()` and `count_character_frequency()`
- **Task 2.2: Object-Oriented Programming**
  - File: `book_store.py`
  - Created a `Book` class with summary and age calculation methods
- **Task 2.3: Error Handling & Debugging**
  - File: `debug_errors.py`
  - Fixed divide-by-zero logic and implemented safe list access with exceptions
- **Task 3.1: API Interaction**
  - File: `api_client.py`
  - Fetched user data from JSONPlaceholder with network and response validation

## Running the Code

Use Python to run each example file from the project root:

```powershell
python bad_style.py
python dsa_challenges.py
python book_store.py
python debug_errors.py
python api_client.py
```

For `api_client.py`, the `requests` library is required, which is already installed in the current environment.

## Reflections

- **Most challenging:** Keeping the code style clean across multiple task files while preserving the required example structure and error-handling behavior.
- **Most interesting:** Working with the JSONPlaceholder API and handling real-world error conditions like network failures and unexpected response formats.
- **What I learned:** I improved my ability to use `flake8` and `black` together to enforce style while also writing robust error handling in Python.

