import os

if os.path.exists("/Users/yangqianxian/Documents/workspace/gaea-service"):
    os.chdir('/Users/yangqianxian/Documents/workspace/gaea-service')
    os.system('git fetch')
    os.system('git rebase origin/master')

else:
    print "no dir found"