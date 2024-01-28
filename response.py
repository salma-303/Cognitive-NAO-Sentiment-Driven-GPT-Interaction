# Specify the file path
file_path = 'question_answering_result.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the content of the file into a string
    file_content = file.read()

# Now, file_content contains the content of the file as a string
print(file_content)

import argparse
from naoqi import ALProxy

robot_ip = '10.1.95.223'
robot_port = '9559'
text_to_say = file_content

def main(robot_ip, robot_port, text_to_say):
  
    # Create ALTextToSpeech proxy
    tts = ALProxy("ALTextToSpeech", robot_ip, robot_port)
    tts.setLanguage("English")

    # Say the provided text
    tts.say(text_to_say)



# main(robot_ip, robot_port, text_to_say)    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="10.1.95.223",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    

    args = parser.parse_args()

   
    # Call the main function with the content of the text file
    main(args.ip, args.port, file_content)
