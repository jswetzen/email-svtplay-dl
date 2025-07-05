#!/usr/bin/env python

import email
import re
import sys

msg = email.message_from_file(sys.stdin)

if msg.is_multipart():
    text = msg.get_payload()[0].get_payload(decode=True)
else:
    text = msg.get_payload(decode=True)
text = text.decode('UTF-8')
matches = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
for url in matches:
    if url.find('svtplay.se') or url.find('tv4play.se'):
        print(url)
        break
