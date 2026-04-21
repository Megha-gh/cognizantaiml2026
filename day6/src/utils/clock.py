import asyncio
import time
async def create_clock():
    while True:#infiity loop
        print(time.strftime("%H:%M:%S", time.localtime()))
        """
        pauses the execution of the loop for 1 second, 
        allowing other tasks to run concurrently .
        this is useful in an asynchronous environment where you want to 
        avoid blocking the event loop while waiting for a certain amount 
        of time to pass. and to allow other tasks to run concurrently without blocking the
         main thread of execution.
        """
        await asyncio.sleep(1)
if __name__ == "__main__":
    asyncio.run(create_clock())