from flask import Flask, render_template, request, send_file, redirect, url_for
import qrcode
import os

app = Flask(__name__)

# Define the path for saving the QR code image
QR_CODE_FOLDER = "static/"
QR_CODE_FILENAME = "qrcode_image.png"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get data from the form input
        data = request.form.get("data")

        if data:
            # Generate the QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            # Create and save the QR code image
            img = qr.make_image(fill="black", back_color="white")
            img.save(os.path.join(QR_CODE_FOLDER, QR_CODE_FILENAME))

            # Redirect to show the generated QR code
            return redirect(url_for("index"))

    # Render the form and QR code (if generated)
    return render_template("index.html", qr_code=QR_CODE_FILENAME)

if __name__ == "__main__":
    app.run(debug=True)
