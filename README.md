# QR Code Generator

A simple Python application that generates QR Codes from text or URLs and saves them as PNG images.

## Features

* Generate QR Codes from any text or URL
* Save QR Codes as PNG files
* Lightweight and easy to use
* Beginner-friendly Python project

## Tech Stack

* Python
* QRCode Library
* Pillow (PIL)

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/qrcode-Generator.git
cd qrcode-Generator
```

### Install Dependencies

```bash
pip install qrcode[pil]
```

## Usage

Run the application:

```bash
python main.py
```

Enter any text or URL when prompted:

```text
Enter Text or URL: https://github.com/AkashGautam-27
Enter File Name: GitHub
```

Output:

```text
QR Code Generated Successfully!
```

A file named `{File Name}.png` will be created in the project directory.

## Project Structure

```text
QR-Code-Generator/
│
├── main.py
└── README.md
```

## Sample Code

```python
import qrcode
data = input("Enter Text or URL: ")
file_name = input("Enter File Name: ")
img = qrcode.make(data)
img.save(f"{file_name}.png")
print(f"QR Code saved as {file_name}.png")
```

## Screenshots

Add your screenshots inside the project folder and reference them:

```md
## ScreenShot
![QR Code Generator](./assets/screenshot1.png)

## Generated QR Code
![Generated QR Code Linkedin](./assets/screenshot2.png)
```

## Future Enhancements

* GUI using Tkinter
* Custom QR Code colors
* Logo embedding in QR Codes
* Download location selection
* Batch QR Code generation

## Author

Akash Gautam

GitHub: https://github.com/AkashGautam-27

## License

This project is open source and available under the MIT License.
