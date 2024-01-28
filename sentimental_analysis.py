import speech_recognition as sr
from textblob import TextBlob

def analyze_sentiment(audio_file_path):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    # Perform speech recognition
    try:
        text = recognizer.recognize_google(audio_data)
        print("Text from audio:", text)

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

    except sr.UnknownValueError:
        print("Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Example usage
audio_file_path = "audio.wav"
analyze_sentiment(audio_file_path)
