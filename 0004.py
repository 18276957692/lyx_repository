#任一个英文的纯文本文件，统计其中的单词出现的个数。
import re
def count_words_in_file(file_name):
    file=open(file_name,'r')
    word_counts=0
    for line in file:
        alter_line=re.sub(r'[.?!,""/]',' ',line)
        for word in alter_line.split():
            word_counts +=1
    print(word_counts)

if __name__ == '__main__':
    count_words_in_file("004test.txt")