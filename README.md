This project uses large model files that are not stored directly in this repository. Please download the following files and place them in the respective directories:

installation

After installing the NVIDIA Container, run the following commands follow to install TensorRT-llm

```bash

docker run --gpus all --entrypoint /bin/bash -it nvidia/cuda:12.1.0-devel-ubuntu22.04

```

```bash

apt-get update && apt-get -y install python3.10 python3-pip openmpi-bin libopenmpi-dev git
pip3 install tensorrt_llm -U --pre --extra-index-url https://pypi.nvidia.com
cd workspace
git clone --recursive https://github.com/otyanokosaisai/TravelerEye.git
cd travel_photo_app
pip3 install gradio

```

link : [Download Model Files (ZIP)](https://drive.google.com/file/d/1UIgEps1LL7jehNJezSvaqGDhclOHqjG-/view?usp=sharing)
- [blip2/rank0.plan] - Place it at `models/blip2/trt_engine/blip-2-opt-2.7b/fp16/1-gpu/rank0.engine`
- [blip2/Qformer_fp16.plan] -Place it at `models/blip2/plan/Qformer/Qformer_fp16.plan`
- [blip2/visual_encoder_fp16.plan] - Place it at `models/blip2/plan/visual_encoder/visual_encoder_fp16.plan`
- [Llama2/rank0.engine] - Place it at `models/llama2/engine/rank0.engine`



usage:
```bash

python3 app.py

```
access `http://127.0.0.1:7860` and upload photo and select genre
