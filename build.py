# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

from six.moves import urllib


def main():
    downloads = os.path.join('www', 'static', 'downloads')
    if not os.path.isdir(downloads):
        os.makedirs(downloads)
    urllib.request.urlretrieve(
        'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.0.489/pdf.js',
        os.path.join(downloads, 'pdf.js')
    )
    urllib.request.urlretrieve(
        'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.0.489/pdf.worker.js',
        os.path.join(downloads, 'pdf.worker.js')
    )
    urllib.request.urlretrieve(
        'https://arxiv.org/pdf/1805.08090.pdf',
        os.path.join(downloads, 'sample.pdf')
    )


if __name__ == '__main__':
    main()
