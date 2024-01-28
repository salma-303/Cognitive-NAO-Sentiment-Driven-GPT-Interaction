# NAO Robot Cognitive Interaction Project

Welcome to the NAO Robot Cognitive Interaction project! This repository contains code to program a NAO robot for a unique cognitive experience. The project involves recording audio, performing sentiment analysis, engaging in GPT-enhanced conversations, and responding vocally.

## Files

### 1. `llm_gpt.py`
   - Speech-to-text conversion using Google's Speech Recognition API
   - Sentiment analysis using TextBlob
   - Integration with OpenAI's GPT-3.5 Turbo for dynamic conversational responses

### 2. `record.py`
   - Records audio using the NAO robot's ALAudioRecorder
   - Saves the recorded audio as 'audio.wav'

### 3. `sentimental_analysis.py`
   - Analyzes sentiment from an audio file using Google's Speech Recognition and TextBlob

### 4. `response.py`
   - Reads the GPT-generated response from 'question_answering_result.txt'
   - Converts the text to speech using the NAO robot's ALTextToSpeech

### 5. `main.py`
   - Orchestrates the execution of the entire project
   - Calls functions to run NAO code, sentiment analysis, GPT code, and NAO text-to-speech code

## Usage

1. **Recording Audio:**
   - Run `record.py` to capture audio and save it as 'audio.wav'.

2. **Sentiment Analysis:**
   - Execute `sentimental_analysis.py` to analyze sentiment from the recorded audio.

3. **Conversational AI:**
   - Run `llm_gpt.py` to initiate a conversation with GPT-3.5 Turbo.

4. **Text-to-Speech Response:**
   - Utilize `response.py` to convert GPT's response to speech and let the NAO robot vocalize it.

5. **Complete Workflow:**
   - Execute `main.py` to run the entire workflow seamlessly.

## Dependencies
- Ensure you have the required Python libraries installed:
  ```
  pip install transformers speech_recognition textblob openai
  ```

## Note
- Make sure to set up your NAO robot's IP address and port in the respective files for proper communication.

Feel free to explore, experiment, and contribute to this exciting cognitive robotics project!
