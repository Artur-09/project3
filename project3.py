import time

minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds = minutes * 60 + seconds


while total_seconds > 0:
    
    mins, secs = divmod(total_seconds, 60)
    print(f"{mins:02d}:{secs:02d}")
    time.sleep(1)
    total_seconds -= 1

print("Time is up!")