import subprocess

print "start update skin"
subprocess.call(["/usr/bin/git", "pull"])
print "end update skin"
