import requests
import json
import sys
import socket


def statusvalidator(sitename):
    try:
        response = requests.get("https://{0}".format(sitename), timeout = 5)
        if response.status_code == 200:
            return True
    except Exception as e:
        return e

def portvalidator(sitename, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            conresult = s.connect_ex((sitename, port))
            if conresult == 0:
                return True
            else:
                return False
    except Exception as e:
           return e

def main():
    try:
        if len(sys.argv) > 1:
            first_argument = sys.argv[1]
            second_argument = int(sys.argv[2])
        else:
            return False
        site=first_argument
        port=second_argument
        connector = {}
        connector["Status_code_valdiation"] = statusvalidator(site)
        connector["port_valdiation"] = portvalidator(site, port)
        print(json.dumps(connector))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
