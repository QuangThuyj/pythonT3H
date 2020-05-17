products = [
    ('P1', 2.0),
    ('P2', 3.5),
    ('P3', 4.0),
    ('P4', 2.5),
    ('P5', 3.75),
]

#0 - 2.5 kem
#2 - 3.8 TB
# > 3.8 Tot
sp_kem = []
sp_tot = []
sp_tb = []
for item in products:
    name, vote = item
    if vote < 2.5:
        sp_kem.append(name)
    elif 2.5<= vote < 3.8:
        sp_tb.append(name)
    else:
        sp_tot.append(name)
print(sp_tot)
print(sp_tb)
print(sp_kem)

#sp_kem = [name for (name, vote) in products if vote < 2.5]
