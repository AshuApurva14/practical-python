#!/usr/bin/python

import os
import json

if os.path.exists('/workspaces/practical-python/daily_challenge/Day_6/bucket.json'):

    print('File exist')


with open('/workspaces/practical-python/daily_challenge/Day_6/bucket.json', 'r') as reader:

  data = json.load(reader)

  print(json.dumps(data, indent=2))

  print(reader.read())

  print(reader.readline())
