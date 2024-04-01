import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__, 
            static_folder='C:\\Users\\user\\OneDrive\\Masaüstü\\SENG438\\static',  # static klasörünü belirt
            template_folder='C:\\Users\\user\\OneDrive\\Masaüstü\\SENG438')


@app.route('/')
def index():
    return render_template('index.html', 
                           css=url_for('static', filename='styles.css'),
                           js=url_for('static', filename='script.js'),
                           img_home=url_for('static', filename='Images/Home2.png'),
                           img_weak=url_for('static', filename='Images/Weak.png'),
                           img_weak2=url_for('static', filename='Images/Weak2.png'),
                           img_dribbling=url_for('static', filename='Images/Dribbling.png'),
                           img_dribbling2=url_for('static', filename='Images/Dribbling2.png'),
                           img_forward=url_for('static', filename='Images/Forward.png'),
                           img_forward2=url_for('static', filename='Images/Forward2.png'),
                           img_defender=url_for('static', filename='Images/Defender.png'),
                           img_defender2=url_for('static', filename='Images/Defender2.png'),
                           img_about=url_for('static', filename='Images/About.png'),
                           img_user=url_for('static', filename='Images/User.png'))

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            subject = request.form['subject']
            message = request.form['message']

            sender_email = "alanmuratcan15@gmail.com"  # Gönderen e-posta adresi
            receiver_email = "footballplayerss25@gmail.com"  # Alıcı e-posta adresi
            password = "tbxj izxk ovfh vqhc"  # Gönderen e-posta şifresi
            # Create email header and content
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            msg.attach(MIMEText(body, 'plain'))

            # Connect to SMTP server and send email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            
            print("SMTP server connection successful!")
            return jsonify({"success": True, "message": "Email sent successfully!"})
        except Exception as e:
            print(f"SMTP server connection error: {str(e)}")
            return jsonify({"success": False, "message": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
