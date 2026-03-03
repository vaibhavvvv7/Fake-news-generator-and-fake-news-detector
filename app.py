import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn


# ✅ Check device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# ✅ Load Models
gpt2_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
gpt2_model = GPT2LMHeadModel.from_pretrained("gpt2").to(device)


bert_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
bert_model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-uncased", num_labels=2
).to(device)


# ✅ Generate Fake News
def generate_fake_news(prompt):
    inputs = gpt2_tokenizer.encode(prompt, return_tensors="pt").to(device)
    outputs = gpt2_model.generate(
        inputs,
        max_length=400,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        early_stopping=True
    )
    generated_text = gpt2_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text


# ✅ Detect Fake or Real News
def detect_news(text):
    inputs = bert_tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(device)
    with torch.no_grad():
        outputs = bert_model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    confidence = torch.softmax(logits, dim=1)[0][predicted_class].item()
    label = "🟥 It is a Fake News" if predicted_class == 0 else "🟩 It is a Real News"
    return f"{label} (Confidence: {confidence:.2f})"


# ✅ FastAPI Setup
app = FastAPI()

class GenerateRequest(BaseModel):
    prompt: str

class DetectRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get("/about")
def read_about():
    return FileResponse("about.html")

@app.get("/contact")
def read_contact():
    return FileResponse("contact.html")

@app.post("/api/generate")
def api_generate(req: GenerateRequest):
    try:
        return {"result": generate_fake_news(req.prompt)}
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/detect")
def api_detect(req: DetectRequest):
    try:
        return {"result": detect_news(req.text)}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0
