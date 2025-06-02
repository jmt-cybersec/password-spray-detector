# 🔐 Password Spray Detector

A simple Python script that detects possible password spray attacks by checking for multiple failed login attempts from the same IP address using different usernames.

## 📚 What is a Password Spray Attack?

Unlike brute-force attacks (which try many passwords on one account), password spraying tries **one password on many different usernames**, hoping that one works.

## 🔍 What This Script Does

- Reads a log file (`logs.txt`)
- Tracks failed login attempts
- Flags any IP that fails to log in using **3 or more different usernames**

## 🧪 Sample Log Input

Jan 01 00:00:01 LOGIN FAIL: user=john ip=192.168.1.10
Jan 01 00:00:02 LOGIN FAIL: user=alice ip=192.168.1.10
Jan 01 00:00:03 LOGIN FAIL: user=bob ip=192.168.1.10
Jan 01 00:00:04 LOGIN SUCCESS: user=admin ip=192.168.1.11


## ▶️ How to Run This Script

Make sure you have Python 3 installed on your computer.

Run the script:
Now run the script with Python 3:
python3 spray_detector.py

## 🖥️ Sample Output
⚠️ Possible password spray detected from IP 192.168.1.10: attempted logins for 3 users

**🙋 About Me**
I'm currently studying Computing and Information Systems with a minor in AI/ML. 
I'm building small, real-world security tools to learn how Python and automation play a role in modern cybersecurity.

GitHub: [@jmt-cybersec](https://github.com/jmt-cybersec)

