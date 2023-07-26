import requests

def request_labels():
    headers = {'Accept': 'application/json'}
    url = 'https://nptwpxthvb.eu-west-1.awsapprunner.com/labels'
    r = requests.get(url, headers=headers)
    return r.json()

def request_one_label(id_label):
    headers = {'Accept': 'application/json'}
    url = 'https://nptwpxthvb.eu-west-1.awsapprunner.com/labels/'+str(id_label)
    print(url)
    r = requests.get(url, headers=headers)
    return r.json()

