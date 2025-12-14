
import wikipedia
import time
from concurrent.futures import ThreadPoolExecutor

# SECTION A – Sequential Wikipedia Downloads

print("Starting Section A: Sequential Download\n")

start_time = time.perf_counter()

# 1. Search for topics
topics = wikipedia.search("generative artificial intelligence")

# 2. Loop through topics one by one
for topic in topics:
    try:
        # Get the page (auto_suggest must be False)
        page = wikipedia.page(topic, auto_suggest=False)

        title = page.title
        references = page.references   # this is a list of links

        # Replace characters that can't be used in filenames
        safe_title = title.replace("/", "-").replace(":", "-")

        # Write references to a file, one per line
        filename = f"{safe_title}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for ref in references:
                f.write(ref + "\n")

        print(f"Wrote references for: {title}")

    except Exception as e:
        # Wikipedia may fail on some pages — we simply skip them
        print(f"Could not process topic '{topic}': {e}")

end_time = time.perf_counter()
print("\nSequential download completed in:", round(end_time - start_time, 4), "seconds\n")


# SECTION B – Concurrent Wikipedia Downloads

print("Starting Section B: Concurrent Download\n")

start_time_concurrent = time.perf_counter()

# 1. Search again (as required)
topics_concurrent = wikipedia.search("generative artificial intelligence")


# 2. Function required by assignment
def wiki_dl_and_save(topic):
    """
    Downloads a Wikipedia page and writes its references to a text file.
    Each reference is written on its own line.
    """
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        title = page.title
        references = page.references

        safe_title = title.replace("/", "-").replace(":", "-")
        filename = f"{safe_title}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            for ref in references:
                f.write(ref + "\n")

        print(f"[Concurrent] Wrote references for: {title}")

    except Exception as e:
        print(f"[Concurrent] Could not process topic '{topic}': {e}")


# 3. Use ThreadPoolExecutor to run downloads concurrently
with ThreadPoolExecutor() as executor:
    executor.map(wiki_dl_and_save, topics_concurrent)

end_time_concurrent = time.perf_counter()
print("\nConcurrent download completed in:", round(end_time_concurrent - start_time_concurrent, 4), "seconds")

print("\nDone.")
