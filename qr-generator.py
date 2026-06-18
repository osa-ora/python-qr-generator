import argparse
import qrcode
from PIL import Image


def generate_qr_with_logo(
    url: str, logo_path: str = None, output_file: str = "qr_with_logo.png"
):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Only process the logo if a path was actually provided
    if logo_path:
        try:
            logo = Image.open(logo_path)
            qr_width, qr_height = img.size

            # Logo size = 20% of QR width
            logo_size = qr_width // 5
            logo.thumbnail((logo_size, logo_size))

            pos = ((qr_width - logo.width) // 2, (qr_height - logo.height) // 2)

            if logo.mode == "RGBA":
                img.paste(logo, pos, logo)
            else:
                img.paste(logo, pos)
        except Exception as e:
            print(f"Warning: Could not load logo from {logo_path}. Generating plain QR instead. Error: {e}")

    img.save(output_file)
    print(f"QR code saved to: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a QR code with an optional logo embedded in the center."
    )

    parser.add_argument(
        "-u", "--url", required=True, help="The URL or text to encode in the QR code"
    )
    
    # Removed required=True and added default=None
    parser.add_argument(
        "-l",
        "--logo",
        default=None,
        help="Path to the logo image file (Optional)",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="qr_with_logo.png",
        help="Path/name of the output QR code image (default: qr_with_logo.png)",
    )

    args = parser.parse_args()

    generate_qr_with_logo(
        url=args.url, logo_path=args.logo, output_file=args.output
    )