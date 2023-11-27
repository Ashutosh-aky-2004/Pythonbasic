class Room:
    length=0
    breadth=0
    def calculate_area_of_rectangle(self):
        print("Area of Rectangle:",self.length*self.breadth)
study_Room=Room()
study_Room.length=10
study_Room.breadth=10
study_Room.calculate_area_of_rectangle()
