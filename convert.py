#!/usr/bin/env python3

import sys
import magic

if len(sys.argv) == 1:
    print('provide input file')
    sys.exit()

with magic.Magic(flags=magic.MAGIC_MIME_ENCODING) as m:
  file_encoding=m.id_filename(sys.argv[1])
  f = open(sys.argv[1],"r", encoding=file_encoding)
  f_content = f.read()
  f.close()
  o = open("%s_output" % sys.argv[1],"w", encoding="utf-8")
  o.write(f_content)
  o.close()
