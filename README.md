# Email Extractor
Welcome to the Email Extractor, a powerful text processing utility built entirely in Python using regular expressions and file handling. This project demonstrates core Python fundamentals like regex pattern matching, file I/O operations, data deduplication, and automated text analysis.

## Project Overview
Email Extractor is a practical automation tool designed to identify and extract email addresses from text files. The application scans provided text documents, uses advanced pattern matching to locate valid email addresses, removes duplicates, and saves the results to an organized output file. This project bridges the gap between basic text processing and professional data extraction techniques, making it invaluable for email list compilation, data cleaning, and information harvesting.

## Features
* Automatic file creation if input file doesn't exist
* Advanced regex pattern matching for accurate email detection
* Supports multiple email formats and domains
* Automatic duplicate removal and sorting
* UTF-8 encoding for international character support
* Safe file handling with context managers
* Real-time processing and feedback
* Summary statistics showing extraction results
* Clean output file with organized email list
* Error prevention with existence checking
* Beginner to intermediate-level, clean, and readable Python code
* User-friendly interface with clear status messages

## How It Works
* The program checks if the input file exists in the current directory.
* If the input file doesn't exist, a new one is automatically created with sample content.
* Users are prompted to add their text containing emails to the input file.
* When the script runs again, it reads the entire content from the input file.
* Advanced regular expressions scan the content for email patterns.
* Email addresses are extracted based on RFC-compliant format validation.
* Duplicate emails are automatically identified and removed using sets.
* Extracted emails are sorted alphabetically for organized output.
* All unique emails are saved to the output file, one per line.
* A detailed summary is displayed showing files processed and results.

## Regular Expression Pattern Explained
The regex pattern used for email extraction:
```
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

**Pattern Breakdown:**
* `[a-zA-Z0-9._%+-]+` - Username part: Letters, numbers, dots, underscores, percent signs, plus signs, hyphens
* `@` - Required "@" symbol
* `[a-zA-Z0-9.-]+` - Domain name: Letters, numbers, dots, hyphens
* `\.` - Literal dot before TLD
* `[a-zA-Z]{2,}` - Top-level domain: At least 2 letters (com, org, co.uk, etc.)

## Example Usage
```
Input File (sample_text.txt):
---
Contact us at: support@company.com
For sales inquiries: sales@company.com
Customer service: help@example.org
Administrative email: admin@company.com
Support team: support@company.com

Output File (extracted_emails.txt):
---
admin@company.com
help@example.org
sales@company.com
support@company.com

Console Output:
========================================
         ✅ Email Extraction Complete
========================================
📄 Input File: sample_text.txt
📄 Output File: extracted_emails.txt
📧 Total Unique Emails Found: 4
========================================
```

## Supported Email Formats
The extractor recognizes and validates these email formats:

✅ **Standard Format**
- user@example.com
- firstname.lastname@company.org

✅ **Numbers & Special Characters**
- user123@domain.co.uk
- john.doe+filter@gmail.com
- support_team@company.com

✅ **Complex Domains**
- user@subdomain.example.co.uk
- admin@mail.organization.gov
- contact@my-company.com

## File Structure
```
your_project_folder/
├── email_extractor.py
├── sample_text.txt (input file - created automatically)
└── extracted_emails.txt (output file - generated after extraction)
```

## Key Programming Concepts

### Regular Expressions (Regex)
* **Pattern Matching** - Finding specific text patterns in content
* **Character Classes** - `[a-zA-Z0-9]` for matching character sets
* **Quantifiers** - `+` for one or more occurrences
* **Metacharacters** - `@` and `\.` for literal matching
* **re.findall()** - Finding all matches in text

### File Operations
* **os.path.exists()** - Checking if file exists
* **File Reading** - Loading content with proper encoding
* **File Writing** - Saving extracted data to output file
* **Context Managers (with statement)** - Safe file handling
* **UTF-8 Encoding** - Supporting international characters
* **File Creation** - Automatic file generation when needed

### Data Processing
* **String Methods** - Working with text data
* **Set Data Structure** - Automatic duplicate removal
* **List Operations** - Sorting and organizing data
* **Sorting** - Alphabetical organization of results

### Python Modules
* **re module** - Regular expression operations
* **os module** - Operating system file operations
* **Built-in functions** - len(), set(), list(), sorted()

## Concepts Used
* Regular expression pattern matching and validation
* File input/output operations and file handling
* Automatic file creation and error prevention
* Set operations for deduplication
* String encoding and character handling
* Data sorting and organization
* Conditional logic for program flow
* User feedback and summary generation
* Cross-platform file path handling
* Text processing and analysis

## Learning Outcomes
By working with this project, you will learn:

✅ **Regular Expressions** - Mastering regex for pattern matching  
✅ **File Handling** - Reading and writing files safely  
✅ **Data Deduplication** - Removing duplicates efficiently  
✅ **Text Processing** - Analyzing and extracting information  
✅ **Automation** - Building automated data extraction tools  
✅ **Error Prevention** - Proactive error handling strategies  
✅ **Data Organization** - Sorting and organizing extracted data  
✅ **Real-World Applications** - Building practical automation tools  

## Possible Enhancements

Future improvements could include:
* Email validation with SMTP verification
* Extracting phone numbers and URLs
* Support for multiple input files
* Batch processing directories
* Export to CSV or Excel formats
* Email domain analysis and statistics
* Filtering by domain extension
* Web scraping for email collection
* Database integration for storage
* GUI development with Tkinter
* Advanced pattern matching for other data types
* Performance optimization for large files

## Practical Use Cases
* **Email List Compilation** - Gathering emails from documents
* **Contact Database Creation** - Building organized contact lists
* **Data Cleaning** - Removing duplicates from email collections
* **Web Scraping** - Extracting emails from web content
* **Customer Support** - Organizing customer email addresses
* **Marketing Campaigns** - Preparing email lists for outreach
* **Security Audits** - Finding exposed email addresses
* **Research Projects** - Collecting email data for analysis


```

### Step 2: Add content to input file
Open `sample_text.txt` and add your text containing emails

### Step 3: Run the script again
```bash
python email_extractor.py
```

### Step 4: Check results
View `extracted_emails.txt` for the extracted email list

## Regex Resources

For learning more about regular expressions:
* [Python re module documentation](https://docs.python.org/3/library/re.html)
* [Regex101.com - Interactive regex tester](https://regex101.com/)
* [RegexOne - Regex tutorials](https://regexone.com/)
* [Python Regex Tutorial](https://www.w3schools.com/python/python_regex.asp)

## Important Notes

⚠️ **Email Format Limitations:**
- The regex pattern focuses on common email formats
- Some edge cases may not be captured (especially international domains)
- Validation is based on format, not actual email existence
- Verification would require SMTP validation or API calls

✅ **Best Practices:**
- Always verify extracted emails before use
- Keep backup of original files
- Test with sample data first
- Ensure proper encoding for special characters

## Related Concepts
* Data extraction and mining
* Text processing and analysis
* Automation scripting
* Pattern recognition
* Information retrieval
* Data validation techniques
* Email marketing tools
* Contact management systems

---

**"Extract emails efficiently, organize data intelligently."** 📧✨
