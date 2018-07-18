"""
Probably one of the largest drawbacks to the Python programming languages is that it is single-threaded. This means that Python will only run on a single thread naturally. If you have a large computational task, you might have already found that it takes Python a very long time to reach a solution, and yet, your processor might sit at 5% usage or even less. There are quite a few solutions to this problem, like threading, multiprocessing, and GPU programming. All of these are possible with Python, and today we will be covering threading. So, what is threading within the frame of Python? Threading is making use of idle processes, to give the appearance of parallel programming. With threading alone in Python, this is not really the case, but we can indeed use threading to make use of idle times and still gain some significant performance increases.

Along with the video above, here is some explained sample code for threading in Python 3:


"""
import threading
from queue import Queue
import time

"""
So far, we've imported threading, queue and time. Threading is for, well, threading, queue is going to help us make, you guessed it, a queue! Finally, we import time. Our only reason for importing time here is to simulate some idle time with a time.sleep() function.

Next, we're going to define a thread lock. The idea of a threading lock is to prevent simultaneous modification of a variable. So, if two processes begin interaction with a variable with it is, say, 5, and one operation adds 2, and the other adds 3, we're going to end with either 7 or 8 as the variable, rather than having it be 5+2+3, which would be 10. A lock will force an operation to wait until the variable is unlocked in order to access and modify it. Another use for a lock is to aid in input/output. With threading, it becomes quite easy to have two processes modifying the same file, and the data will literally just run over each other. So say you are meaning to save two values, like "Monday" and "Tuesday" to a file, you are intending for the file to just read: "Monday Tuesday," but instead it winds up looking like "MoTunedsadyay." A lock helps this.
"""
print_lock = threading.Lock()

"""
Here, we're looking to use the lock to stop print functions from running over each other in their output.

Now we're ready to create some sort of task to show off threading with:
"""
def exampleJob(worker):
    time.sleep(.5) # pretend to do some work.
    with print_lock:
        print(threading.current_thread().name,worker)

"""
So we define this exampleJob function, with a parameter of worker. With that job, we pretend to do something that will cause some idle, and that is just a time.sleep. After that, we use the print lock, which locks while we're doing some output to prevent overlapping. Once the with statement completes, the lock will automatically unlock.

Now we need something that will assign tasks to our threads. Here, we're calling our threads workers.
"""

# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        exampleJob(worker)

        # completed with the job
        q.task_done()


"""
I'll let the commenting speak for how this one works, as it would be too confusing to split this one up. See the video as well for more explanation if you need it.

Now we've used this "q," but we've not defined it, so we had better do that:
"""

# Create the queue and threader
q = Queue()

"Now let's create our threads, and put them to work!"

# how many threads are we going to allow for
for x in range(10):
     t = threading.Thread(target=threader)

     # classifying as a daemon, so they will die when the main dies
     t.daemon = True

     # begins, must come after daemon definition
     t.start()

start = time.time()

# 20 jobs assigned.
for worker in range(20):
    q.put(worker)

# wait until the thread terminates.
q.join()

# with 10 workers and 20 tasks, with each task being .5 seconds, then the completed job
# is ~1 second using threading. Normally 20 tasks with .5 seconds each would take 10 seconds.
print('Entire job took:',time.time() - start)
