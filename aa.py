import requests, random, time
wallet = input("Wallet address: ")
email = input("Input email: ")
user_id = input("Input user id: ")
video = input("Input link video <https://fanzy.page.link/8xf5LbFwaxxmPKAK8>: ")
def run():
    num = 1
    idv = requests.get(video).json()
    vid_id = idv["result"]["result"][0]["org_video_id"]
    max_duration = int(idv["result"]["result"][0]["duration"]) - 200
    playing = 10
    loop = True
    while(True):
        try:
            headersx = {
                'user-agent': 'Dart/2.7 (dart:io)',
                'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
                'accept-encoding': 'gzip',
                'content-length': '149',
                'host': 'app.fanzy.io',
            }
            datax = {
                'user_id': user_id,
                'wallet_address': wallet,
                'email': email,
                'org_video_id': vid_id,
            }
            responses = requests.post('https://app.fanzy.io/video_view/request', headers=headersx, data=datax)
            if responses.status_code == 403:
                print("Bypassing forbidden access!!")
                time.sleep(30)
            else:
                responsex = responses.json()
            headers = {
                'user-agent': 'Dart/2.7 (dart:io)',
                'coding': 'gzip',
                'content-length': '188',
                'host': 'app.fanzy.io',
            }
            data = {
                'user_id': user_id,
                'hash': wallet,
                'email': email,
                'org_video_id': vid_id,
                'duration': str(playing),
                'started_at': responsex["result"]["result"]["updated_at"]
            }
            response = requests.post('https://app.fanzy.io/video_reward/request', headers=headers, data=data).json()
            if response["code"] == 200:
                print(str(num)+".) "+"Success getting reward!!!")
            elif response["code"] == 400:
                print("Failed viewing!")
            else:
                playing -= 50
                print(response)
            num += 1
            if loop == True:
                playing += 10
            else:
                playing = max_duration
                loop = False
        except Exception as E:
            print("Got error contact: corrykalam[at]zicor.media")
            print(E)
            pass
run()
