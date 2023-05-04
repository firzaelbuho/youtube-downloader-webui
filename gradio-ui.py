
from gradio.mix import Parallel
import requests
from io import BytesIO
import gradio as gr
from PIL import Image


def reverse(url, pict):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # img = Image.open("logo.png")
    
    return pict, img.convert('RGB')
demo = gr.Interface(
    fn = reverse, 
    inputs = [gr.Textbox(label="Addition"), gr.Image(label="input")], 
    outputs= [gr.Image(label="Addition"), gr.Image(label="img output")]
)
demo.launch()