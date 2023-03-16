import os
import uuid
import qrcode
import requests
from io import BytesIO
from PIL import ImageOps
from PIL import Image, ImageDraw, ImageFont
from firebase_admin import storage
from firebase_config import firebase_app 

# Load your Firebase project
bucket = storage.bucket(app=firebase_app)

def create_gradient_border(width, height, start_color, end_color):
    gradient = Image.linear_gradient("L")
    gradient = ImageOps.colorize(gradient, start_color, end_color)
    gradient = gradient.resize((width, height))
    return gradient

def add_gradient_border(image):
    img_w, img_h = image.size
    border_w = 15

    color1 = "#11998e"
    color2 = "#38ef7d"

    # Create gradient border
    left_border = create_gradient_border(border_w, img_h, color1, color2)
    top_border = create_gradient_border(img_w + 2 * border_w, border_w, color1, color1)
    right_border = left_border.transpose(Image.FLIP_LEFT_RIGHT)
    bottom_border = create_gradient_border(img_w + 2 * border_w, border_w, color2, color2)

    # Create new canvas with border
    canvas = Image.new("RGBA", (img_w + 2 * border_w, img_h + 2 * border_w), (255, 255, 255, 0))
    canvas.paste(left_border, (0, 0))
    canvas.paste(top_border, (border_w, 0))
    canvas.paste(right_border, (img_w + border_w, 0))
    canvas.paste(bottom_border, (border_w, img_h + border_w))
    canvas.paste(image, (border_w, border_w))

    return canvas

def create_qr_code_with_text(unique_id, title, subtitle, banner_url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data("https://api.whatsapp.com/send?phone=34677893008&text=Ticket%20Unique%20ID:%20"+unique_id)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_w, img_h = img.size

    # Download banner image
    response = requests.get(banner_url)
    banner = Image.open(BytesIO(response.content))
    banner_w, banner_h = banner.size

    # Calculate new banner size to fit the canvas width
    new_banner_h = int((img_w / banner_w) * banner_h)
    banner = banner.resize((img_w, new_banner_h))

    # Add title, subtitle, and banner to the canvas
    canvas = Image.new("RGBA", (img_w, img_h + 60 + new_banner_h), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()

    title_w, title_h = draw.textsize(title, font)
    subtitle_w, subtitle_h = draw.textsize(subtitle, font)

    draw.text(((img_w - title_w) // 2, 10), title, font=font, fill="black")
    draw.text(((img_w - subtitle_w) // 2, 40), subtitle, font=font, fill="black")
    canvas.paste(banner, (0, 60))
    canvas.paste(img, (0, 60 + new_banner_h))

    # Add gradient border
    canvas_with_border = add_gradient_border(canvas)

    return canvas_with_border

def upload_image_to_firebase(image):
    unique_id = str(uuid.uuid4())
    file_path = f"qrcodes/{unique_id}.png"
    image.save(file_path, "PNG")

    bucket = storage.bucket()
    blob = bucket.blob(file_path)
    blob.upload_from_filename(file_path)

    blob.make_public()
    return blob.public_url

def save_url_to_database(url):
    ref = db.reference("qrcodes")
    ref.push(url)

# def main():
#     unique_id = str(uuid.uuid4())
#     title = "Real Madrid CF vs Liverpool FC"
#     subtitle = "European Cup 2022-23 - Round of 16"
#     banner_url = "https://estaticos.esmadrid.com/cdn/farfuture/cOhhvW6sHt7weOXD_z0clOoXXmm7EcO_T4Wn2USU7Ik/mtime:1667830662/sites/default/files/eventos/eventos/real_madrid_-_liverpool_fc_uefa_champions_league.jpg"
#     qr_image = create_qr_code_with_text(unique_id, title, subtitle, banner_url)
#     public_url = upload_image_to_firebase(qr_image)
#     save_url_to_database(public_url)

#     print(f"QR code image uploaded to: {public_url}")
    
#     return public_url

# if __name__ == "__main__":
#     main()
