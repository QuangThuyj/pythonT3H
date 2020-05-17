html = '<span class="price">$1,53.43</span>'
bearer = '$'
pos = html.find(bearer)
if pos >= 0:
    start = pos + len(bearer)
    html = html[start:]
    end = html.find('</')
    html = html[:end]
print(html)

    
    
