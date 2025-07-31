from threading import Semaphore, Lock

class DiningPhilosophers:
    def __init__(self):
        self.sizelock = Semaphore(4)
        self.locks = [Lock() for _ in range(5)]

    def wantsToEat(self, index, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        left, right = index, (index - 1) % 5
        with self.sizelock:
            with self.locks[left], self.locks[right]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
