from transformers import pipeline
import speech_recognition as sr
from textblob import TextBlob
import openai 
openai.api_key = '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'

# Initialize recognizer

# recognizer = sr.Recognizer()
# audio_file_path = "audio.wav"

# # Load audio file
# with sr.AudioFile(audio_file_path) as source:
#     audio_data = recognizer.record(source)

# # Perform speech recognition
# text = recognizer.recognize_google(audio_data)
# print("Text from audio:", text)

text = "The environment is: You have a wall in front of you, an obstacle 2 steps to you're left "

messages = [ {"role": "system", "content":  
              """you are a Humonoid Nao Robot, I will explain the environment around you, you have to take actions, to navigate the environments, 
                your actions are: move_forward, rotate. move _right, move_left
                reply only with the actions
                and the number of steps for each action expect rotate"""} ] 
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