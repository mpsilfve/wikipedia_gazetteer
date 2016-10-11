from sys import stdin, stdout
from re import search

def get_title(line):
    if line[:7] == '<title>':
        return line[7:][:-8]
    return None

def get_page_end(line):
    if line == '</page>':
        return line
    return None

def get_infobox_line(line, in_infobox, saw_infobox):
    if saw_infobox:
        return None, 0
    if line[:2] == '{{' and not search('[}|\[\]<>&#=]',line):
        return (line, 1)
    elif in_infobox:
        if line == '}}':
            return (line, 0)
        else:
            return (line, 1)
    return None, 0

title = ''
saw_infobox = 0
in_infobox = 0
infobox = []

for line in stdin:
    line = line.strip()

    
    if get_page_end(line) != None:
        print ("Title=%s" % title)
        print ("Infobox=%s" % ' '.join(infobox))
        title = ''
        saw_infobox = 0
        in_infobox = 0
        infobox = []
        stdout.flush()
        continue

    title_str = get_title(line)
    infobox_line, new_in_infobox = get_infobox_line(line, in_infobox, saw_infobox)
    
    if title_str != None:
        title = title_str
        continue
    
    if infobox_line != None:
        infobox.append(infobox_line)

    if in_infobox and not new_in_infobox:
        saw_infobox = 1

    in_infobox = new_in_infobox


