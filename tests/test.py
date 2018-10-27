import requests
import argparse
import json
from time import sleep

payload1 = json.dumps({"first": "blabla"}, sort_keys=True)
payload2 = json.dumps({"sec": "blabla!!"}, sort_keys=True)

def get(url):
    res = requests.get(url)
    
    if res.status_code != 200:
        raise Exception('GET fail. status code: {}'.format(res.status_code))
    
    res = json.dumps(res.json(), sort_keys=True)
    print 'GET({}) -> {}'.format(url, res)
    return res

def post(url, payload):
    print 'POST({},{})'.format(url, payload)
    res = requests.post(url, data=payload)
    
    if res.status_code == 204:
        return
    elif res.status_code == 502:
        raise Exception('fail fw palyload. status code: {}'.format(res.status_code))
    else:
        raise Exception('POST fail. status code: {}'.format(res.status_code))

def main():    
    parser = argparse.ArgumentParser()
    parser.add_argument("--url1")
    parser.add_argument("--url2")
    
    args = parser.parse_args()
    url1 = args.url1
    url2 = args.url2
    
    #post url1 and get from url2
    print '{} test 1 {}'.format('~'*20,'~'*20)
    post(url1, payload1)
    res2 = get(url2)
    if payload1 != res2:
        raise Exception("mismatch!!!")
    print '{} test 1 completed succesfully {}'.format('~'*20,'~'*20)
    sleep(1)
    
    #post url2 and get from url1
    print '{} test 2 {}'.format('~'*20,'~'*20)
    post(url2, payload2)
    res1 = get(url1)
    if payload2 != res1:
        raise Exception("mismatch!!!")
    print '{} test 2 completed succesfully {}'.format('~'*20,'~'*20)
    sleep(1)
    
    #get and compare both remotes
    print '{} test 3 {}'.format('~'*20,'~'*20)
    res1 = get(url1)
    res2 = get(url2)
    if res1 != res2:
        raise Exception("mismatch!!!")
    print '{} test 3 completed succesfully {}'.format('~'*20,'~'*20)
    

if __name__ == '__main__':
    main()