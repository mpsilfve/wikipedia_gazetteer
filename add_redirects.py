from sys import argv, stderr
from pickle import dump
from copy import copy

if len(argv) != 4:
    stderr.write('USAGE: %s infobox_categories redirects ofile\n' % argv[0])
    exit(1)

info_categories = {w:c for w,c in [l.split('\t') for l in open(argv[1]).read().split('\n') if l != '']}
redirects = {w:r for w,r in [l.split('\t') for l in open(argv[2]).read().split('\n') if l != '']}

ofile = open(argv[3],'wb')

for w, r in redirects.items():
    if not w in info_categories:
        if r in info_categories:
            info_categories[w] = info_categories[r]

gazetteer = {}

for w,c in info_categories.items():
    k = w
    if w[-1] == ')' and w.count(' (') == 1:
        ind = w.find(' (')
        k = w[:ind]
    if not k in gazetteer:
        gazetteer[k] = set()
    gazetteer[k].add(c)

gazetteer_lc = copy(gazetteer)
for w,c in gazetteer.items():
    if not w.lower() in gazetteer:
        gazetteer_lc[w.lower()] = c

dump(gazetteer_lc,ofile)

