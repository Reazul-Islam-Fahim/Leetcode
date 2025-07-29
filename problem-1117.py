from threading import Semaphore, Barrier
from typing import Callable

class H2O:
    def __init__(self):
        self.h_semaphore = Semaphore(2)
        self.o_semaphore = Semaphore(1)
        self.barrier = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_semaphore.acquire()
        self.barrier.wait()
        releaseHydrogen()
        self.h_semaphore.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_semaphore.acquire()
        self.barrier.wait()
        releaseOxygen()
        self.o_semaphore.release()
