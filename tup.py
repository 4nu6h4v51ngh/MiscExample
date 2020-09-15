tup=[(1,2,3),(11,12,13),(14,15,16),(17,18,19)]
print(tup)
print(type(tup))
print([t[:-1] + (100,) for t in tup])