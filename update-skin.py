import subprocess

print "start update skin"
subprocess.call(["/usr/bin/git", "--git-dir=/home/pi/.kodi/addons/skin.CarPC-touch_carbon/.git", "--work-tree=/home/pi/.kodi/addons/skin.CarPC-touch_carbon" ,"pull"])
print "end update skin"
