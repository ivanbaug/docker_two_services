from datetime import datetime


def run():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time: ", current_time)

if __name__ == "__main__":
    run()