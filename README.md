# QR Code Generator with Title, Subtitle, Banner, and Gradient Border
This Python script generates a QR code image with a unique ID, title, subtitle, and a banner image between the subtitle and the QR code. Additionally, it adds a gradient border with a blue top and a red bottom. The resulting image is then uploaded to Firebase Storage, and its public URL is stored in the Firebase Realtime Database.

## Requirements
Python 3.6 or higher
qrcode library
pillow (Python Imaging Library, PIL) library
requests library
firebase-admin library
Install the required libraries using pip:
```pip install qrcode pillow requests firebase-admin```

## Setup
Set up a Firebase project and enable Storage and Realtime Database.
Download the service account key file (JSON) for your Firebase project.
Replace the placeholders in the script with your Firebase project information:
"path/to/your-service-account-key.json": The path to your service account key file.
"your-firebase-storage-bucket-url": The URL of your Firebase Storage bucket.
"your-firebase-database-url": The URL of your Firebase Realtime Database.

### Usage
Set the desired title, subtitle, and banner URL in the main function:
```
def main():
    unique_id = str(uuid.uuid4())
    title = "Your Title"
    subtitle = "Your Subtitle"
    banner_url = "https://example.com/path/to/your/banner/image.jpg"
    # ...
```

### Run the script:
```python qr_code_generator.py```

The script will generate a QR code with the given title, subtitle, and banner image, and upload it to Firebase Storage. The public URL of the uploaded image will be saved to the Firebase Realtime Database.

### Functions
create_qr_code_with_text(unique_id: str, title: str, subtitle: str, banner_url: str) -> Image: Generates a QR code image with a unique ID, title, subtitle, and a banner image.
upload_image_to_firebase(image: Image) -> str: Uploads the given image to Firebase Storage and returns its public URL.
save_url_to_database(url: str) -> None: Saves the given URL to the Firebase Realtime Database.
main() -> None: The main function that coordinates the QR code generation, uploading, and saving the URL to the database.

### Customization
- You can customize the font used for the title and subtitle by modifying the font variable in the create_qr_code_with_text function. Provide the path to the desired font file and the font size:
```font = ImageFont.truetype("path/to/your/font.ttf", font_size)```

- You can adjust the border width by modifying the border_w variable in the add_gradient_border function. Set it to the desired width (in pixels):
```border_w = 20  # Change this value to your desired border width```

- You can change the colors of the gradient border by modifying the start_color and end_color arguments in the create_gradient_border function calls within the add_gradient_border function:
```left_border = create_gradient_border(border_w, img_h, "start_color", "end_color")```