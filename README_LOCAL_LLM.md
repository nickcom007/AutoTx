# Guide to Using AutoTx Framework with a Finetuned Mistral_7B Model based on vLLM

This guide provides step-by-step instructions on how to use the AutoTx framework with a finetuned Mistral_7B model based on the vLLM.

## Step 1: Setup a Conda Environment
Begin by setting up a dedicated conda environment for the project:
```bash
conda create -n vLLM_host
conda activate vLLM_host
```

## Step 2: Install vLLM
Install the vLLM package in the environment. We recommend using version 0.3.3 for compatibility:
```bash
pip install vllm==0.3.3
```

## Step 3: Download the Finetuned Model
Download the finetuned Mistral_7B model from HuggingFace. Make sure `git lfs` is installed on your machine to handle large files effectively:
```bash
git lfs clone https://huggingface.co/Superoisesuki/AutoTx_Mistral_7B_CrewAI
```

## Step 4: Launch the Server
Launch the server with the following command:
```bash
python -m vllm.entrypoints.openai.api_server --served-model-name AutoTx_Mistral_7B --model ./AutoTx_Mistral_7B_CrewAI/ --gpu-memory-utilization 0.95 --dtype bfloat16 --max-model-len 8192 --port 8002
```
Note: Default port is 8000. You can specify a different one if needed.

## Step 5: Server Output
Upon successful launch, you should see outputs like:
```
INFO:     Started server process [675184]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8002 (Press CTRL+C to quit)
```

## Step 6: Configure Connection Settings
If port 8002 is open for inbound protocols, modify the `.env` file with these settings:
```
OPENAI_API_BASE=http://your.ip:8002/v1
OPENAI_BASE_URL=http://your.ip:8002
OPENAI_API_KEY=EMPTY
```
You may specify a custom value for `OPENAI_API_KEY` if you included the `api-key` parameter in the vLLM start command.

## Step 7: Using Ngrok for Local Testing
If the port is not open, you can use ngrok:
```bash
ngrok http http://localhost:8002
```
Then replace `OPENAI_BASE_URL` and `OPENAI_API_BASE` with the URL provided by ngrok.

## Congratulations
You have successfully configured the AutoTx framework to work with the AutoTx_Mistral_7B_CrewAI model. Enjoy leveraging this powerful model in your projects!