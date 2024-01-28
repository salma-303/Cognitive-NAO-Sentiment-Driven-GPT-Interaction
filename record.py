import time
import os
import paramiko
from naoqi import ALProxy

# Set the IP address and port of your NAO robot
nao_ip = "10.1.95.223"
nao_port = 9559

# life_proxy = ALProxy("ALAutonomousLife", nao_ip, 9559)

# Disable autonomous life
# life_proxy.setState("disabled")

# Create an ALAudioRecorder proxy
audio_recorder = ALProxy("ALAudioRecorder", nao_ip, nao_port)

# Set the file path and name for the recording
# file_path = "D:\Desktop\recordings\recording.wav"
file_path = "/home/nao/audio.wav"

# Set the recording duration in seconds
record_duration = 5

# Start recordingfrom naoqi import ALProxy

audio_recorder.startMicrophonesRecording(file_path, "wav", 16000, [0, 0, 1, 0])
print("Recording...")

# Wait for the specified duration
time.sleep(record_duration)

# Stop recording
audio_recorder.stopMicrophonesRecording()
print("Recording stopped.")




# Release the proxy
audio_recorder.post.stopMicrophonesRecording()
def send_to_pc():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(nao_ip, username="nao", password="nao")
    sftp = ssh.open_sftp()
    remote_path= "/home/nao/audio.wav"
    #local_path = r'D:\Hossam\Pepper-master - Copy\audio.wav'
    local_path = r'./audio.wav'
    sftp.get(remote_path,local_path)
    #subprocess.Popen(["scp nao@pepper.local:/home/nao/audio.wav D:\Hossam"])
    #subprocess.Popen(["scp", "nao@pepper.local:/home/nao/audio.wav", rD:\Hossam"])
    sftp.close()
    ssh.close()
send_to_pc()