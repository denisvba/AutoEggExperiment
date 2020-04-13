import uiautomator2 as u2

d = u2.connect() # connect to device

sec_count = 6000

for i in range(sec_count):
     d.click(550, 2145)