# ⚙️ Configuration Manager

A simple and powerful web-based configuration management tool built with **Flask**. It allows users to upload or paste configuration files in `.ini` or `.json` format, view and edit the configuration through a clean web UI, save it to a **SQLite database**, and export the updated configuration.

---

## 🔧 Features

- 🌐 Web interface to upload, paste, and edit configuration files
- 📝 Supports both `.ini` and `.json` formats
- 🧩 Displays parsed config as editable tables grouped by section
- 💾 Stores latest configuration in SQLite database
- 📤 Exports updated config as `.ini` or `.json` files
- 🔌 REST API for fetching and updating configuration programmatically

---

## 📁 Project Structure

```bash
config_parser/
├── app.py             # Flask web application
├── templates/
│   └── index.html     # Web interface HTML template
├── uploads/           # Uploads directory (auto-created)
├── database.db        # SQLite database (auto-generated)
└── README.md          # Project documentation

---
```
## 📦 Requirements

- Python 3.12 or higher
- pip (Python package installer)

## How to install
git clone https://github.com/sainathislavath/Backup_Files.git

cd Backup_Files

### Install required packages:

pip install flask

### Run the application

python app.py

### Open in Browser

http://127.0.0.1:5000/

![alt Backup Files](image.png)