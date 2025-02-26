import cv2
import os
import string

img = cv2.imread("/content/Screenshot 2024-04-30 221446.png") # Replace with the correct image path

msg = input("Enter secret message:")
password = input("Enter a passcode:")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("/content/encryptedImage.jpg", img)
os.system("xdg-open /content/encryptedImage.jpg")  # Use 'xdg-open' for Linux or 'open' for macOS

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption:")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
