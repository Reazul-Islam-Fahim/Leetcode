from threading import Condition

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.cv = Condition()

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 3 != 0 or self.current % 5 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    break
                printFizz()
                self.current += 1
                self.cv.notify_all()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 5 != 0 or self.current % 3 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    break
                printBuzz()
                self.current += 1
                self.cv.notify_all()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.current <= self.n and self.current % 15 != 0:
                    self.cv.wait()
                if self.current > self.n:
                    break
                printFizzBuzz()
                self.current += 1
                self.cv.notify_all()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 3 == 0 or self.current % 5 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    break
                printNumber(self.current)
                self.current += 1
                self.cv.notify_all()
