from flask import Flask, jsonify, request
import  re, requests
app=Flask(__name__)

@app.route('/')
def home():
  return "Home"



@app.route('/usn', methods=["POST"])
def usn():
  if request.method=='POST':
    body_data=request.get_json()
    usn=body_data['data_usn']
    session=requests.Session()
    res=session.get("https://www.vtu4u.com/results/4AI17IS033?cbse=1")
    cod=res.text
    prev,keyword,next=cod.partition("csrf-token")
    prev,keyword,next=next.partition('content="')
    csrf_cod=(next.split()[0])
    csrf_token=str(csrf_cod.replace('">', ""))
    print(csrf_token)
    l_r=session.cookies.get_dict()['laravel_session']
    laravel_session=str('laravel_session='+l_r)
    print(laravel_session)
    text_inp=[csrf_token,laravel_session]
    csrf_token=text_inp[0]
    laravel_session=text_inp[1]
    headers = {
        'authority': 'www.vtu4u.com',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'accept': 'application/json, text/plain, */*',
        'x-csrf-token': csrf_token,
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.vtu4u.com/results/4AI17IS032?cbse=1',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': laravel_session,
    }
    params = (
        ('is_cbse', '1'),
    )
    print("y")
    print("y1")
    response = requests.get('https://www.vtu4u.com/results/'+usn+'/get', headers=headers, params=params)
    print(response.text)
    return jsonify(str(response.json()))
  elif  request.method=='GET':
    return "Its a get methos"

app.run(port=5000)