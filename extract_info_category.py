from sys import stdin, stdout
from re import search

title = ''
category = ''

for line in stdin:
    line = line.strip()
    
    if line == '':
        continue
    if line[:6] == 'Title=':
        title = line[6:]
    elif line[:8] == 'Infobox=':
        infoline = line[10:]
        if infoline != '':
            if ' |' in infoline:
                category = infoline[:infoline.find(' |')]
            else:
                category = infoline
        category = category.strip()
        if category != '' and title != '':
            if not search('[}|\[\]<>&#=]', title+category) and not search('[tT]iedosto',title):
                print ("%s\t%s" % (title, category))
            stdout.flush()
        title = ''
        category = ''
