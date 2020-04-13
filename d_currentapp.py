import uiautomator2 as u2

d = u2.connect() # connect to device
print(d.app_current)
print(d.app_info('com.auxbrain.egginc'))

