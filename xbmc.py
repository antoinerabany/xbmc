#! /usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import optparse

def main():

    p = optparse.OptionParser()

    p.add_option('--message', '-m', default="Bonjour")

    options, arguments = p.parse_args()

    url = "http://miku.larez.fr:8080/jsonrpc"
    headers = {'Content-Type': 'application/json'}

    xbmc = {
        "method": "GUI.ShowNotification",
        "params": {'title':'voctroll','message':options.message,'image':'Troll.png'},
        "jsonrpc": '2.0',
        "id": 0,
    }

    response = requests.post(
        url, data=json.dumps(xbmc), headers=headers, auth=('xbmc','xbmc')).json()

    #assert response["result"] == "echome!"
    assert response["jsonrpc"] == '2.0'
    assert response["id"] == 0

    print  (response)



if __name__ == "__main__":
    main()