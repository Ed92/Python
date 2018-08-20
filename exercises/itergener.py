class MyIterator(object):
    def __init__(self, step):
        self.step = step
    def next(self):
        # Returns the next element.
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step
    def __iter__(self):
        # returns the iterator self.
        return self

for el in MyIterator(4):
    print(el)
