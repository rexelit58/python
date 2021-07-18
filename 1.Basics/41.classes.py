#we use classes to define a new type and that type can have methods in body of the class.
#They can have attibutes which can be set from anywhere from the program
class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1=Point()
point1.x=10
point1.y=20
print(point1.x)
point1.draw()