import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, threadName, threadDelay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName
        self.threadDelay = threadDelay
        
    def run(self):
        print "Starting " + self.threadName
        print_time(self.threadName, 5, self.threadDelay)
        print "Exiting " + self.threadName

def print_time(threadName, counter, delay):
    while counter:
#         if exitFlag:
#             print "\n ----------------"
#             threadName.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

# Create new threads
thread1 = myThread(threadID = 1, threadName = "Thread-1", threadDelay = 1)
thread2 = myThread(threadID = 2, threadName = "Thread-2", threadDelay = 2)

# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"