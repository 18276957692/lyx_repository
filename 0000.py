from PIL import Image, ImageDraw, ImageFont

def add_num(image_name,unread_message):
    image=Image.open(image_name)#打开图片
    font = ImageFont.truetype("arial.ttf",70)#设置字体
    width,height = image.size#获取图片宽度，高度
    draw = ImageDraw.Draw(image)
    draw.text((width-120,20),unread_message,font=font,fill='red')#图片写入数字
    image.save('final-QQ-image.jpg')#图片另存为

if __name__ == '__main__':
    add_num('QQ-photo.jpg','99+')
    