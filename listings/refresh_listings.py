import os
from collections import defaultdict

d = os.path.dirname(__file__)
pl = len('{}/'.format(os.path.dirname(d)))

ide_dir = '{}/flovver/ide'.format(d)
compiler_dir = '{}/flovver/compiler'.format(d)


ide_files = []
caption_cntr = defaultdict(int)

for path, subdirs, files in os.walk(ide_dir):
    for name in files:
        fn = os.path.join(path, name)
        if (fn.endswith('svelte') or fn.endswith('ts')):
            lstfmt = '\lstinputlisting[language={{HTML}},frame=none,numbers=none,label={{lst:{label}}}]{{{path}}}\n'
            caption = os.path.basename(fn)
            caption_cntr[caption] += 1
            label = caption.replace('.', '').lower() + str(caption_cntr[caption])
            lst = lstfmt.format(caption=caption, label=label, path=fn[pl:])
            ide_files.append('\\noindent\\textbf{{{caption}}}\n'.format(caption=caption))
            ide_files.append(lst)


compiler_files = []
caption_cntr = defaultdict(int)

for path, subdirs, files in os.walk(compiler_dir):
    for name in files:
        fn = os.path.join(path, name)
        if (fn.endswith('scala')):
            lstfmt = '\lstinputlisting[language={{Scala}},frame=none,numbers=none,label={{lst:{label}}}]{{{path}}}\n'
            caption = os.path.basename(fn)
            caption_cntr[caption] += 1
            label = caption.replace('.', '').lower() + str(caption_cntr[caption])
            lst = lstfmt.format(caption=caption, label=label, path=fn[pl:])
            compiler_files.append('\\noindent\\textbf{{{caption}}}\n'.format(caption=caption))
            compiler_files.append(lst)

with open(d + '/ide_listings', 'w') as l:
    l.writelines(ide_files)

with open(d + '/compiler_listings', 'w') as l:
    l.writelines(compiler_files)