"""Public contribution HTML parser. Refuse missing counts rather than invent data."""
import re
import urllib.request
from html.parser import HTMLParser

class CalendarParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.days = []
        self.counts = {}
        self.tip = None
        self.text = ''
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'td' and a.get('data-date'):
            m = re.fullmatch(r'contribution-day-component-(\d+)-(\d+)', a.get('id', ''))
            if m:
                self.days.append({'col':int(m[2]), 'row':int(m[1]), 'date':a['data-date'], 'level':int(a['data-level']), 'id':a['id']})
        if tag == 'tool-tip' and a.get('for','').startswith('contribution-day-component-'):
            self.tip = a['for']; self.text = ''
    def handle_data(self, data):
        if self.tip: self.text += data
    def handle_endtag(self, tag):
        if tag == 'tool-tip' and self.tip:
            m = re.match(r'([\d,]+)\s+contributions?\b', self.text.strip())
            if m: self.counts[self.tip] = int(m[1].replace(',',''))
            elif self.text.strip().startswith('No contributions'): self.counts[self.tip] = 0
            self.tip = None

def fetch_contributions_html(username):
    req = urllib.request.Request(f'https://github.com/users/{username}/contributions', headers={'User-Agent':'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        text = r.read().decode('utf-8')
    p = CalendarParser(); p.feed(text)
    if len(p.days) < 350: raise RuntimeError('Contribution calendar incomplete; refusing empty output')
    for d in p.days:
        ident = d.pop('id')
        if ident not in p.counts: raise RuntimeError(f'Missing exact contribution count for {d["date"]}')
        d['count'] = p.counts[ident]
    p.days.sort(key=lambda d:d['date'])
    return p.days, sum(d['count'] for d in p.days)
