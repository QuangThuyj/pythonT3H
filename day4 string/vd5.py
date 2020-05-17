st = 'Reply from 216.58.200.14: bytes=32 time=67ms TTL=49'

bearer = 'time='
pos = st.find(bearer)
if pos >= 0:
    start = pos + len(bearer)
    print(st[start:])
    st = st[start:]
    pos2 = st.find('ms')
    end = pos2
    print(st[:end])
