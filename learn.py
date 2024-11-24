import requests
import json

# URL endpoint
url = "https://chat100.erweima.ai/api/v1/chat/gpt4o/chat"

# Headers
headers = {
    "authorization": "",  # Cần thay bằng token thực tế
    "content-type": "application/json",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "uniqueid": "fa71d3714a76958526ada109236c6fd1",
    "verify": "0.pPurmeAN-KxZaxmdRKJrTlq07DsQ-C1g1QUwydrcvh56ZgsMjB5kE4hzKsvZa_pol3V0Sm-zs4S9biDsQm2ZNz5yv2TYQYCTo2ZMboyXHWf4BRz94pyshQQs2tgv0-OKjNMJPybK2LSgVzTw467YvFeHGwr_Kiad5guRIzaTByp_1aTw8p1bL8FM-g1TTTXbKTAgEbHfhEEbm4A0J5rPegokHbm2gsC6seOmYSUHCcTk7_0Bz7pewHCHaTBBqqF8r4p_2Lf5XzHrU0UrfWXDRakmO_1wY0YGyllasBdIBegirvML0oYx85Jjp26M6ajSOgexCVZEy3zdXeITJFx3FxkfcpYLqgY93wV32FBqHF4AN0cjqNNp-JKj9R8tN5Gh8qbEgZmO1AhyD7QI7xwQvWdOwi0jnDOoeL_iSQCWe7oMUMIR92rQrFBjVch9ut5I0_sgZixoDXPWfRYk3hjfHCF0a-vp-AzSedF2mXzru5yW8UHmxw09b9xNKYewFoxmMjDQuTy74EnnvX2aGQERtlPqTeqaQd3IHTohMTlISGnbFd1Et6EO0k1-904RA0EO-cHKHG3UdNs99JSO1zqmlkeKMxBHSB0VOUx6APgIuIPn3rN5Xiep_nquXb-PPpXAYiCn1O1sUUo_PE48tzg0vN0z-Oj5gfLFeBDnTIXrU66OdM19FTIbz3o0W-Tw5QZRxTE6tZVO3ktuXjMKC6tTS8OT4AR_Zypv6wUiLa5cS9c.AqnuX-u9nyJ8srkRZHQzYw.e17dff20c423cf9c448b7e34ae6a7f7ba2ab013c1437d288c0940d88a276d388"  # Cần thay bằng giá trị thực tế
}

# Payload (body) với thông tin vị trí
data = {
    "prompt": "bằng python, tôi muốn gửi requests và nhận. có được không",
    "sessionId": "10cf66aa376682a9db57490a070d9f5e",
    "attachments": [],
    "location": {
        "longitude": 126.6297,  # Kinh độ (thay giá trị theo vị trí của bạn)
        "latitude": 10.8231,    # Vĩ độ (thay giá trị theo vị trí của bạn)
        "timezone_id": "Asia/Ho_Chi_Minh",  # Múi giờ
        "locate": "Ho Chi Minh City, Vietnam"  # Vị trí cụ thể
    }
}

try:
    # Gửi yêu cầu POST
    response = requests.post(url, headers=headers, json=data)
    
    # Kiểm tra mã trạng thái
    if response.status_code == 200:
        print("Response JSON:")
        print(response.json())  # Phân tích phản hồi nếu là JSON hợp lệ
    else:
        print(f"Error: HTTP {response.status_code}")
        print("Response Text:", response.text)

except requests.RequestException as e:
    print("An error occurred:", e)
