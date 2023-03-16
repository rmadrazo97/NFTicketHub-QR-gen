# Django QR Code Generator
This is a Django web server that generates a QR code image with a unique ID, title, subtitle, and a banner image between the subtitle and the QR code. Additionally, it adds a gradient border with a blue top and a red bottom. The resulting image is then uploaded to Firebase Storage, and its public URL is stored in the Firebase Realtime Database.

# Requirements
Python 3.6 or higher
Django 4.1.2 or higher
qrcode library
pillow (Python Imaging Library, PIL) library
requests library
firebase-admin library
Install the required libraries using pip:

``` pip install -r requirements.txt ```

## Setup
Set up a Firebase project and enable Storage and Realtime Database.
Download the service account key file (JSON) for your Firebase project.
Replace the placeholders in the qr_code_app/config.py file with your Firebase project information:
"path/to/your-service-account-key.json": The path to your service account key file.
"your-firebase-storage-bucket-url": The URL of your Firebase Storage bucket.
"your-firebase-database-url": The URL of your Firebase Realtime Database.

## Usage
Run the Django server:

``` python manage.py runserver ```
Visit http://127.0.0.1:8000/qr-code/generate-qr-code/ to generate a QR code, upload it to Firebase Storage, and save its public URL to the Firebase Realtime Database. The server will return a JSON response containing the public URL of the generated QR code.

## Customization
- You can customize the title, subtitle, and banner URL by modifying the main function in the qr_code_app/qr_code_utils.py file:


```
def main():
    unique_id = str(uuid.uuid4())
    title = "Your Title"
    subtitle = "Your Subtitle"
    banner_url = "https://example.com/path/to/your/banner/image.jpg"
    # ...
```
- You can customize the font used for the title and subtitle by modifying the font variable in the create_qr_code_with_text function within the qr_code_app/qr_code_utils.py file. Provide the path to the desired font file and the font size:

```font = ImageFont.truetype("path/to/your/font.ttf", font_size)```
- You can adjust the border width by modifying the border_w variable in the add_gradient_border function within the qr_code_app/qr_code_utils.py file. Set it to the desired width (in pixels):

```border_w = 20  # Change this value to your desired border width```
- You can change the colors of the gradient border by modifying the start_color and end_color arguments in the create_gradient_border function calls within the add_gradient_border function in the qr_code_app/qr_code_utils.py file:

``` left_border = create_gradient_border(border_w, img_h, "start_color", "end_color") ```