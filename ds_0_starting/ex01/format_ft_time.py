import time
now = time.time()




print(f"Seconds since January 1, 1970: {now:,.4f} or {now:.2e} in scientific notation")
print(time.strftime("%b %d %Y",time.localtime()))
