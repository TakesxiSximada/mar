#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import argparse

import requests
from pit import Pit


from celery import Celery, shared_task
BROKER_URL = 'redis://localhost:6379/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}

app = Celery('tasks', broker=BROKER_URL)


@shared_task
def recog_image(image_uri):
    setting = Pit.get(
        'iwdcat',
        {'require': {'username': '',
                     'password': '',
                     }})
    auth_token = setting['username'], setting['password']
    url = 'https://gateway.watsonplatform.net/visual-recognition-beta/api/v1/tag/recognize'

    res = requests.post(url, auth=auth_token, files={
            'imgFile': ('sample.jpg', open(image_uri, 'rb')),
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
