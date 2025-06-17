# app.py
import django
import subprocess

def insecure_function(user_input):
    # Command injection vulnerability (compliance issue)
    subprocess.call("echo " + user_input, shell=True)

if __name__ == "__main__":
    user_input = input("Enter something: ")
    insecure_function(user_input)
