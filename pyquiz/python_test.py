x=[100,110,120,130,140,150]
for b in x:print(b*5)
#2
def divisible_by_three(n):
    for number in range(1,n):
        if number%3==0:
            print(number)

divisible_by_three(16)
#3

x = [[1,2],[3,4],[5,6]]
new_list = []

for lists in x:
    for numbers in lists:
        new_list.append(numbers)

print(new_list)

def divisible_by_seven():
    all_numbers = []
    for number in range(100,200):
        if number%7==0:
            all_numbers.append(number)
    print(all_numbers)

divisible_by_seven()




#6
x=range(100.200)
for b in x:
    if b%7==0:
        print(b)


#5
x=['a','b','a','e','d','b','c','e','f','g','h']
b=set(x)
print(b)
#7
students=[{"age":19,"name":"eunice"},{"age":21,"name":"Agnes"},{"age":18,"name":"Teresa"},{"age":22,"name":"sarah"}],
for student in students:
    name=student['name']
    age=students['age']
   # sentence={f" {} you were born {}"

class Rectangle():
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area():
        return 6*5
    def perimeter():
        return 8*6









