# CodeAlpha Internship – Email Extraction Project

## 📌 Project Overview

This project is developed as part of my **CodeAlpha Internship**.  
The project demonstrates how to extract email addresses from a text file using **Python Regular Expressions (Regex)**.

The program reads the contents of `email_extraction_practice.txt`, identifies valid email addresses using a regular expression pattern, displays the extracted emails, and saves them into a separate file named `extracted_emails.txt`.

## 🎯 Objectives

- Read text data from a file.
- Use Python's `re` module for pattern matching.
- Identify email addresses from the text.
- Display the extracted email addresses.
- Save the extracted emails into a new text file.

## 🛠️ Technologies Used

- **Python 3**
- **Regular Expressions (`re` module)**
- **Text Files (`.txt`)**

## 📂 Project Files

```text
Email-Extraction-Project/
│
├── email_extraction.py
├── email_extraction_practice.txt
├── extracted_emails.txt
└── README.md
```

## ⚙️ How It Works

1. The program imports Python's built-in `re` module.
2. It opens `email_extraction_practice.txt` and reads the complete text.
3. `re.findall()` searches the text for email addresses.
4. The regular expression used is:

```python
r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
```

5. The extracted email addresses are displayed on the screen.
6. The emails are written one per line into `extracted_emails.txt`.

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

### 2. Keep the required files together

Place these files in the same folder:

- `email_extraction.py`
- `email_extraction_practice.txt`

### 3. Run the program

Open a terminal in the project folder and run:

```bash
python email_extraction.py
```

## 📤 Output

The program displays:

```text
Extracted Email Addresses:
```

followed by the email addresses found in the input file.

It then creates:

```text
extracted_emails.txt
```

and stores each extracted email address on a separate line.

## 🔍 Regular Expression Explanation

The email pattern is designed to match common email-address formats.

- `\b` – Word boundary.
- `[A-Za-z0-9._%+-]+` – Matches the username/local part.
- `@` – Matches the `@` symbol.
- `[A-Za-z0-9.-]+` – Matches the domain name.
- `\.` – Matches the dot before the domain extension.
- `[A-Za-z]{2,}` – Matches a domain extension containing at least two letters.
- `\b` – Word boundary.

## 💡 Learning Outcomes

Through this project, I practiced:

- Python file handling.
- Reading and writing text files.
- Regular expressions.
- Pattern matching with `re.findall()`.
- Automating data extraction.
- Saving processed data into an output file.

## 👨‍💻 Internship

**Internship:** CodeAlpha Internship  
**Project:** Email Extraction using Python  
**Language:** Python

## 📜 Conclusion

This project provides a simple and practical demonstration of using Python Regular Expressions to extract email addresses from text. It helped strengthen my understanding of **file handling, regular expressions, string processing, and basic automation in Python**.

---

⭐ Developed as part of my **CodeAlpha Internship**.
