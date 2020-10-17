class Student:

    def __init__(self,name):
        self.name=name

    def calculateAvg(self,score):
        
        sum = 0

        for num in score:

            sum += num

        avg = sum/len(score)

        return avg

    def judge(self,avg):

        if(avg>=60):
            print("合格!")

        else:
            print("不合格!")

a001 = Student("飯島")
score = [60,60,0,80]
avg = a001.calculateAvg(score)
a001.judge(avg)
