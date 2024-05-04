import time
for x in reversed(range(65)) :
    second=x%60
    minutes=int(x/60)
    print(f"00.{minutes}.{second:02}")
    time.sleep(1)