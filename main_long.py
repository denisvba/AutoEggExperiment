import uiautomator2 as u2

d = u2.connect() # connect to device

sec_count = 20
for i in range(sec_count):
    d.long_click(550, 2145, 30)
    print (i)
