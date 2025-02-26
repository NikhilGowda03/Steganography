from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import cv2
import os

app = Flask(__name__)
app.secret_key = "secret123"
UPLOAD_FOLDER = "static/uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to encode a message into an image
def encode_message(image_path, message, passcode):
    img = cv2.imread(image_path)
    if img is None:
        return None, "Invalid Image"

    hidden_data = passcode + "|" + message + "\0"
    d = {chr(i): i for i in range(256)}

    n, m, z = 0, 0, 0
    height, width, _ = img.shape

    for char in hidden_data:
        img[n, m, z] = d[char]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == width:
                m = 0
                n += 1
                if n == height:
                    return None, "Message too long for image"

    encoded_path = os.path.join(UPLOAD_FOLDER, "encoded_image.png")
    cv2.imwrite(encoded_path, img)
    return encoded_path, "Success"

# Function to decode a message from an image
def decode_message(image_path, passcode):
    img = cv2.imread(image_path)
    if img is None:
        return None, "Invalid Image"

    c = {i: chr(i) for i in range(256)}
    message = ""
    n, m, z = 0, 0, 0
    height, width, _ = img.shape

    while True:
        char = c[img[n, m, z]]
        if char == '\0':
            break
        message += char
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == width:
                m = 0
                n += 1
                if n == height:
                    break

    if '|' not in message:
        return None, "Decryption failed"
    
    stored_passcode, decrypted_message = message.split('|', 1)

    if stored_passcode == passcode:
        return decrypted_message, "Success"
    else:
        return None, "Incorrect passcode"

# Home page
@app.route('/')
def index():
    return render_template('index.html', title="Steganography Tool")

# Encrypt page
@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        file = request.files['image']
        message = request.form['message']
        passcode = request.form['passcode']

        if file and message and passcode:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            encoded_path, status = encode_message(file_path, message, passcode)
            if status == "Success":
                flash("Image encoded successfully! Download your image below.", "success")
                return send_file(encoded_path, as_attachment=True)
            else:
                flash(status, "danger")
    
    return render_template('encrypt.html', title="Encrypt Message")

# Decrypt page
@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        file = request.files['image']
        passcode = request.form['passcode']

        if file and passcode:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            message, status = decode_message(file_path, passcode)
            if status == "Success":
                flash(f"Decrypted Message: {message}", "success")
            else:
                flash(status, "danger")
    
    return render_template('decrypt.html', title="Decrypt Message")

if __name__ == '__main__':
    app.run(debug=True)
