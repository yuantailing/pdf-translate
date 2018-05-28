# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


def main():
    with open('build/pdf.js/web/viewer.html', 'rb') as f:
        content = f.read()
    content = content.replace(br'<link rel="stylesheet" href="viewer.css">', br'<link rel="stylesheet" href="pdf.js/web/viewer.css">')
    content = content.replace(br'<link rel="resource" type="application/l10n" href="locale/locale.properties">', br'<link rel="resource" type="application/l10n" href="pdf.js/web/locale/locale.properties">')
    content = content.replace(br'<script src="../build/pdf.js"></script>', br'<script src="pdf.js/build/pdf.js"></script>')
    content = content.replace(br'<script src="viewer.js"></script>', br'<script src="pdf.js/web/viewer.js"></script>')
    with open('src/index-addon.html', 'rb') as f:
        addon = f.read()
    insertBeforeLine = br'</body>'
    content = content.replace(insertBeforeLine, addon + insertBeforeLine)
    with open('build/index.html', 'wb') as f:
        f.write(content)


if __name__ == '__main__':
    main()
