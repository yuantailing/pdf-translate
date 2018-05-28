#!/bin/bash
set -e -x

# copy needed files from pdf.js
mkdir -p build/pdf.js
cp -r pdf.js/build/generic/* build/pdf.js/

# copy webpages
cp -r www/* build/

# download welcome PDF
mkdir -p build/assets
curl https://arxiv.org/pdf/1805.08090.pdf -obuild/assets/welcome.pdf
