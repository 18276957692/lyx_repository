def Josephus_Ring_problem(killed_num,people_sum):
    suvive_num_index=0
    for i in range (people_sum):
        suvive_num_index=(suvive_num_index+killed_num)%(i+1)
    return suvive_num_index+1
if __name__ == '__main__':
    actual_suvive_num=Josephus_Ring_problem(3,41)
    print(actual_suvive_num)
