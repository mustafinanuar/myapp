import time
import os
import redis

#r = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=6379, decode_responses=True)

while True:
    count = r.incr("tick_counter")
    print(f"tick #{count} (значение хранится в Redis, переживает рестарт контейнера)", flush=True)
    time.sleep(5)

