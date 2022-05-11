import time


def get_timer():
    print("Enter the number of seconds for your timer")
    seconds = input("> ")
    while not seconds.isdigit():
        seconds = input("Enter a NUMBER > ")
    return int(seconds)


def set_timer(seconds):
    print("Timer starts... NOW")
    for i in range(1, seconds + 1):
        print(f"\t{i}...")
        time.sleep(1)
    print("DRING !!!")

if __name__ == "__main__":
    print("=== TIMER ===")
    timer = get_timer()
    set_timer(timer)
