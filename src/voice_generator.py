from aip import AipSpeech

# generate_initial_voice.py

from aip import AipSpeech
import os
from config import APP_ID, API_KEY, SECRET_KEY  # 从配置文件导入API密钥

# 初始化AipSpeech对象
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def synthesize_initial_voice(text, output_file='进入.mp3'):
    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,
        'spd': 5,
        'pit': 5,
        'per': 4
    })

    if not isinstance(result, dict):
        with open(output_file, 'wb') as f:
            f.write(result)
        print(f"语音合成成功，文件已保存为 {output_file}")
        # 自动播放音频
        os.system(f"mpg321 {output_file}")
    else:
        print("语音合成失败，错误信息：", result)

if __name__ == '__main__':
    text = ("你好，我是你的智障语音助手，请问有什么可以帮到你的吗？")
    synthesize_initial_voice(text)