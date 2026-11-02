import os,re,json,html
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
R="/home/claude/littlegasp.github.io"
pages=sorted(os.path.relpath(os.path.join(d,f),R) for d,_,fs in os.walk(R) if not os.path.relpath(d,R).startswith(('.git','vendor')) for f in fs if f.endswith('.html'))
class P(HTMLParser):
  def __init__(s): super().__init__(); s.refs=[]; s.meta={}; s.links={}; s.h1=0; s.title=''; s._t=False; s.imgs=[]; s.ld=[]; s._ld=False; s.ids=set()
  def handle_starttag(s,t,a):
    a=dict(a)
    if 'id' in a: s.ids.add(a['id'])
    for k in ('href','src'):
      if k in a and a[k]: s.refs.append((t,a[k]))
    if t=='meta': s.meta[a.get('name') or a.get('property') or a.get('charset','x')]=a.get('content','')
    if t=='link' and 'rel' in a: s.links.setdefault(a['rel'],[]).append(a.get('href'))
    if t=='h1': s.h1+=1
    if t=='title': s._t=True
    if t=='img': s.imgs.append(a)
    if t=='script' and a.get('type')=='application/ld+json': s._ld=True; s.ld.append('')
  def handle_endtag(s,t):
    if t=='title': s._t=False
    if t=='script': s._ld=False
  def handle_data(s,d):
    if s._t: s.title+=d
    if s._ld: s.ld[-1]+=d
issues=[]; info={}
def exists(page,ref):
  u=urlparse(ref)
  if u.scheme in('http','https') :
    if u.netloc in('littlegasp.com','www.littlegasp.com'): path=u.path
    else: return None
  elif u.scheme in('mailto','tel','data','javascript'): return None
  elif ref.startswith('#') or ref=='' : return None
  else: path=u.path
  if '${' in path or '{' in path: return None
  if path.startswith('/'): f=R+unquote(path)
  else: f=os.path.normpath(os.path.join(R,os.path.dirname(page),unquote(path)))
  if f.endswith('/'): f+='index.html'
  if os.path.isdir(f): f+='/index.html'
  return os.path.exists(f)
for pg in pages:
  src=open(os.path.join(R,pg),encoding='utf-8').read()
  p=P(); p.feed(src)
  for t,ref in p.refs:
    ok=exists(pg,ref)
    if ok is False: issues.append(f"BROKEN {pg}: <{t}> {ref}")
  # css url()
  for ref in re.findall(r'url\((["\']?)([^)"\']+)\1\)',src):
    r=ref[1]
    if r.startswith(('data:','http','#','var(')) or '$' in r or '{' in r: continue
    if exists(pg,r) is False: issues.append(f"BROKEN-CSS {pg}: {r}")
  for b in p.ld:
    try: json.loads(b)
    except Exception as e: issues.append(f"BAD JSON-LD {pg}: {e}")
  info[pg]=dict(title=p.title.strip(),desc=p.meta.get('description',''),robots=p.meta.get('robots',''),canon=(p.links.get('canonical') or [None])[0],h1=p.h1,og=p.meta.get('og:image'),ogt=p.meta.get('og:title'),noalt=sum(1 for i in p.imgs if 'alt' not in i),viewport='viewport' in p.meta, lang='lang="en"' in src[:300], ld=len(p.ld))
json.dump(info,open('/tmp/claude-0/audit/info.json','w'),indent=1)
print("\n".join(issues) or "no broken refs")
print()
for pg,i in info.items():
  flags=[]
  idx = i['robots']!='noindex'
  if not i['title']: flags.append('no title')
  elif idx and not (25<=len(i['title'])<=65): flags.append(f"title len {len(i['title'])}")
  if idx and not (110<=len(i['desc'])<=165): flags.append(f"desc len {len(i['desc'])}")
  if idx and not i['canon']: flags.append('no canonical')
  if i['h1']!=1: flags.append(f"h1={i['h1']}")
  if not i['og']: flags.append('no og:image')
  if i['noalt']: flags.append(f"{i['noalt']} img no alt")
  if not i['viewport']: flags.append('no viewport')
  if not i['lang']: flags.append('no lang')
  print(f"{'IDX ' if idx else 'NOIX'} {pg:45} {', '.join(flags)}")
