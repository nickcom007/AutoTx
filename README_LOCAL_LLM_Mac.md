# Guide to Setting Up llama.cpp with a Finetuned Mistral_7B Model for Mac

This guide will help you configure llama.cpp to work seamlessly with a finetuned Mistral_7B model on a Mac system. Here's a step-by-step instruction for setting up and running the configuration.

## Step 1: Clone the llama.cpp Repository
Start by cloning the llama.cpp repository into your local environment:

```bash
git clone https://github.com/ggerganov/llama.cpp
```

## Step 2: Download the Finetuned Model
Download the finetuned Mistral_7B model appropriate for Mac from HuggingFace. Ensure you have `git lfs` installed to handle large files:

```bash
git lfs clone https://huggingface.co/flock-io/Mistral-7B-CrewAI
```
Note: Choose the model with a 'gguf' suffix. The Q4 precision model is recommended for lower memory usage, while the Q8 precision model and full parameter precision is recommended for higher accuracy.

## Step 3: Navigate to the llama.cpp Directory
Change your current working directory to the cloned llama.cpp directory:

```bash
cd llama.cpp
```

## Step 4: Build llama.cpp
Compile the llama.cpp source code using the make command:

```bash
make
```

## Step 5: Launch the Server
Run the server with the downloaded model using the following command:

```bash
./server -m ./Mistral_7B_CrewAI/ggml-model-f16-Q4_K_M.gguf -c 8196
```
This command sets up the model to run locally with openai API compatibility on the default port 8080. For changing the default port or other settings, you can add parameters like `--port` and refer to [llama.cpp server examples](https://github.com/ggerganov/llama.cpp/tree/master/examples/server).

## Step 6: Configure Connection Settings
Ensure that port 8080 is configured to allow inbound connections. Modify the `.env` file with these settings:

```env
OPENAI_API_BASE=http://localhost:8080/v1
OPENAI_BASE_URL=http://localhost:8080/v1
OPENAI_MODEL_NAME=AutoTx_Mistral_7B
OPENAI_API_KEY=EMPTY
```

You can specify a custom value for `OPENAI_API_KEY` if an API key mechanism is set up in the llama.cpp configuration.

## Congratulations
You have successfully configured and set up the AutoTx framework with the AutoTx_Mistral_7B_CrewAI model on your Mac using llama.cpp. This setup lets you leverage this powerful model for your applications and projects on Mac environments effectively!