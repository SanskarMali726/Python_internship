# 📇 Contact Management System (Python CLI)

A simple and powerful **Contact Management System** built using **Python**.  
This is a **command-line based application** that allows users to store, search, update, and manage contacts with proper validation and file persistence.

---

## 🚀 Features

- ➕ Add new contacts
- 🔍 Search contacts by name
- 📞 Search contacts by phone number
- ✏️ Update existing contacts
- ❌ Delete contacts
- 📋 Display all contacts
- 📊 Show contact statistics
- 📤 Export contacts to CSV
- 💾 Auto-save data using JSON
- 🔒 Input validation (phone & email)
- 🧪 Unit testing using `pytest`

---

## 🛠️ Technologies Used

- **Python 3**
- **JSON** (data storage)
- **CSV** (export feature)
- **Regex** (validation)
---

## 📁 Project Structure

```
├── contact_manager.py 
├── test_contact.py 
├── contacts_data.json 
├── contacts_backup.json
├── contacts.csv 
├── .gitignore
└── README.md
```


---

## ▶️ How to Run the Application

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SanskarMali726/Python_internship.git

cd week3/contact_manager

python contact_manager.py

```

---


## 📝 Input Validation Rules
### 📞 Phone Number


- Only digits are stored

- Length must be 10 to 15 digits

- Supports country codes



### 📧 Email


- Must follow standard email format <br>
Example: example@gmail.com

---

## 📤 CSV Export

- Contacts can be exported to contacts.csv

- Compatible with Excel, LibreOffice, and Google Sheets

---

## 🔒 Data Safety

- Primary data stored in contacts_data.json

- Automatic backup created in contacts_backup.json

⚠️ These files are ignored using .gitignore to protect privacy.

--- 

## 👨‍💻 Author

Sanskar Mali <br>
Computer Engineering Student <br>
Passionate about Backend Development & Systems Programming

---
---