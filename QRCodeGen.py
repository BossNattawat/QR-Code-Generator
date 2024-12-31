import qrcode

data = input("Enter the text or URL: ").strip()
fileName = input("Enter the filename: ").strip()

qrCode = qrcode.QRCode(box_size=10, border=4)
qrCode.add_data(data)

image = qrCode.make_image(fill_color="black", back_color="white")
image.save(f"{fileName}.jpg")

print(f"QR code saved as {fileName}.jpg")