import requests
import datetime

# GitHub アクセストークンをセットします
ACCESS_TOKEN = ''
ACCESS_USER = ''

# HTTP ヘッダーにアクセストークンを含めるための辞書を定義します
headers = {
    'Authorization': f'token {ACCESS_TOKEN}'
}

# 草の情報を取得する日付を設定します
date = datetime.datetime.now().strftime('%Y-%m-%d')
print(date)

# GitHub API を使用して草の情報を取得します
url = f'https://api.github.com/users/{ACCESS_USER}/events?per_page=1000'
response = requests.get(url, headers=headers)
events = response.json()
commits = [event for event in events if event['type'] == 'PushEvent' and event['created_at'][:10] == date]

# 草を生やしていない場合に通知する処理を行います
if not commits:
    # 通知処理を実装してください
    print('草を生やしていません')
else:
    print('草を生やしました')
