#!/bin/sh

echo "Searching for original..."
../comphisto.py -d dataset/ -q query/original.JPG
echo "Searching for thumbnail..."
../comphisto.py -d dataset/ -q query/thumbnail.JPG
echo "Searching for sharpened thumbnail..."
../comphisto.py -d dataset/ -q query/thumbnail_sharpen.JPG
echo "Searching for small thumbnail..."
../comphisto.py -d dataset/ -q query/thumbnail_small.JPG
echo "Searching for b&w thumbnail..."
../comphisto.py -d dataset/ -q query/thumbnail_bw.JPG
echo "Searching for b&w thumbnail colorblind..."
../comphisto.py -d dataset/ -q query/thumbnail_bw.JPG --colorblind
