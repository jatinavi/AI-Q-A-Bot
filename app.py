# app.py
# A simple Q&A bot using TinyLlama model and Streamlit
# Author: Jatin Kumar Balchandani

import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# -----------------------------
# Load the TinyLlama model
# -----------------------------
# This is a small and fast model for chat-based Q&A
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",       # Automatically uses GPU if available
    torch_dtype=torch.float16  # Use half precision to save memory
)

# -----------------------------
# Function to generate answer
# -----------------------------
def ask(question):
    """
    Takes a text question as input,
    generates an answer using TinyLlama,
    and returns it as a string.
    """
    # Tokenize the input and send to model device
    inputs = tokenizer(question, return_tensors="pt").to(model.device)
    
    # Generate answer using sampling
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,  # maximum length of answer
        do_sample=True,      # enable randomness
        top_k=50,            # consider top 50 tokens
        top_p=0.95           # nucleus sampling
    )
    
    # Decode token IDs to text
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("TinyLlama Q&A Bot")
st.write("Ask a question and get an AI response!")

# Input box for user question
question = st.text_input("Your Question:")

# Button to generate answer
if st.button("Ask"):
    if question:
        with st.spinner("Thinking..."):  # show spinner while model generates answer
            answer = ask(question)
        st.success(answer)  # display the answer
