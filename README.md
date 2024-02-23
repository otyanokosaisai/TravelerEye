# 🌍 TravelerEye: Visual Exploration Tool

Welcome to **TravelerEye** 📸, a cutting-edge visual exploration tool that leverages the power of AI 🤖 to enhance your photo experiences. Utilizing state-of-the-art models like **BLIP-2** and **Llama2**, TravelerEye provides intuitive genre selection and photo analysis capabilities.

![TravelerEye Interface](https://github.com/otyanokosaisai/TravelerEye/blob/master/TravelerEye_sample.png)
![TravelerEye Interface](https://github.com/otyanokosaisai/TravelerEye/blob/master/TravelerEye_sample2.png)
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

"Introducing TravelerEye, the AI companion powered by Nvidia's cutting-edge technology, transforming your travel photos into rich stories and knowledge.

Revisit cherished memories with family and friends as TravelerEye brings your past adventures to life. Each photo, enriched with cultural and historical insights, deepens the bonds and conversations shared around those memories.

On solo journeys or explorations without a guide, TravelerEye becomes your instant digital companion. Just upload a photo, and our app, leveraging BLIP-2 and Llama2 models accelerated by TensorRT-llm, reveals everything you need to know about the places you've visited. From historical sites to natural wonders, TravelerEye provides context, making every trip more meaningful.

TravelerEye is more than an app; it's a new way to experience your travels and share stories, where memories meet discovery, enhancing how we connect with our world and each other.

Now, let's quickly walk through how to bring this magic to life:

Follow the installation guide on our GitHub page to set up your Docker container.
Launch the app and upload a photo to start your journey.
Choose or type a genre for the photo to tailor the insights you receive.
Hit the 'Generate' button and watch as TravelerEye unveils the stories behind your image.
In just a few simple steps, TravelerEye transforms your travel photos into gateways of exploration and connection, making every photo an opportunity for discovery.

Thank you for exploring with TravelerEye, your passport to rediscovering the world through your lens."

## このプロジェクトについて
TravelerEyeは、写真が持つ潜在的な物語と知識を解き放ち、忘れ去られた情報やまだ見ぬ知識を再発見することを目指す革新的な取り組みです。スマートフォンの普及により、私たちは旅行先で目にする新鮮な光景や名所を写真に収める機会が増えました。しかし、時間が経つにつれ、その場で感じたことや学んだことを忘れてしまうことがよくあります。TravelerEyeは、撮影された写真に隠された文化的、歴史的背景から自然環境や民俗に至るまで、多様な情報を提供することで、写真に新たな命を吹き込みます。

このプロジェクトは、SalesforceのBLIP-2-OPT-2.7bによる高度な画像からの特徴抽出技術と、MetaのLLaMA-2-7b-chat-hfを活用したジャンル毎の情報提供システムによって支えられています。TensorRT-llmを用いた加速技術により、ユーザーが選択したジャンルに応じて、写真に映る被写体に関連する詳細な情報を迅速に提供します。提供されるジャンルは、文化芸術、歴史史跡、自然、科学技術、民俗生活など多岐にわたり、さらにユーザー自身でカスタマイズするオプションも用意されています。この柔軟性により、ユーザーは自分の興味に合った情報を容易に得ることができます。

さらに、TravelerEyeは現代社会におけるコミュニケーションの課題に対しても解決策を提供します。写真を通じて忘れていた情報や新たな発見を共有することで、人々はより深いレベルで体験を共有し、会話の質を高めることができます。ツアーガイドがいない旅行や一人旅においても、TravelerEyeは「sightseeing」などのジャンルを通じて、旅先についての豊富な情報を提供することで、知識豊かなガイドとなります。

今日のLLMとIT技術の進展により、希薄化しつつある人間関係を再び深める手段として、TravelerEyeは新たな可能性を開きます。このアプリケーションは、旅行から得られる体験の再定義と記憶の豊かな保存を可能にし、LLM技術を用いたコミュニケーションの促進に貢献します。TravelerEyeは、旅の記憶を永続させ、世界とのつながりを深めるための、画期的なツールです。

