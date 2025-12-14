# Pair Exercise #3 — Functions & Classes

This repository contains my solution for **Pair Exercise #3** in IST 303.  
The assignment required implementing:

- A Caesar cipher encoder and decoder (`encode`, `decode`)
- A base `BankAccount` class
- Two subclasses: `SavingsAccount` and `CheckingAccount`
- Rules for deposits, withdrawals, overdrafts, and account age restrictions

---

## Test Results

All tests were run locally using `pytest`, and the expected results were achieved:

- **25 passed**
- **2 xfailed** - expected failures included in the test suite

---

## Project Structure

pe3.py  -  Main assignment file
test_pe3.py - Instructor-provided test suite (for local testing)
pytest.ini - Pytest configuration file
README.md


---

## How to Run Tests Locally

1. **Create and activate a virtual environment:**

   **macOS / Linux:**
   python3 -m venv venv
   source venv/bin/activate


   **Windows (cmd):**
   python -m venv venv
   venv\Scripts\activate

   **Windows (PowerShell):**
   python -m venv venv
   .\venv\Scripts\Activate.ps1


2. **Install dependencies:**
pip install pytest


3. **Run the tests:**
pytest -v test_pe3.py


---

## Summary

All assignment components have been implemented and validated through automated tests.  
This repository is ready for submission per project guidelines.
