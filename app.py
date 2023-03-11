import openai
import gradio as gr

openai.api_key = "<your api key>"

model_engine = "text-davinci-003"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

io = gr.Interface(
    generate_response,
    inputs=gr.inputs.Textbox("Enter Prompt Here"),
    outputs=gr.outputs.Textbox(),
)

io.launch(share=True)