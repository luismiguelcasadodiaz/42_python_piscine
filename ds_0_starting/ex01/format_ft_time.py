import time
now = time.time()
a = f"Seconds since January 1, 1970: {now:,.4f} "
a = a + f"or {now:.2e} in scientific notation"
print(a)
print(time.strftime("%b %d %Y", time.localtime()))
