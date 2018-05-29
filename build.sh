#!/bin/bash
set -e -x

# copy needed files from pdf.js
mkdir -p build/pdf.js
if [[ $PRODUCTION = 1 ]]; then
  cp -r pdf.js/build/minified/* build/pdf.js/;
else
  cp -r pdf.js/build/generic/* build/pdf.js/;
fi

# copy assets
cp -r www/* build/

# download required JS
mkdir -p build/static/js
pushd . && cd build/static/js
if [[ $PRODUCTION = 1 ]]; then
  curl -sSL https://unpkg.com/jquery/dist/jquery.min.js -ojquery.min.js
  curl -sSL https://unpkg.com/jquery.md5/index.js -ojquery.md5.js
  curl -sSL https://unpkg.com/vue/dist/vue.min.js -ovue.min.js;
else
  curl -sSL https://unpkg.com/jquery/dist/jquery.js -ojquery.js
  curl -sSL https://unpkg.com/jquery.md5/index.js -ojquery.md5.js
  curl -sSL https://unpkg.com/vue/dist/vue.js -ovue.js;
fi
popd

# download welcome PDF
mkdir -p build/assets
curl -sSL https://arxiv.org/pdf/1805.08090.pdf -obuild/assets/welcome.pdf

# build webpages
python src/build.py
