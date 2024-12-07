# CFD_LLM_Accelerate24

## Introduction

A collaborative hackathon to prototype a small LLM to analyze data on a jet engine.

## Usage

Open up github codespaces

Type the following commands in the terminal

```R
pip install -r requirements.txt
```

```R
mkdir mkdir -p /home/codespace/.local/lib/python3.12/site-packages/google/colab
```

Add a new file in the root directory called `.gitignore`. 

Add the following to the .gitignore file:

.env

and save it.

You should then create a new file called .env and add your OpenAI API key to it.

```R
OPENAI_API_KEY=<YOUR_API_KEY>
```

Run the following scripts

`main_exercise.py`: Has a simple call to the OpenAI API

```R
python main_exercise.py
```

`opensource_llm.py`: Has a simple call to an open-source LLM (no need for an API key and no need for any money)

```R
python opensource_llm.py
```


## Resources

https://docs.science.ai.cam.ac.uk/hands-on-llms/setting-up/codespaces/

