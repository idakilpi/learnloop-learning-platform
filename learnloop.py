import os
from dataclasses import dataclass
import sympy as sp
import gradio as gr

# --- Config ---
LEVELS = ("Beginner", "Intermediate", "Advanced")

@dataclass
class TutorConfig:
    default_level: str = "Beginner"

CFG = TutorConfig()

# --- Core (LLM-stub + SymPy) ---
def verify_math(expr_str: str) -> str:
    try:
        expr = sp.sympify(expr_str)
        simplified = sp.simplify(expr)
        return f"Simplified: ${sp.latex(simplified)}$"
    except Exception as e:
        return f"Could not verify with SymPy: {e}"

def structured_answer(question: str, level: str, step_by_step: bool) -> str:
    intro = f"Level: **{level}**  |  Mode: {'step-by-step' if step_by_step else 'concise'}"
    if any(ch in question for ch in "+-*/=^") or question.lower().startswith(("simplify", "derive", "integrate")):
        sympy_note = verify_math(question)
    else:
        sympy_note = "No math verification needed."
    if step_by_step:
        body = "\n".join([
            "1) Rephrase the question in simpler terms.",
            "2) Identify the key concept(s).",
            "3) Work through the solution methodically.",
            "4) Summarize and suggest a follow-up exercise."
        ])
    else:
        body = "Here's a concise explanation based on core concepts."
    return f"{intro}\n\n**Answer (stub):** This is a minimal placeholder response. Replace with an LLM.\n\n**SymPy check:** {sympy_note}\n\n{body}"

# --- UI ---
def tutor_ui(question: str, level: str, step_by_step: bool):
    return structured_answer(question.strip(), level, step_by_step)

def build_app():
    with gr.Blocks(title="LearnLoop — adaptive learning platform") as demo:
        gr.Markdown("# LearnLoop — adaptive learning platform")
        gr.Markdown("Ask about math, programming, or grammar. SymPy validates math expressions.")

        with gr.Row():
            question = gr.Textbox(label="Your question", placeholder="e.g., simplify (x^2 - 1)/(x - 1)")
        with gr.Row():
            level = gr.Dropdown(choices=list(LEVELS), value=CFG.default_level, label="Level")
            step = gr.Checkbox(value=True, label="Step-by-step")
        submit = gr.Button("Explain")
        output = gr.Markdown(label="Answer")
        submit.click(fn=tutor_ui, inputs=[question, level, step], outputs=output)
    return demo

def main():
    port = int(os.getenv("PORT", "7860"))
    app = build_app()
    app.launch(server_name="0.0.0.0", server_port=port, show_api=False)

if __name__ == "__main__":
    main()
