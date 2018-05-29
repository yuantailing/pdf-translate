# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

from six.moves import urllib


def main():
    with open('build/pdf.js/web/viewer.html', 'rb') as f:
        content = f.read()
    for url_old in ('viewer.css', 'locale/locale.properties', '../build/pdf.js', 'viewer.js', 'pdf.viewer.js'):
        url_new = urllib.parse.urljoin('pdf.js/web/', url_old)
        bin_old = '"{:s}"'.format(url_old).encode()
        bin_new = '"{:s}"'.format(url_new).encode()
        assert content.count(bin_old) <= 1
        content = content.replace(bin_old, bin_new)

    with open('src/index-addon.html', 'rb') as f:
        addon = f.read()
    if os.environ.get('PRODUCTION') == '1':
        for url_old, url_new in (
            ('static/js/jquery.js', 'static/js/jquery.min.js'),
            ('static/js/vue.js', 'static/js/vue.min.js'),
        ):
            bin_old = '"{:s}"'.format(url_old).encode()
            bin_new = '"{:s}"'.format(url_new).encode()
            assert addon.count(bin_old) <= 1
            addon = addon.replace(bin_old, bin_new)

    insertBeforeLine = br'</body>'
    content = content.replace(insertBeforeLine, addon + insertBeforeLine)
    with open('build/index.html', 'wb') as f:
        f.write(content)


if __name__ == '__main__':
    main()
