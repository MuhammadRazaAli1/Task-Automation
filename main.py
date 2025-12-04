import re
import os

# Step 1: Define file names
input_file = "sample_text.txt"
output_file = "extracted_emails.txt"

# Step 2: Check if input file exists, if NOT → create it
if not os.path.exists(input_file):
    print(f"'{input_file}' file not found. New file created!")
    with open(input_file, "w", encoding="utf-8") as f:
        f.write("Example emails:\nuser@example.com\ncontact@mail.com\n")
    print("Add your text/paragraph with emails to this file.")
    print("Then run the script again.\n")

# Step 3: Read content safely
with open(input_file, "r", encoding="utf-8") as file:
    content = file.read()

# Step 4: Extract emails using regex
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Step 5: Remove duplicates
unique_emails = sorted(list(set(emails)))

# Step 6: Save extracted emails
with open(output_file, "w", encoding="utf-8") as file:
    for email in unique_emails:
        file.write(email + "\n")

# Step 7: Print Summary
print("     ✅ Email Extraction Complete")
print("--------------------------------------")
print(f"📄 Input File: {input_file}")
print(f"📄 Output File: {output_file}")
print(f"📧 Total Unique Emails Found: {len(unique_emails)}")
