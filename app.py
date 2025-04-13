import gradio as gr

import google.generativeai as genai

genai.configure(api_key="AIzaSyA9QCGSLbsYMlcQHjogtyY_QNYHUtYelLg")

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
response = model.generate_content("Give me a 1-week study plan for becoming a data analyst.")
print(response.text)


# 📄 Prompt template
def generate_plan(role, goal, style, hours):
    prompt = f"""
    You are a career coach. Create a personalized 6-month professional development plan.

    Current Role: {role}
    Career Goal: {goal}
    Preferred Learning Style: {style}
    Available Weekly Hours: {hours}

    The plan should include:
    - Key skill areas to develop
    - Weekly or monthly action steps
    - Recommended resources (courses, books, projects)
    - Progress milestones
    - Motivational advice
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating plan: {e}"

# 🖼️ Gradio UI using Blocks
with gr.Blocks(css="footer {display:none !important}") as app:
    gr.Markdown("# 🌱 Professional Development Plan Creator")

    with gr.Row():
        with gr.Column():
            role = gr.Textbox(label="Your Current Role", placeholder="e.g. Junior Data Analyst")
            goal = gr.Textbox(label="Career Goal", placeholder="e.g. Become a Data Scientist")
        with gr.Column():
            style = gr.Dropdown(
                ["Reading", "Online Courses", "Hands-on Projects", "Mixed"],
                label="Preferred Learning Style",
                value="Mixed"
            )
            hours = gr.Slider(1, 40, value=5, step=1, label="Available Weekly Hours")

    generate_btn = gr.Button("Generate Plan 🚀")
    output = gr.Textbox(label="Your Personalized Development Plan", lines=25, interactive=False)

    generate_btn.click(fn=generate_plan, inputs=[role, goal, style, hours], outputs=output)

# 🖥️ Launch the app
if __name__ == "__main__":
    app.launch()
