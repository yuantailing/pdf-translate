#!/bin/bash
set -e -x

# copy needed files from pdf.js
mkdir -p build/pdf.js
cp -r pdf.js/build/generic/* build/pdf.js/

# copy assets
cp -r www/* build/

# download required JS
mkdir -p build/static/js
pushd . && cd build/static/js
curl -sS https://unpkg.com/jquery/dist/jquery.min.js -ojquery.min.js
curl -sS https://unpkg.com/vue/dist/vue.min.js -ovue.min.js
popd

# download welcome PDF
mkdir -p build/assets
curl -sS https://arxiv.org/pdf/1805.08090.pdf -obuild/assets/welcome.pdf

# build webpages
python src/build.py
