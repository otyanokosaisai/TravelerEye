# TravelerEye: Visual Exploration Tool

Welcome to **TravelerEye**, a cutting-edge visual exploration tool that leverages the power of AI to enhance your photo experiences. Utilizing state-of-the-art models like **BLIP-2** and **Llama2**, TravelerEye provides intuitive genre selection and photo analysis capabilities.

![TravelerEye Interface](path_to_your_demo_image_here)

## TravelerEye Overview


## Installation

Before diving into the visual world of TravelerEye, you'll need to set up your environment. Follow these steps to get started:
- install NVIDIA Container
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

This project uses large model files not stored directly in this repository. Please download the necessary files and place them in the respective directories.

#### Model Files

- **BLIP-2 and Llama2 Models**: Download the model files to ensure the application runs smoothly.

  - [Download Model Files (ZIP)](https://drive.google.com/file/d/1UIgEps1LL7jehNJezSvaqGDhclOHqjG-/view?usp=sharing)
    - `[blip2/rank0.plan]` - Place it at `models/blip2/trt_engine/blip-2-opt-2.7b/fp16/1-gpu/rank0.engine`
    - `[blip2/Qformer_fp16.plan]` -Place it at `models/blip2/plan/Qformer/Qformer_fp16.plan`
    - `[blip2/visual_encoder_fp16.plan]` - Place it at `models/blip2/plan/visual_encoder/visual_encoder_fp16.plan`
    - `[Llama2/rank0.engine]` - Place it at `models/llama2/engine/rank0.engine`

  - [Download Model Files (pt)](https://drive.google.com/file/d/1hI6da39QVX70ZKxbm4EQKwRzBoJevOal/view?usp=sharing)
    - `[query_tokens.pt]` Place it at `models/blip2/query_tokens.pt`

### Usage
Run the application with the following command:

```bash

python3 app.py

```

Access TravelerEye by navigating to http://127.0.0.1:7860 in your web browser. Upload a photo and select a genre to begin the exploration.


## Contributing

We welcome contributions! If you have suggestions for improvements or new features, please [open an issue](link_to_your_issues_page) or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgments

- Thanks to Salesforce, Inc. for developing BLIP-2.
- Thanks to NVIDIA for providing TensorRT-llm.
- Thanks to Meta Platforms, Inc. for making Llama2 available to the community.



