import gradio as gr
from PIL import Image
import torchvision.transforms as transforms
import sys
import numpy as np
import torch
# trt_infer.py が存在するディレクトリへのパスを追加
sys.path.append('./models/blip2')
sys.path.append('./models/llama2')
from trt_infer import app_infer
from trt_info_gen import llama_infer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def preprocess(image):
    preprocess = transforms.Compose([
        # 解像度を下げるためにサイズを調整
        transforms.Resize((224, 224)),  # 解像度を低下させる
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    tensor = preprocess(image).to(device).to(torch.float16)
    # tensor=transforms.Resize(tensor,(224,224))
    # tensor=transforms.functional.to_tensor(image)
    return tensor

def image_to_tensor(image):
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    tensor = preprocess(image)
    return tensor

def process_image(image, genre_dropdown, genre_custom):
    image_tensor = image_to_tensor(image)
    genre = genre_custom if genre_custom.strip() != "" else genre_dropdown  # カスタムジャンルが入力されていればそれを使用
    prompts = [
        "question: How is the weather? answer:",
        "question: What features or landmarks stand out? answer: ",
        "question: How would you describe the overall composition of the image? answer: ",
        "question: What visual elements contribute to its impact?  answer : "
        "question: Discuss any unique characteristics or distinguishing features of the location depicted in the image. answer: ",
        "question: Where is this picture taken? answer : ",
        "question: What can tell from this picture? answer :"
    ]
    result_texts = app_infer(image_tensor, prompts)
    information_text = llama_infer(result_texts, genre)
    return information_text

iface = gr.Interface(
    fn=process_image,
    inputs=[
        gr.Image(),
        gr.Dropdown([
            "Culture and Arts",
            "History and Heritage",
            "Nature and Environment",
            "Science, Technology, and Exploration",
            "Cuisine and Lifestyle"
        ], label="Genre (Predefined)"),
        gr.Textbox(label="Genre (Custom)"),  # カスタムジャンル入力用
    ],
    outputs=gr.Text(),
    title="Travel Photo Analyzer",
    description="Upload a photo and select or enter a genre to generate information related to it."
)

if __name__ == "__main__":
    iface.launch()
