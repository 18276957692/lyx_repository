class people():
    def __init__(self,people_number,people_name,people_gender):
        self.people_number=people_number
        self.people_name=people_name
        self.people_gender=people_gender

def get_people_list(people_sum):
    assert people_sum>0

    people_list=[]
    for i in range(people_sum):
        people_number=i+1
        print("请输入第%d个人的姓名"%(i+1))
        people_name=input()
        print("请输入第%d个人的性别(man/women)"%(i+1))
        people_gender=input()
        people_list.append(people(people_number,people_name,people_gender))
    return people_list

def Josephus_problem(people_list,killed_step,killed_index):
    assert len(people_list)>0
    assert killed_step>0
    assert killed_index<=len(people_list)

    killed_index=(killed_index+killed_step-1)%len(people_list)
    people_list.pop(killed_index)
    return people_list,killed_index

def Josephus_survival_list():
    killed_index=0
    for i in range(len(people_list)-1):
        (survival_list,killed_index)=Josephus_problem(people_list,3,killed_index)
        print("当前还剩%d个人"%len(survival_list))
        for people in survival_list:
            print(people.people_number,people.people_name,people.people_gender)

if __name__ == '__main__':
    people_list=get_people_list(3)
    Josephus_survival_list()