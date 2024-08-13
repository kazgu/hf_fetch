# hf_fetch

```
git clone https://github.com/kazgu/hf_fetch.git
cd hf_fetch
pip install .
```

```
hf-fetch -h
```
usage: hf-fetch [-h] [-repo REPO] [-base BASE] [-o O]

huggingface model downoader

options:
  -h, --help  show this help message and exit
  -repo REPO  huggingface model,like xxx/yyyy
  -base BASE  proxy
  -o O        output path


## usage

```
hf-fetch -repo openai-community/gpt2
```

the model will be downloaded in ~/.cache/huggingface/hub ,named models--openai-community--gpt2
