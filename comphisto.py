#!/usr/local/bin/python

import cv2
import argparse
import glob

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-d', '--dataset', required = True, help = 'Path to the directory of images')
ap.add_argument('-q', '--query', required = True, help = 'Query image to match against')
ap.add_argument('-t', '--threshold', required = False, help = 'Matching threshold (0-1)')
ap.add_argument('-l', '--limit', required = False, help = 'Limit the number of results')
ap.add_argument('--colorblind', action = 'store_true', help = 'Ignore color (greyscale compare)')
args = vars(ap.parse_args())

def getHistogram(filename):
    image = None
    if args['colorblind']:
        image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    else:
        image = cv2.imread(filename, cv2.IMREAD_COLOR)

    # valid image?
    if image is None:
        return None
    else:
        # extract a 3D RGB color histogram from the image, using 8 bins per channel,
        # normalize, and update the index
        hist = cv2.calcHist(image, [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist,hist,0,255,cv2.NORM_MINMAX).flatten()
        return hist

# query image histogram to compare against
query_hist = getHistogram(args['query'])

results = []

for imagePath in glob.glob(args['dataset'] + '/*.*'):
    hist = getHistogram(imagePath)
    if hist is not None:
        comp = cv2.compareHist(query_hist, hist, cv2.HISTCMP_CORREL)
        if args['threshold'] is None or comp >= float(args['threshold']):
            results.append([comp, imagePath])

results = sorted(results, key=lambda r: r[0], reverse=True)
if args['limit']:
    results = results[0:int(args['limit'])]
for result in results:
    print str(int(result[0] * 100)) + '%', result[1]
#print results[0:10]
