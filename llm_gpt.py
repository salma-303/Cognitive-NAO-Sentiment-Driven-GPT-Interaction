from transformers import pipeline
import speech_recognition as sr
from textblob import TextBlob
import openai 
openai.api_key = 'YOUR API KEY'

# Initialize recognizer

recognizer = sr.Recognizer()
audio_file_path = "audio.wav"

# Load audio file
with sr.AudioFile(audio_file_path) as source:
    audio_data = recognizer.record(source)

# Perform speech recognition
text = recognizer.recognize_google(audio_data)
print("Text from audio:", text)


def analyze_sentiment(text):

    # Perform sentiment analysis using TextBlob
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    print("Sentiment Score:", sentiment_score)

    # Classify sentiment
    if sentiment_score > 0:
        print("Sentiment: Positive")
    elif sentiment_score < 0:
        print("Sentiment: Negative")
    else:
        print("Sentiment: Neutral")


# Example usage
analyze_sentiment(text)

messages = [ {"role": "system", "content":  
              "You are a NAO robot, exist at colleage of Artificial Intelligence in Alamain city, developed by Ai students.Answer in 2 sentences."} ] 
while True: 
    message = (f"User :{text} ")
    if message: 
        messages.append( 
            {"role": "user", "content": message}, 
        ) 
        chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=messages 
        ) 
    reply = chat.choices[0].message.content 
    print(f"ChatGPT: {reply}") 
    messages.append({"role": "assistant", "content": reply}) 

    # Save the first reply to a text file
    if len(messages) == 3:
        with open('question_answering_result.txt', 'w') as file:
            file.write(reply)
        break