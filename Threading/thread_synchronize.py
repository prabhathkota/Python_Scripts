import threading
import time

"""
Synchronous will allow only one thread to run at any time
When a thread acquires a lock, no other thread can run at that same instant
"""

class myThread (threading.Thread):
    def __init__(self, threadID, threadName, threadDelay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName
        self.threadDelay = threadDelay
        
    def run(self):
        print "Starting " + self.threadName
        # Get lock to synchronize threads
        threadLock.acquire()
        print self.threadName + " Lock Acquired"
        print_time(self.threadName, 5, self.threadDelay)
        # Free lock to release next thread
        threadLock.release()
        print self.threadName + " Lock Released"

def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(threadID = 1, threadName = "Thread-1", threadDelay = 1)
thread2 = myThread(threadID = 2, threadName = "Thread-2", threadDelay = 2)
thread3 = myThread(threadID = 3, threadName = "Thread-3", threadDelay = 3)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
 
# Add threads to thread list
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

# Wait for all threads to complete
for t in threads:
    t.join()
    
print "Exiting Main Thread"