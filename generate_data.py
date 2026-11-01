# generate_data.py
import os

data_dir = os.path.join("data", "dummy_files")
os.makedirs(data_dir, exist_ok=True)

files = {
    "tax_return_2025.txt": "Official tax return documents for the financial year 2025. Includes income and deductions.",
    "seminar_notes.txt": "Notes on Semantic Data Lifecycle Management using Edge NLP and TinyML.",
    "web_cache_01.log": "session_token=a1b2c3d4e5 timestamp=1718902 cache_hit=true",
    "browser_cookies.tmp": "site=tracker.com user_id=9988 expires=0 session_active=false",
    "bank_statement_jan.txt": "Monthly account statement showing salary credits and utility bill payments."
}

for filename, content in files.items():
    with open(os.path.join(data_dir, filename), "w") as f:
        f.write(content)

print(f"Successfully generated {len(files)} files in '{data_dir}'.")