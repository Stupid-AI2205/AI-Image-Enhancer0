# AI Image Enhancer

An AI-powered image enhancement and super-resolution application built with Python, FastAPI, and Real-ESRGAN.

## Features

- AI-powered image enhancement
- 4× image upscaling
- Supports JPG, PNG and WEBP
- FastAPI backend
- Modern web frontend
- Before/after image preview
- Download enhanced images
- CPU-compatible inference

## Tech Stack

### Backend
- Python
- FastAPI
- OpenCV
- PyTorch
- Real-ESRGAN
- BasicSR

### Frontend
- HTML
- CSS
- JavaScript

## Project Structure

```text
AI-Image-Enhancer/
│
├── backend/
│   ├── main.py
│   ├── enhancer.py
│   ├── test_enhancer.py
│   ├── models/
│   ├── uploads/
│   └── outputs/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
├── README.md
└── requirements.txt