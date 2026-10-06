
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import FileResponse
import os
import uuid

from enhancer import ImageEnhancer

app = FastAPI(
    title="AI Image Enhancer",
    description="AI-powered image super-resolution API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "uploads"
)

OUTPUT_FOLDER = os.path.join(
    BASE_DIR,
    "outputs"
)


os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


print("Starting AI Image Enhancer...")

enhancer = ImageEnhancer()


@app.get("/")
def home():

    return {
        "message": "AI Image Enhancer API",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model": "Real-ESRGAN x4"
    }


@app.post("/enhance")
async def enhance_image(
    file: UploadFile = File(...)
):

    allowed_types = [
        "image/jpeg",
        "image/png",
        "image/webp"
    ]

    if file.content_type not in allowed_types:

        return {
            "error": "Only JPG, PNG and WEBP are supported."
        }


    extension = os.path.splitext(
        file.filename
    )[1]

    unique_id = str(uuid.uuid4())

    input_filename = (
        unique_id + extension
    )

    output_filename = (
        unique_id + "_enhanced.png"
    )


    input_path = os.path.join(
        UPLOAD_FOLDER,
        input_filename
    )

    output_path = os.path.join(
        OUTPUT_FOLDER,
        output_filename
    )


    contents = await file.read()

    with open(input_path, "wb") as f:

        f.write(contents)


    try:

        enhancer.enhance(
            input_path,
            output_path
        )

    except Exception as e:

        return {
            "error": str(e)
        }


    return {
        "message": "Image enhanced successfully",
        "output_file": output_filename,
        "download_url": (
            f"/download/{output_filename}"
        )
    }


@app.get("/download/{filename}")
def download_image(filename: str):

    file_path = os.path.join(
        OUTPUT_FOLDER,
        filename
    )

    if not os.path.exists(file_path):

        return {
            "error": "File not found."
        }


    return FileResponse(
        file_path,
        media_type="image/png",
        filename=filename
    )