# Q&A Bot Project – Development Journey
## In this file I will be recording every step, failure, or success I encountered to finish this project.
## Trying to Make the Bot Work Using Different Models
### 1. ChatGPT API: Initially tried using ChatGPT API but ran into RUNLIMIT after 2 inputs due to limited access.
### 2. HuggingFace Models: Switched to HuggingFace models for better accessibility.
### 3. Mistral Model: Tried Mistral model, but it required authentication.
### 4. Google/flan-t5-base: Attempted google/flan-t5-base (free, closer to ChatGPT), but it didn’t work.
### 5. Zephyr-7B-Beta: Attempted zephyr-7b-beta model, which fetched 8 files of ~2GB each (the neural network’s "brain").
### 6. TinyLlama/TinyLlama-1.1B-Chat-v1.0: Finally worked! Small, fast, ~2.5GB, optimized for Q&A.
## Example:
### Question: Who is Jatin?
### Answer: Bot: Who is Jatin? Answer according to: The name Jatin or Kunti is an Indian name for females, which is of Sanskrit origin. The name Jatin is pronounced similarly to Jyothi, Jinny, Jitni.
# Streamlit UI Implementation
### Initial Attempt: Tried normal Streamlit UI as in other projects, but didn’t work on Colab CPU.
### Ngrok Requirement: Needed Ngrok to create a public URL from Colab VM to browser. Without it, localhost:8501 is inaccessible.
### Successful UI: Implemented Streamlit interface for Q&A.
## Example:
### Question: What is AI?
### Answer: What is AI? How can I learn it? Robot: AI is an acronym that stands for Artificial Intelligence. AI refers to the ability of machines to think, learn, and act like humans do. In the field of computer science.
### Note: Current response limit is 100 characters in the interface.
