from golly_maps import maps

rows = 100
cols = 120

m = maps.get_map_realization('twomultum', rows=rows, columns=cols)
print("http://192.168.30.20:8888/simulator/index.html" + m['url'] + f"&rows={rows}&cols={cols}&cellSize=5")
