# Pair Exercise #4 — Sequential vs. Concurrent Wikipedia Downloads

---

## Overview

The script `pe4.py` performs two tasks:

1. **Sequential Download**  
   - Searches for topics related to *"generative artificial intelligence"*  
   - Downloads each Wikipedia page one at a time  
   - Saves references into `<page title>.txt`

2. **Concurrent Download**  
   - Defines the required function `wiki_dl_and_save(topic)`  
   - Uses `ThreadPoolExecutor.map()` to download topics in parallel  
   - Saves references in the same format as the sequential version

Both sections measure and print their execution time.

---

## How to Run

Install dependencies:
pip install wikipedia


Run the script:
python3 pe4.py

## Summary

Both sequential and concurrent implementations run successfully.  
The concurrent approach is significantly faster, satisfying all assignment requirements.

