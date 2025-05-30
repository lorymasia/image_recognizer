# Image Recognizer

Image Recognizer is a simple web application that allows automatic recognition of objects within images uploaded via a web interface, using the YOLOv8 model.

## Features

- **Image upload**: Upload an image from your computer for recognition.
- **Object recognition**: Uses YOLOv8 to identify and count the objects present in the image.
- **Web interface**: Minimal frontend based on FastAPI and Jinja2.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) for API and web server management.
- [Jinja2](https://jinja.palletsprojects.com/) for HTML template rendering.
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for image recognition.
- [Python 3.8+](https://www.python.org/)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lorymasia/image_recognizer.git
   cd image_recognizer
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the application:**
   Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

3. **Upload an image:**
   - On the homepage, select an image from your device and click "Upload".
   - The recognized objects and the count for each identified category will be shown.

## Project Structure

```
image_recognizer/
│
├── main.py               # Main FastAPI application
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates (index.html, upload.html)
└── .gitignore
```

## Notes

- The YOLOv8 model (`yolov8s.pt`) is automatically downloaded from Ultralytics if not already present.
- All uploaded images are temporarily saved on the server for processing.
- Make sure you have a compatible GPU for optimal performance, although the model can also run on CPU.

## License

This project is open source and released under the MIT license. See the LICENSE file for more details.
