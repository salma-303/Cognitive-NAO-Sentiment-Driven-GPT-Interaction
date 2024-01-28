import subprocess

def run_nao_code():
    # Replace 'nao_script.py' with the actual filename of your NAO code
    subprocess.run(['python2', 'record.py'])

# def run_speech_recognition_code():
#     subprocess.run(['python11', 'sentimental_analysis.py'])

def run_gpt_code():
    subprocess.run(['python11', 'llm_gpt.py'])

def run_nao_tts_code():
    # Replace 'nao_tts_code.py' with the actual filename of your NAO TTS code
    subprocess.run(['python2', 'response.py'])

def main():
    run_nao_code()
    # run_speech_recognition_code()
    run_gpt_code()
    run_nao_tts_code()

if __name__ == "__main__":
    main()
