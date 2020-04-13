import uiautomator2 as u2

d = u2.connect() # connect to device

sec_count = 6000

for i in range(sec_count):
     d.double_click(550, 2145, 0.01)
     print(i)
