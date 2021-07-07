import random
import string
str=string.ascii_letters+string.digits
def get_verification_code(length):
    for n in range(200):
        result=''
        for m in range(length):
            res=str[random.randint(0,len(str)-1)]
            result += res
        print(result)
      
if __name__ == '__main__':
    get_verification_code(10)
