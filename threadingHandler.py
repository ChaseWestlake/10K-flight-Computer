import threading

#Setting up threading for main.
# Note: Threading may not speed up all tasks due to the GIL (Global Interpreter Lock). 
# source:https://www.datacamp.com/community/tutorials/threading-in-python


#references:    1: https://www.datacamp.com/community/tutorials/threading-in-python
#               2: https://docs.python.org/3/library/threading.html#:~:text=%20Thread%20Objects%20%C2%B6%20%201%20start%20%28%29,%206%20isDaemon%20%28%29%20%C2%B6.%20%20More%20              

#Created:   Aug 23, 2021

#Written by:    Chase Westlake

#Description:   Intent to write threading for UVic Rocketry Flight Computer.
#               Currently under testing cases. 

#Requirements:  -   Thread transmitting data
#               -   Thread recieveing data and instructions
#               -   Thread Reading GPIO


#Progress:  currently lacks functionality to complete tasks assigned from flight computer.
#           bug at line 32 - 34. Class does not want to let the threading module run start(). 
#           I also attempted to run the start in my testing file. Needs some work. Recommendations and
#           course correction welcome.


import threading    
import time         

class ThreadingHandler:
    
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        
    def __setup(self, name, delay):
        self.name = name
        self.delay = delay
    
    def getThread(self):
        return self.name
    
    def getDelay(self):
        return self.delay
    
    
    
    def run(self):
        
        #information on line 50 is contained in references (1).
        threading.Thread(target=self.threadDelay, args=(self.name, self.delay))
        print('\nStarting Thread:', self.name, "\nWith a delay of:", self.delay)
        # self.start()
        # (self.name).start()
        # self.name.start()
        print('\nExecution of Thread:', self.name, 'is complete\n')
    
    
    #information on threadDelay() contained in references (1).  
    def threadDelay(name, delay):
    
        count = 0
    
        while count < 3:
            time.sleep(delay)
            count += 1
            print(name, '------>', time.localtime(time.time())[5], 'seconds')
