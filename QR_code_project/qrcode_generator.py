import qrcode

def generate_qr_code(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()  

    text = lines[0].strip()
    filename = lines[1].strip()

    # Convert text or url to QR_code
    image_qrcode = qrcode.make(text)  # Create a QR code image

    # Save the QR code image
    image_qrcode.save(filename)  # Save the image in the project folder

# Generate the QR code from input.txt
generate_qr_code("a.txt")

