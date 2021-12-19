#!/usr/bin/env python

import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('album', metavar='A', type=str, nargs=1)
parser.add_argument('track', metavar='T', type=int, nargs=1)
parser.add_argument('rating', metavar='R', type=int, nargs=1,
                    choices=range(1, 6))

args = parser.parse_args()
filename = 'albums/' + args.album[0] + '.md'

ratings = {}
try:
  with open(filename, 'r') as f:
    line = 1
    for l in f.readlines():
      data = l.split('.')
      for i, d in enumerate(data):
        data[i] = d.strip()

      if (len(data) > 2 or not data[0].isdigit() or
          not data[1].isdigit() and data[1] != ''):
        print('Error: ' + str(data))
        sys.exit()

      if data[1] == '':
        ratings[line] = 0
      elif int(data[1]) >= 0 and int(data[1]) <= 5:
        ratings[int(data[0])] = int(data[1])
      else:
        print('Error: Invalid rating in file')
        sys.exit()

      line += 1
except:
  # We don't care if file doesn't exist since we're creating it later anyway
  pass

ratings[args.track[0]] = args.rating[0]
for i in range(1, max(ratings.keys())):
  if not i in ratings.keys():
    ratings[i] = 0

with open(filename, 'w+') as f:
  for k, v in sorted(ratings.items()):
    f.write(str(k) + '. ' + str(v) + '\n')
