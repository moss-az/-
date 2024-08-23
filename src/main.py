import os

import openai_interaction
import voice_recognition
from voice_generator import synthesize_initial_voice





print("你好，有什么我可以帮到你的嘛？")

filename ='human.wav'
while True:
    voice_recognition.record_audio(filename)
    result = voice_recognition.recognise(filename)
    if '你好' in result or '开始' in result:
        response = openai_interaction.send_request_4(result)
        synthesize_initial_voice(response)
    elif '退出' in result:
        exit_voice = "退出语音"

        os.system(f"mpg321 退出.mp3")
        break