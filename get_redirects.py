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

def get_redirect(line):
    if line.find('<comment>') != -1:
        return None
    ind = line.find('#REDIRECT [[')
    if ind == -1:
        return None
    redirect = line[ind + len('#REDIRECT [['):]
    ind = redirect.find(']]')

    if ind == None:
        return -1

    redirect = redirect[:ind]

    return redirect

if __name__=='__main__':
    title = ''
    redirect = ''

    for line in stdin:
        line = line.strip()

        if get_page_end(line) != None:
            if title != '' and redirect != '':
                print ("%s\t%s" % (title, redirect))
            title = ''
            redirect = ''
            continue

        title_str = get_title(line)
        redirect_str = get_redirect(line)
    
        if title_str != None:
            title = title_str
            continue
    
        if redirect_str != None:
            redirect = redirect_str


