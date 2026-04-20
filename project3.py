import time

def get_time_input(name):
    while True:
        try:
            value = input(f"Enter {name}: ").strip()

            if value == "":
                print("Input cannot be blank. Try again.")
                continue

            value = int(value)

            if value < 0:
                print("Value cannot be negative. Try again.")
                continue

            return value

        except ValueError:
            print("Please enter a numeric value.")


minutes = get_time_input("minutes")
seconds = get_time_input("seconds")

if seconds >= 60:
    print("Seconds should be less than 60.")
    exit()

total_seconds = minutes * 60 + seconds

while total_seconds > 0:
    mins, secs = divmod(total_seconds, 60)
    print(f"{mins:02d}:{secs:02d}")
    time.sleep(1)
    total_seconds -= 1

print("Time is up!")
