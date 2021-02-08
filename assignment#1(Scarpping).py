import fileinput
import re
import html
from urllib.request import urlopen
url ="http://www.pakbj.org/index.php?m=content&c=index&a=show&catid=29&id=6"
page = urlopen(url)
html1 = page.read().decode("utf-8")
headings = re.findall(r'(\b[A-Z][a-z][\s\d:+\w,.`(&#8;)-]+)',str(html1))
com=[ x for x in headings if "Arial" not in x ]
com=html.unescape(com)
unwanted_string = {'Feb.', 'Jan.','border-right:','Ambassador Meets Mr.','Arial, Helvetica, sans-serif; border-right','Qfast.','Pakistan-Vision-2025.','Code 100600.','Sina_Weibo_Logo_RGB_Cn.','Ambassador Masood Khalid New1.','Nation Quaid-e-Azam Muhammad Ali Jinnah&amp; 39;s achievement as the found   '}
com = [ele for ele in com if ele not in unwanted_string]
with open('final.txt', 'w') as filehandle:
    for listitem in com:
        filehandle.write('%s\n' % html.unescape(listitem))