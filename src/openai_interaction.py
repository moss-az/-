import requests #
import json # jeson库
import logging #

# gpt-4o
def send_request_4(kw):
    # 替换为自己的KEY
    api_key = 'sk-PqpCIqfKggPl0ehF2c2dAbDb398e40498eFe158f9fC8D9B9'
    try:
        api_url = 'https://api.apiyi.com/v1/chat/completions'
        # 设置请求头部，包括 API 密钥
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        # 准备请求的数据
        payload = {
            'model': "gpt-4o",
            'messages': [{"role": "system", "content": kw}]
        }
        # 发送 POST 请求
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        # 检查响应状态
        if response.status_code == 200:
            # 解析响应并提取需要的信息
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return f'Error: Received status code {response.status_code}'
    except Exception as e:
        logging.info(e)
        return 'An error occurred while sending the request'

if __name__ == '__main__':
    kw = '你好'
    response = send_request_4(kw)
    print(response)