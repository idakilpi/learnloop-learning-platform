# LearnLoop — adaptive learning platform

An AI-based tutoring web app for step-by-step explanations in math, programming, and grammar. Adjusts responses to the learner’s level (Beginner / Intermediate / Advanced) and can operate in English and Finnish.

## Features
- Adaptive difficulty control (Beginner / Intermediate / Advanced)
- Step-by-step reasoning; solution verification for math via **SymPy**
- Follow-up practice exercise generation after each solved question
- Guardrails to prevent unsafe or irrelevant code suggestions
- User-friendly chat UI with **Gradio**
- Deployed for real-time use on **Hugging Face Spaces**
- Future-ready for scalable backend (e.g., user progress database)

## Tech Stack (decided)
- **Interface:** Gradio (Python)
- **Deployment:** Hugging Face Spaces
- **LLMs (instruction-tuned, open-source):**
  - Primary: **Qwen2.5-7B-Instruct**
  - Alternatives: **Mistral-7B-Instruct-v0.3**, **Llama-3-Instruct**
- **Math engine:** SymPy for symbolic verification
- **Languages:** Finnish and English
- **Model usage:** Start with pretrained models + prompt engineering & structured outputs; optional later fine-tuning on small domain datasets

## Data / Evaluation (initial)
- No new dataset initially
- Use existing open datasets for evaluation/adaptation:
  - **GSM8K** (math), **CodeAlpaca** (programming Q&A), grammar-correction sets
- May generate small synthetic QA sets to test reasoning consistency

## Setup
1. Clone the repo
2. Create a Python env (≥ 3.10) and install deps
3. (If needed) set environment variables in `.env`
4. Run the Gradio app

```bash
# example
pip install -r requirements.txt
python app.py  # or: python -m learnloop.app

