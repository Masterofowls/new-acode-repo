import qrcode
from PIL import Image

def generate_qr_code(data: str, filename: str = "qrcode.png", box_size: int = 10, border: int = 4, fill_color: str = "black", back_color: str = "white"):
    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')
        img.save(filename)
        print(f"Success! QR Code saved as {filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url_data = "https://www.google.com"
    generate_qr_code(url_data, "my_qrcode.png")