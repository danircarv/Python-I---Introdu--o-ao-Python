import winsound

for i in range(11):
    if i >= 0:
        print(10-i)
        winsound.Beep(800, 1000)
print("beep")
winsound.Beep(900, 1500)
    