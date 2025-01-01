from flask import Flask, request, render_template
import qrcode
import io
import base64

# Initialize Flask App
app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Generate QR Code Route
@app.route('/generate', methods=['POST'])
def generate_qr():
    # Get the data from the form
    data = request.form.get('data')

    if not data:
        return "Error: No data provided!", 400

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image for the QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save image to an in-memory file
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Encode image to base64
    qr_code_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Render the page with the QR code
    return render_template('index.html', qr_code=qr_code_base64)

if __name__ == "__main__":
    app.run(debug=True)
