def show_log():
    f = open("/var/log/mysql/mysql.log", 'r')
    while True:
        line = f.readline()
        if not line: break
        print(line)
    f.close()