# 🔒 Password Checker Tool  

A Python-based tool that helps you check if your passwords have been compromised using the [Have I Been Pwned API](https://haveibeenpwned.com/Passwords). This project ensures privacy and security while providing a user-friendly experience for verifying password safety.  

---

## 🚀 Features  
- **Individual Password Check**: Enter a password to see if it’s been breached.  
- **Batch Processing**: Upload a file containing multiple passwords for bulk checking.  
- **Secure Hashing**: Uses SHA-1 hashing to ensure your passwords are not exposed during the process.  
- **Privacy-Oriented**: Only the first five characters of the hash are sent to the API, keeping your passwords secure.  
- **User-Friendly**: Clear and detailed output, including the number of times a password has been breached.  

---

## 🛠️ How It Works  
1. **Hashing**: Your password is hashed using SHA-1 encryption.  
2. **API Query**: The first five characters of the hash are sent to the Have I Been Pwned API.  
3. **Response Parsing**: The API returns a list of hashes starting with the same five characters. The tool checks if your hashed password tail matches any of these.  
4. **Result**: If a match is found, the tool shows how many times your password has appeared in data breaches.  

---

## ⚙️ Requirements  
- Python 3.8 or later  
- Libraries:  
  - `requests`  
  - `argparse`  

To install the required libraries:  
```bash
pip install -r requirements.txt
