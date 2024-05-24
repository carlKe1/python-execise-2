# You are given a file called logfile.txt that lists log-on and log-off times for users of a
# system. A typical line of the file looks like this:
# Van Rossum, 14:22, 14:37

with open("logfile.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    username, login_time, logout_time = line.strip().split(", ")
    login_hour, login_minute = map(int, login_time.split(":"))
    logout_hour, logout_minute = map(int, logout_time.split(":"))
    total_minutes = (logout_hour * 60 + logout_minute) - (login_hour * 60 + login_minute)
    if total_minutes >= 60:
        print(username)
