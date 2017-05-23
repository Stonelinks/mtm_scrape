import os
import shutil
import time
import csv
from subprocess import check_output
from pyquery import PyQuery as pq

post_start = 1
post_end = 674

with open("output.txt", "wb") as f:
    for post in range(post_start, post_end + 1):
        post = str(post)
        print 'downloading post ' + post
        html = check_output(["./download_post.sh", post])
        title = pq(html)('h1').text().encode('utf-8')

        content = pq(html)('div[style="float:left;font-size:16px;font-family:\'Alegreya Sans\', sans-serif;color:#000000;"]').text().encode('utf-8')

        f.write(title)
        f.write('\n')
        f.write(content)
        f.write('\n')
        f.write('\n')