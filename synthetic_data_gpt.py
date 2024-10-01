
import sys
import pandas as pd
import numpy as np


import requests
import json

import openai
openai.api_key = ""#insert API key

dataset = pd.read_csv("ADA-USD.csv")#data

def generate_prompt(dataset):
    prompt = f"""
    Your task is to generate a dataset that is similar to the uploaded file.

    The data that you will use looks like the following:

    ```
    {dataset}
    ```
    """
    return(prompt)

def gather_chatgpt_outputs(prompt):
  messages = [{"role":"user", "content":prompt}]
  response = openai.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages,
      temperature = 0,
  )
  return response.choices[0].message["content"]

def main():
  prompt = generate_prompt(dataset)
  output = gather_chatgpt_outputs(prompt)
  output.to_csv('new_data.csv')
  return output

if __name__ == "__main__":
  main()