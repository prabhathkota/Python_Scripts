import subprocess

def checkProcessRunning(cmd, processName):
    print "\n Process to check : " + cmd
    result = writeToCMD(cmd)
    if (result[0].rstrip().find(processName) != -1):
        print processName + " is present/running"
        return True
    else:
        print processName + " is not present/running"
        return False
    	    	
def writeToCMD(cmd):
    proc = None       
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell="True")
    stdout_value = proc.communicate()
    if stdout_value:
        return stdout_value

checkProcessRunning(cmd = "adb shell ps", processName = "com.android.phone")