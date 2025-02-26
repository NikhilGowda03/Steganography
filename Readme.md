# 🛡️ Image Steganography Web App

A **Flask-based Image Steganography Web App** that allows users to **hide secret messages** inside images (encryption) and **retrieve hidden messages** using a passcode (decryption).  

## 🚀 Features
- Hide text inside an image securely.
- Retrieve the hidden message using a passcode.
- Simple and user-friendly web interface.
- Supports **PNG, JPG, and JPEG** formats.

## 📌 Installation & Setup
### 1⃣ Install Dependencies  
Make sure you have **Python 3** installed. Then, install the required libraries:

```bash
pip install flask opencv-python
```

### 2⃣ Clone or Download the Repository  
```bash
git clone https://github.com/your-repository/image-steganography.git
cd image-steganography
```

### 3⃣ Run the Flask App  
```bash
python app.py
```

### 4⃣ Open in Browser  
Go to: **http://127.0.0.1:5000/**  

---

## 🖥️ How to Use
### 🔐 Encrypt a Message:
1. Click **"Encrypt Message"** on the homepage.
2. Upload an image.
3. Enter your secret message.
4. Set a **passcode** for decryption.
5. Click **"Encrypt & Download"** to get the encrypted image.

### 🔓 Decrypt a Message:
1. Click **"Decrypt Message"** on the homepage.
2. Upload the **encrypted image**.
3. Enter the **passcode** used during encryption.
4. Click **"Decrypt"** to reveal the hidden message.

---

## 💁‍♂️ Project Structure
```
📂 image-steganography/
│-- 📂 static/
│   ├── 📂 uploads/        # Stores uploaded & encrypted images
│-- 📂 templates/          # HTML files for UI
│   ├── index.html         # Homepage
│   ├── encrypt.html       # Encryption page
│   ├── decrypt.html       # Decryption page
│-- app.py                 # Flask backend
│-- README.md              # Project documentation
```

---

## 🌍 Deployment
To deploy this app on a cloud server like **Heroku** or **Render**, follow these steps:

1. **Install Gunicorn (for production)**  
   ```bash
   pip install gunicorn
   ```
2. **Create a `Procfile` for Heroku**  
   ```
   web: gunicorn app:app
   ```
3. **Push to a hosting platform (e.g., Render, Heroku, or AWS).**

---

## 🛠️ Technologies Used
- **Python** (Flask, OpenCV)
- **HTML, CSS** (Bootstrap for UI)
- **Flask Flash Messages** (For error handling)

---

## 🐜 License
This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author
- **Fakruddin**
- 💎 Email: fakruddin4121@gmail.com
- 🔗 [LinkedIn](https://linkedin.com/in/your-profile)

