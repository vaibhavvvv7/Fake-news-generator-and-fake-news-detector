# 📰 Credible News: Fake News Generator & Detector

![Credible News](https://img.shields.io/badge/Status-Active-success)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Enabled-red)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)

Welcome to **Credible News**, a powerful web application designed to both generate fictional news stories using **GPT-2** and detect the authenticity of news text using **BERT**. This platform provides an intuitive, customized UI integrated seamlessly with state-of-the-art Natural Language Processing models.

## ✨ Features

- **📝 Fake News Generator**: Provide a prompt, and the app leverages the `gpt2` model to generate up to 400 words of realistic-sounding continuation text using dynamic nucleus sampling.
- **🔍 News Credibility Assessor**: Paste an article, claim, or news snippet, and the app uses an `AutoModelForSequenceClassification` built on `bert-base-uncased` to determine if it is Real 🟩 or Fake 🟥, complete with a confidence score.
- **🎨 Modern UI/UX**: A sleek, dark theme with glassmorphism effects, gradient text, loading animations, and responsive design.
- **⚡ Super-Fast Backend**: The backend operates on **FastAPI**, ensuring highly concurrent, robust, and exceptionally fast API endpoints.
- **🚀 GPU Acceleration Supported**: The application automatically checks for CUDA availability via PyTorch and runs predictions on the GPU if accessible, seamlessly falling back to CPU if not.

## 🛠️ Technology Stack

- **Backend**: FastAPI, PyTorch, Uvicorn, Pydantic
- **Machine Learning**: Hugging Face `transformers` library (`GPT2LMHeadModel`, `GPT2Tokenizer`, `AutoModelForSequenceClassification`)
- **Frontend**: HTML5, CSS3, JavaScript (Frontend Fetch API)

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/vaibhavvvv7/Fake-news-generator-and-fake-news-detector.git
   cd Fake-news-generator-and-fake-news-detector
   ```

2. **Create a Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   Install the required Python packages utilizing PyPI:
   ```bash
   pip install torch transformers fastapi uvicorn pydantic
   ```
   *(Note: Ensure you have installed the correct `torch` version matching your system's CUDA capabilities. For GPU support, check [PyTorch's official installation guide](https://pytorch.org/get-started/locally/).)*

4. **Run the Application**
   Launch the FastAPI application on the default port (8000):
   ```bash
   python app.py
   # OR
   python "credible news.py"
   ```

5. **Access the Web Interface**
   Open your preferred web browser and navigate to:
   ```text
   http://localhost:8000
   ```
   The application will load the frontend interface in your browser.

## 📂 Project Structure

- `app.py` / `credible news.py` - The central FastAPI server handling API routes (`/api/generate` and `/api/detect`) and ML model definitions.
- `index.html` - The modern, front-facing UI logic calling the async endpoints.
- `about.html` - An informational page containing details about the creation and scope of the project.
- `contact.html` - A contact directory supporting the user experience.

## 🧠 Models Under The Hood

- **Text Generation**: [GPT-2 Language Model](https://huggingface.co/gpt2) curated by OpenAI.
- **Sequence Classification**: Pre-trained [BERT (Bidirectional Encoder Representations from Transformers)](https://huggingface.co/bert-base-uncased) adapted for a binary real-vs-fake sequence classification task.

## 🤝 Contributing

Contributions are highly welcome! To contribute:
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---
*⚠️ **Disclaimer**: This tool is designed for educational, research, and entertainment purposes. The text generated under "fake news" should not be utilized in bad faith or misrepresented as genuine information.*
