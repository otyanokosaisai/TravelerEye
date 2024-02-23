# 🌍 TravelerEye: Visual Exploration Tool

Welcome to **TravelerEye** 📸, a cutting-edge visual exploration tool that leverages the power of AI 🤖 to enhance your photo experiences. Utilizing state-of-the-art models like **BLIP-2** and **Llama2**, TravelerEye provides intuitive genre selection and photo analysis capabilities.

![TravelerEye Interface](https://github.com/otyanokosaisai/TravelerEye/blob/master/TravelerEye_sample.png)

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

## System Requirements

To ensure the best experience and performance while using TravelerEye, your system should meet the following requirements:

- **GPU**: Nvidia GPU that supports TensorRT-llm, with VRAM of at least 16GB.
- **RAM**: Minimum of 32GB, though 64GB has been tested and recommended for optimal performance.
- **Storage**: At least 70GB of free space for installation and running the application.

Please note that these requirements are crucial for running the application smoothly and efficiently.

## Installation Guide

Follow these steps to set up TravelerEye on your system:

1. **NVIDIA Container Toolkit Installation**:
   Ensure that you have the NVIDIA Container Toolkit installed on your system. For detailed instructions, refer to the [Nvidia Container toolkit installation guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

2. **Start Docker Container**:
   Launch the Docker container with NVIDIA GPU support by running:
   ```bash
   docker run --gpus all --entrypoint /bin/bash -it nvidia/cuda:12.1.0-devel-ubuntu22.04
   ```
3. Update your package list and install necessary dependencies:
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
To start exploring with TravelerEye, follow these simple steps:

1. **Launch the Application**:
   Run TravelerEye using the following command:
   ```bash
   python3 app.py 
   ```
2. Accessing TravelerEye:
  Open your web browser and go to http://127.0.0.1:7860. Here, you can upload a photo to begin your exploration.

3. Genre Selection:
  After uploading your photo, choose a genre from the predefined list or type your own custom genre. Available genres include:
  
  - Culture and Arts
  - History and Heritage
  - Nature and Environment
  - Science, Technology, and Exploration
  - Cuisine and Lifestyle
  
  This feature allows you to tailor the analysis to your specific interests, providing insights and information relevant to the genre of your choice. Whether you're interested in the cultural significance of your travel destinations, the natural beauty of the landscapes you've captured, or the culinary delights you've experienced, TravelerEye is designed to enhance your photo exploration experience.
### custom genre example
- sightseeing
- science
- food

### attention
If you cannot access `http://127.0.0.1:7860` in your web browser, then fix firewall setting and if necessary use vscode.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgments

- Thanks to Salesforce, Inc. for developing BLIP-2.
- Thanks to NVIDIA for providing TensorRT-llm.
- Thanks to Meta Platforms, Inc. for making Llama2 available to the community.



## GenAIonRTX contest
This application is a submission to the **Nvidia GenAIonRTX contest(2024) Text-Based Applications**.
This project is tested on the following system.
- Windows11
- wsl2
- docker 24.0.7
- Nvidia RTX4090 laptop

## GenAIonRTX Contest Appeal

We are thrilled to present **TravelerEye** as our submission to the **Nvidia GenAIonRTX contest (2024) Text-Based Applications**. Our project harnesses the synergistic powers of BLIP-2 and Llama2-7b models, traditionally known for their intensive computational demands. With the integration of TensorRT-llm, we've achieved a monumental leap in performance, accelerating processing speeds by several folds. This breakthrough enables TravelerEye to extract meaningful insights from mere images, transforming them into rich narratives and interactive experiences.

### Problem Statement and Vision

In an era where social media proliferation has inadvertently contributed to the superficiality of family connections, TravelerEye aims to counteract this trend by deepening the shared experiences of past travels. Our application doesn't just recall memories; it reignites conversations, fosters shared joy, and strengthens bonds through the vivid storytelling of your journeys.

Moreover, TravelerEye addresses the common challenge faced during solo travels or trips without a guide. It empowers travelers to uncover the stories behind their surroundings and captured moments, solely based on their photographs. This feature not only enhances the travel experience but also serves as a virtual companion, providing context and insights that might otherwise require extensive research or a human guide.

### Enhancing Communication through Shared Photo Experiences

TravelerEye also innovates in the realm of social interactions, particularly in photo sharing among friends. By appending information derived from images, our application enriches conversations, adding layers of context and intrigue that facilitate smoother, more engaging communication. This feature is especially valuable in today's digital age, where meaningful interaction is often lost amidst the noise of constant content sharing.

### Conclusion

Our submission to the Nvidia GenAIonRTX contest is more than just an application; it's a tool designed to bridge gaps, create connections, and enhance the way we interact with our memories and the world around us. Powered by the cutting-edge acceleration of TensorRT-llm, TravelerEye stands at the forefront of AI-driven innovation, promising to revolutionize the way we perceive, share, and converse about our travel experiences.

We believe that TravelerEye not only showcases the potential of combining powerful AI models with advanced acceleration technologies but also addresses pressing social issues, making it a worthy contender in the GenAIonRTX contest. Our hope is that this platform will inspire more meaningful interactions, bring people closer, and make every travel memory a treasure worth sharing.

## demo movie

"Welcome to TravelerEye, the AI-driven platform that enriches the way we revisit our travel memories and discover the world around us."

"Imagine looking back at photos from a family vacation or a trip with friends. With TravelerEye, every photo becomes a gateway to shared memories, bringing stories to life with just a tap. Our app uses advanced NVIDIA AI technology, including BLIP-2 and Llama2 models, to provide context and insights that deepen your connection to those moments. Whether it's uncovering the cultural significance of a hidden gem or reliving the laughter shared under a foreign sky, TravelerEye makes reminiscing more meaningful."

"But TravelerEye's magic doesn't end with memories. Picture yourself exploring a new city without a tour guide. With our app, instantly learn about the place you've just visited by uploading a photo. TravelerEye acts as your digital guide, offering information about historical sites, local culture, and natural wonders, all powered by NVIDIA's TensorRT-llm for rapid insights. It's the perfect companion for both solo travelers seeking knowledge and groups looking for a deeper understanding of their adventures."

"TravelerEye isn't just an application; it's a revolution in how we interact with our photos and the world. It's about making every photo a conversation starter, enriching discussions with family and friends, and turning every snapshot into an opportunity for discovery and connection."

"Join us as we redefine photo exploration with TravelerEye, where memories meet discovery. Powered by NVIDIA, TravelerEye is your personal guide to the past and the present, making every journey an exploration of stories waiting to be told."

"Thank you for exploring with TravelerEye, a testament to how technology can bring us closer to our world and to each other. This is our submission to the Nvidia GenAIonRTX contest, showcasing the potential of AI to enhance our lives in meaningful ways."




