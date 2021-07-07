#import time
def split_the_file(file_name,split_size):
    with open(file_name,"r") as file:
        while True:
            split_part =file.read(split_size)  
            if  split_part:
                yield split_part
            else:
                return None 
    file.close()   

def get_split_file(file_name,split_size):
    num=1
    for part in split_the_file(file_name,split_size):
        print("Successfully split %d!"%num)
        num+=1          
if __name__ == '__main__':
    #begin=time.time()
    
    get_split_file("test.txt",1024*4)
    
    #end=time.time()
    #print('Time is %d second'%(end-begin))