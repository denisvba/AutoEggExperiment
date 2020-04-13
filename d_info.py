import uiautomator2 as u2

d = u2.connect() # connect to device
print(d.info)
print(d.app_info('com.auxbrain.egginc'))
print(d.device_info)


