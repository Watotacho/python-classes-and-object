class Car:
    def __init__(self,make,color,capacity,size):
          self.make=make
          self.color=color
          self.capacity=capacity
          self.size=size
    def hooting(self):
        return f"I love {self.make}.It is {self.color}in color and is{self.size} in size"
    def dailyCapacity(self):
        return self.capacity*10