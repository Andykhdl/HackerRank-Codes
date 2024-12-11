import re

def parse_html(n, l):
    html = '\n'.join(l)

    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

    t = r'<\s*([a-zA-Z0-9]+)([^>]*)>'
    a = r'([a-zA-Z-]+)="([^"]*)"'

    for match in re.finditer(t, html):
        tn = match.group(1)
        print(tn)
        
        at = match.group(2)
        for attr_match in re.finditer(a, at):
            attr_name = attr_match.group(1)
            attr_value = attr_match.group(2)
            print(f"-> {attr_name} > {attr_value}")

n = int(input())
lines = [input() for _ in range(n)]
parse_html(n, lines)