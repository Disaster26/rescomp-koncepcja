import os
d=os.path.dirname(os.path.abspath(__file__))
r=lambda f:open(os.path.join(d,f),encoding='utf-8').read()
s=r('src.html').replace('{{BADGE_STYLE}}',r('_src/badge_style.part').strip()).replace('{{BADGE_LINK}}',r('_src/badge_link.part').strip())
assert '{{' not in s
assert '—' not in s
open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(s)
print(len(s))
