# app.py
import django
import subprocess

# Example of a fake AWS secret access key (for testing secret scanning)
aws_secret = "AKIA1234567890FAKEKEYEXAMPLE"

def insecure_function(user_input):
    # Command injection vulnerability (compliance issue)
    subprocess.call("echo " + user_input, shell=True)

if __name__ == "__main__":
    user_input = input("Enter something: ")
    insecure_function(user_input)
