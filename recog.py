#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""画像認識のためのサンプル"""
import sys
import json
import argparse

import requests
from pit import Pit


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('img')
    args = parser.parse_args(argv)

    setting = Pit.get(
        'iwdcat',
        {'require': {'username': '',
                     'password': '',
                     }})
    auth_token = setting['username'], setting['password']
    url = 'https://gateway.watsonplatform.net/visual-recognition-beta/api/v1/tag/recognize'

    res = requests.post(url, auth=auth_token, files={
            'imgFile': ('sample.jpg', open(args.img, 'rb')),
        })
    if res.status_code == requests.codes.ok:
        data = json.loads(res.text)
        for img in data['images']:
            print('{} - {}'.format(img['image_id'], img['image_name']))
            for label in img['labels']:
                print('    {:30}: {}'.format(label['label_name'], label['label_score']))
    else:
        print(res.status_code)
        print(res.reason)

if __name__ == '__main__':
    sys.exit(main())
