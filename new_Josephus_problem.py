class people():
    def __init__(self,people_number,people_name,people_gender):
        self.people_number=people_number
        self.people_name=people_name
        self.people_gender=people_gender

def input_people_list():
    people_list=[]
    print("请输入参与人数总和：")
    people_sum=int(input())
    assert people_sum>0

    for i in range(people_sum):
        people_number=i+1
        print("请输入第%d个人的姓名"%(i+1))
        people_name=input()
        print("请输入第%d个人的性别"%(i+1))
        people_gender=input()
        people_list.append(people(people_number,people_name,people_gender))
    return people_list

def josephus_problem(people_list,killed_step,killed_index):
    assert len(people_list)>0
    assert killed_step>0
    assert killed_index<=len(people_list)

    killed_index=(killed_index+killed_step-1)%len(people_list)
    people_list.pop(killed_index)
    return people_list,killed_index

def josephus_survival_list(killed_step,killed_index):
    for i in range(len(people_list)-1):
        (survival_list,killed_index)=josephus_problem(people_list,killed_step,killed_index)
        print("当前剩余%d人："%len(survival_list))
        for people in survival_list:
            print(people.people_number,people.people_name,people.people_gender)

if __name__ == '__main__':
    people_list=input_people_list()
    josephus_survival_list(3,0)