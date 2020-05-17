sales = [
	{'qty': 2, 'time': '2019-01-01 08:45'},
	{'qty': 3, 'time': '2019-01-01 09:33'},
	{'qty': 4, 'time': '2019-01-01 16:35'},
	{'qty': 5, 'time': '2019-01-02 10:40'},
	{'qty': 1, 'time': '2019-01-02 13:55'},
	{'qty': 2, 'time': '2019-01-02 17:20'},
	{'qty': 5, 'time': '2019-01-02 09:42'},
	{'qty': 3, 'time': '2019-01-03 14:42'},
	{'qty': 3, 'time': '2019-01-03 15:55'},
	{'qty': 1, 'time': '2019-01-03 17:10'},
]


so_sp = {}
for sale in sales:
    qty, day = sale['qty'], sale['time'][:10]
    so_sp[day] = so_sp.get(day, 0) + qty

print(so_sp)
