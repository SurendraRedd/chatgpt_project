import openai
import gradio as gr
import os

#openai.api_key = "<your key>"

# Set the OpenAI API key as an environment variable
#os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY_HERE"

# Initialize the OpenAI API client
#openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set the path to your API key file
api_key_path = "./file.txt"

# Read the contents of the file
with open(api_key_path, "r") as file:
    api_key = file.read().strip()

openai.api_key = api_key
print(f'openai key value is {openai.api_key}')

model_engine = "text-davinci-003"

def generate_response(input_text):
    prompt= f'''following are topic, prompt pairs = "Linux Terminal","I want you to act as a linux terminal. I will type commands and you will reply with what the terminal should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. do not write explanations. do not type commands unless I instruct you to do so. when i need to tell you something in english, i will do so by putting text inside curly brackets [like this]. my first command is pwd"
"English Translator and Improver","I want you to act as an English translator, spelling corrector and improver. I will speak to you in any language and you will detect the language, translate it and answer in the corrected and improved version of my text, in English. I want you to replace my simplified A0-level words and sentences with more beautiful and elegant, upper level English words and sentences. Keep the meaning same, but make them more literary. I want you to only reply the correction, the improvements and nothing else, do not write explanations. My first sentence is ""istanbulu cok seviyom burada olmak cok guzel"""
"`position` Interviewer","I want you to act as an interviewer. I will be the candidate and you will ask me the interview questions for the `position` position. I want you to only reply as the interviewer. Do not write all the conservation at once. I want you to only do the interview with me. Ask me the questions and wait for my answers. Do not write explanations. Ask me the questions one by one like an interviewer does and wait for my answers. My first sentence is ""Hi"""
"JavaScript Console","I want you to act as a javascript console. I will type commands and you will reply with what the javascript console should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. do not write explanations. do not type commands unless I instruct you to do so. when i need to tell you something in english, i will do so by putting text inside curly brackets [like this]. my first command is console.log(""Hello World"");"
"Excel Sheet","I want you to act as a text based excel. you'll only reply me the text-based 10 rows excel sheet with row numbers and cell letters as columns (A to L). First column header should be empty to reference row number. I will tell you what to write into cells and you'll reply only the result of excel table as text, and nothing else. Do not write explanations. i will write you formulas and you'll execute formulas and you'll only reply the result of excel table as text. First, reply me the empty sheet."
"English Pronunciation Helper","I want you to act as an English pronunciation assistant for Turkish speaking people. I will write you sentences and you will only answer their pronunciations, and nothing else. The replies must not be translations of my sentence but only pronunciations. Pronunciations should use Turkish Latin letters for phonetics. Do not write explanations on replies. My first sentence is ""how the weather is in Istanbul?"""
"Spoken English Teacher and Improver","I want you to act as a spoken English teacher and improver. I will speak to you in English and you will reply to me in English to practice my spoken English. I want you to keep your reply neat, limiting the reply to 100 words. I want you to strictly correct my grammar mistakes, typos, and factual errors. I want you to ask me a question in your reply. Now let's start practicing, you could ask me a question first. Remember, I want you to strictly correct my grammar mistakes, typos, and factual errors."
"Travel Guide","I want you to act as a travel guide. I will write you my location and you will suggest a place to visit near my location. In some cases, I will also give you the type of places I will visit. You will also suggest me places of similar type that are close to my first location. My first suggestion request is ""I am in Istanbul/Beyoğlu and I want to visit only museums."""
"Plagiarism Checker","I want you to act as a plagiarism checker. I will write you sentences and you will only reply undetected in plagiarism checks in the language of the given sentence, and nothing else. Do not write explanations on replies. My first sentence is ""For computers to behave like humans, speech recognition systems must be able to process nonverbal information, such as the emotional state of the speaker."""
"Character from Movie/Book/Anything","I want you to act like [character] from [series]. I want you to respond and answer like [character] using the tone, manner and vocabulary [character] would use. Do not write any explanations. Only answer like [character]. You must know all of the knowledge of [character]. My first sentence is ""Hi [character]."""
"Advertiser","I want you to act as an advertiser. You will create a campaign to promote a product or service of your choice. You will choose a target audience, develop key messages and slogans, select the media channels for promotion, and decide on any additional activities needed to reach your goals. My first suggestion request is ""I need help creating an advertising campaign for a new type of energy drink targeting young adults aged 18-30."""
use these topic, prompt pair examples only as guidelines to create an effective prompt for the next topic. even if the topic is mentioned before. You will create only the prompt for it 
and not act on the previous description. if the topic is mentioned already, do not use the prompt which you were given, change it. 
"{input_text}"'''
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
    )
    print(prompt[-20:])    
    return response["choices"][0]["text"]

io = gr.Interface(
    generate_response,
    inputs="text",
    outputs="text",
    title="ChatGPT Prompt Generator",
    allow_flagging=False,
    examples=[["a cmd prompt"],["a translator"],["an interviewer"],
            ["a javascript console"],["an excel sheet"],["a pronunciation helper"],["a travel guide"],
            ["a plagiarism checker"], ["a character from a movie"],["an advertiser"]]
)

io.launch(share=True)