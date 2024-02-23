# 🌍 TravelerEye: Visual Exploration Tool

Welcome to **TravelerEye** 📸, a cutting-edge visual exploration tool that leverages the power of AI 🤖 to enhance your photo experiences. Utilizing state-of-the-art models like **BLIP-2** and **Llama2**, TravelerEye provides intuitive genre selection and photo analysis capabilities.

![TravelerEye Interface](path_to_your_demo_image_here)

## 🌟 TravelerEye Overview

**TravelerEye** is designed to transform the way you interact with your travel photos. This innovative application uses artificial intelligence to analyze images and provide insights into the culture, natural environment, and ambiance of the places you've visited. Whether you're on a solo journey, reminiscing about a past trip, or enjoying family memories, TravelerEye offers a unique way to connect with your travel experiences.

### Key Features

- **Cultural Insights**: Discover the cultural background of your travel destinations based on your photos 🏰.
- **Natural Environment Analysis**: Learn about the flora, fauna, and landscapes captured in your images 🏞.
- **Memory Lane**: Revisit the essence of your travels and relive your adventures through an AI-powered lens 🔍.
- **Family Fun**: Share and enjoy memories with your family, letting TravelerEye reveal the story behind each photo 👨‍👩‍👧‍👦.

TravelerEye is perfect for:
- **Solo Travelers** 🚶: Gain deeper insights into your solo adventures by understanding the places you visit through the photos you take.
- **Memory Keepers** 📖: Use TravelerEye to recall the details and stories of the places you've been, making every photo a gateway to the past.
- **Families** 👪: Enjoy quality time with loved ones as TravelerEye helps narrate the stories of family trips, making every photo session a journey of discovery.



## Installation

Before diving into the visual world of TravelerEye, you'll need to set up your environment. Follow these steps to get started:
- install NVIDIA Container
follow [Nvidia Container toolkit installation guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
- start docker container
```bash
docker run --gpus all --entrypoint /bin/bash -it nvidia/cuda:12.1.0-devel-ubuntu22.04
```
- Setting Up the Environment
```bash

apt-get update && apt-get -y install python3.10 python3-pip openmpi-bin libopenmpi-dev git
pip3 install tensorrt_llm -U --pre --extra-index-url https://pypi.nvidia.com
git clone --recursive https://github.com/otyanokosaisai/TravelerEye.git
cd TravelerEye
pip3 install gradio

```

### Prerequisites

We prepare llama2 and blip2 accelerated by TensorRT-llm. This project uses these large model files not stored directly in this repository. Please download the necessary files and place them in the respective directories.
If you want to use other models, you can make the accelerated models by using [TensorRT-llm](https://github.com/NVIDIA/TensorRT-LLM.git).

#### Model Files

- **BLIP-2 and Llama2 Models**: Download the model files to ensure the application runs smoothly.

  - [Download Model Files (ZIP)](https://drive.google.com/file/d/1UIgEps1LL7jehNJezSvaqGDhclOHqjG-/view?usp=sharing)
    - `[blip2/rank0.plan]` - Place it at `models/blip2/trt_engine/blip-2-opt-2.7b/fp16/1-gpu/rank0.engine`
    - `[blip2/Qformer_fp16.plan]` -Place it at `models/blip2/plan/Qformer/Qformer_fp16.plan`
    - `[blip2/visual_encoder_fp16.plan]` - Place it at `models/blip2/plan/visual_encoder/visual_encoder_fp16.plan`
    - `[Llama2/rank0.engine]` - Place it at `models/llama2/engine/rank0.engine`

  - [Download Model Files (pt)](https://drive.google.com/file/d/1hI6da39QVX70ZKxbm4EQKwRzBoJevOal/view?usp=sharing)
    - `[query_tokens.pt]` Place it at `models/blip2/query_tokens.pt`

### 🚀　Usage
Run the application with the following command:

```bash

python3 app.py

```

Access TravelerEye by navigating to `http://127.0.0.1:7860` in your web browser. Once there, you can begin the exploration by uploading a photo. After uploading, you have the option to select a genre from the predefined list or type your own to specify a unique genre. The predefined genres include:

- "Culture and Arts"
- "History and Heritage"
- "Nature and Environment"
- "Science, Technology, and Exploration"
- "Cuisine and Lifestyle"

This feature allows you to tailor the analysis to your specific interests, providing insights and information relevant to the genre of your choice. Whether you're interested in the cultural significance of your travel destinations, the natural beauty of the landscapes you've captured, or the culinary delights you've experienced, TravelerEye is designed to enhance your photo exploration experience.



## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgments

- Thanks to Salesforce, Inc. for developing BLIP-2.
- Thanks to NVIDIA for providing TensorRT-llm.
- Thanks to Meta Platforms, Inc. for making Llama2 available to the community.



