This project uses large model files that are not stored directly in this repository. Please download the following files and place them in the respective directories:

installation

After installing the NVIDIA Container, run the following commands follow to install TensorRT-llm

```bash

docker run --gpus all --entrypoint /bin/bash -it nvidia/cuda:12.1.0-devel-ubuntu22.04
apt-get update && apt-get -y install python3.10 python3-pip openmpi-bin libopenmpi-dev git
pip3 install tensorrt_llm -U --pre --extra-index-url https://pypi.nvidia.com
cd workspace
git clone --recursive https://github.com/otyanokosaisai/TravelerEye.git
cd travel_photo_app
pip3 install gradio
```

link : `https://drive.google.com/file/d/1UIgEps1LL7jehNJezSvaqGDhclOHqjG-/view?usp=sharing`
- [blip2/rank0.plan] - Place it under `models/blip2/trt_engine/blip-2-opt-2.7b/fp16/1-gpu/`
- [blip2/Qformer_fp16.plan] -Place it under `models/blip2/plan/Qformer/`
- [blip2/visual_encoder_fp16.plan] - Place it under `models/blip2/plan/visual_encoder/`
- [Llama2/rank0.engine] - Place it under `models/llama2/engine/`

After downloading, your project directory should look like this:
.
|-- README.md
|-- app.py
|-- flagged
|-- models
|   |-- blip2
|   |   |-- __pycache__
|   |   |   `-- trt_infer.cpython-310.pyc
|   |   |-- plan
|   |   |   |-- Qformer
|   |   |   |   `-- Qformer_fp16.plan
|   |   |   `-- visual_encoder
|   |   |       `-- visual_encoder_fp16.plan
|   |   |-- query_tokens.pt
|   |   |-- trt_engine
|   |   |   `-- blip-2-opt-2.7b
|   |   |       `-- fp16
|   |   |           `-- 1-gpu
|   |   |               |-- config.json
|   |   |               `-- rank0.engine
|   |   `-- trt_infer.py
|   `-- llama2
|       |-- Llama-2-7b-chat-hf
|       |   |-- tokenizer.json
|       |   |-- tokenizer.model
|       |   `-- tokenizer_config.json
|       |-- __pycache__
|       |   |-- trt_info_gen.cpython-310.pyc
|       |   `-- utils.cpython-310.pyc
|       |-- engine
|       |   |-- config.json
|       |   `-- rank0.engine
|       |-- trt_info_gen.py
|       `-- utils.py
`-- requirements.txt



usage:
```bash

python3 app.py

```
access `http://127.0.0.1:7860` and upload photo and select genre



appendix:package dependency
Package                   Version
------------------------- -------------------
accelerate                0.25.0
aiofiles                  23.2.1
aiohttp                   3.9.4rc0
aiosignal                 1.3.1
altair                    5.2.0
annotated-types           0.6.0
anyio                     4.3.0
async-timeout             4.0.3
attrs                     23.2.0
build                     1.0.3
certifi                   2024.2.2
charset-normalizer        3.3.2
click                     8.1.7
colorama                  0.4.6
colored                   2.2.4
coloredlogs               15.0.1
contourpy                 1.2.0
cuda-python               12.3.0
cycler                    0.12.1
datasets                  2.17.1
diffusers                 0.15.0
dill                      0.3.8
evaluate                  0.4.1
exceptiongroup            1.2.0
fastapi                   0.109.2
ffmpy                     0.3.2
filelock                  3.13.1
flatbuffers               23.5.26
fonttools                 4.49.0
frozenlist                1.4.1
fsspec                    2023.10.0
gradio                    4.19.1
gradio_client             0.10.0
h11                       0.14.0
httpcore                  1.0.4
httpx                     0.27.0
huggingface-hub           0.20.3
humanfriendly             10.0
idna                      3.6
importlib-metadata        7.0.1
importlib-resources       6.1.1
janus                     1.0.0
Jinja2                    3.1.3
jsonschema                4.21.1
jsonschema-specifications 2023.12.1
kiwisolver                1.4.5
lark                      1.1.9
markdown-it-py            3.0.0
MarkupSafe                2.1.5
matplotlib                3.8.3
mdurl                     0.1.2
mpi4py                    3.1.5
mpmath                    1.3.0
multidict                 6.0.5
multiprocess              0.70.16
networkx                  3.2.1
ninja                     1.11.1.1
numpy                     1.26.4
nvidia-ammo               0.7.3
nvidia-cublas-cu12        12.1.3.1
nvidia-cuda-cupti-cu12    12.1.105
nvidia-cuda-nvrtc-cu12    12.1.105
nvidia-cuda-runtime-cu12  12.1.105
nvidia-cudnn-cu12         8.9.2.26
nvidia-cufft-cu12         11.0.2.54
nvidia-curand-cu12        10.3.2.106
nvidia-cusolver-cu12      11.4.5.107
nvidia-cusparse-cu12      12.1.0.106
nvidia-nccl-cu12          2.18.1
nvidia-nvjitlink-cu12     12.3.101
nvidia-nvtx-cu12          12.1.105
onnx                      1.15.0
onnx-graphsurgeon         0.3.25
onnxruntime               1.16.3
optimum                   1.17.1
orjson                    3.9.14
packaging                 23.2
pandas                    2.2.0
pillow                    10.2.0
pip                       22.0.2
polygraphy                0.49.0
protobuf                  5.26.0rc2
psutil                    5.9.8
pyarrow                   15.0.0
pyarrow-hotfix            0.6
pydantic                  2.6.1
pydantic_core             2.16.2
pydub                     0.25.1
Pygments                  2.17.2
pynvml                    11.5.0
pyparsing                 3.1.1
pyproject_hooks           1.0.0
python-dateutil           2.8.2
python-multipart          0.0.9
pytz                      2024.1
PyYAML                    6.0.1
referencing               0.33.0
regex                     2023.12.25
requests                  2.31.0
responses                 0.18.0
rich                      13.7.0
rpds-py                   0.18.0
ruff                      0.2.2
safetensors               0.4.2
scipy                     1.12.0
semantic-version          2.10.0
sentencepiece             0.2.0
setuptools                59.6.0
shellingham               1.5.4
six                       1.16.0
sniffio                   1.3.0
starlette                 0.36.3
sympy                     1.12
tensorrt                  9.2.0.post12.dev5
tensorrt-bindings         9.2.0.post12.dev5
tensorrt-libs             9.2.0.post12.dev5
tensorrt-llm              0.9.0.dev2024022000
tokenizers                0.15.2
tomli                     2.0.1
tomlkit                   0.12.0
toolz                     0.12.1
torch                     2.1.2
torchprofile              0.0.4
torchvision               0.16.2
tqdm                      4.66.2
transformers              4.36.1
triton                    2.1.0
typer                     0.9.0
typing_extensions         4.10.0rc1
tzdata                    2024.1
urllib3                   2.2.1
uvicorn                   0.27.1
websockets                11.0.3
wheel                     0.37.1
xxhash                    3.4.1
yarl                      1.9.4
zipp                      3.17.0