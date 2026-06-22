import qrcode
data = input("Enter Text or URL: ")
file_name = input("Enter File Name: ")
img = qrcode.make(data)
img.save(f"{file_name}.png")
print(f"QR Code saved as {file_name}.png")