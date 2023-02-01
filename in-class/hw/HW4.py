# -*- coding: utf-8 -*-
# HW4_String_File_Processing (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)

# - เขียนในเซลล์นี้เท่านั้น 
# - ถ้าต้องการเขียนฟังก์ชันเพิ่ม ก็เขียนในเซลล์นี้

# ตัวแปรต่อไปนี้เป็นตัวแปรที่กำหนดค่าสีเพื่อเอาไว้ใช้ในโปรแกรม (ห้ามแก้ไข)
RESET = '\033[0m'
RED = '\033[;31m'
GREEN = '\033[;32m'
BLUE = '\033[;34m'
HIGHLIGHT = '\033[;103m'

# ---------------------------------------------------
def red(s):
    return RED + s + RESET
# ---------------------------------------------------
def green(s):
    return GREEN + s + RESET
# ---------------------------------------------------
def blue(s):
    return BLUE + s + RESET
# ---------------------------------------------------
def highlight(s):
    return HIGHLIGHT + s + RESET
# ---------------------------------------------------
def color_text(s, color):
    color = color.lower()
    if color == 'red' :
        return red(s)
    elif color == 'green':
        return green(s)
    elif color == 'blue':
        return blue(s)
    return s
# ---------------------------------------------------
def color_tag(s):
    s = s.replace('<red>', RED)
    s = s.replace('<green>', GREEN)
    s = s.replace('<blue>', BLUE)
    s = s.replace('<highlight>', HIGHLIGHT)
    s = s.replace('</>', RESET)
    return s
# ---------------------------------------------------
def highlight_words(s, words):
    for word in words:
      s = s.replace(word, highlight(word))
    return s

# ---------------------------------------------------
def display_tag_file(filename):
    file = open(filename, 'r')#, encoding='utf-8')
    print(color_tag(file.read()))
    file.close()

print('red text:' + red('red text') + 'and normal text')
print('green text:' + green('green text') + 'and normal text')
print('blue text:' + blue('blue text') + 'and normal text')
print('highlight text:' + highlight('highlight text') + 'and normal text')

print(color_text('This is red text', 'red'))
print(color_text('This is green text', 'GreeN'))
print(color_text('This is blue text', 'BLUE'))
print(color_text('This is yellow text', 'yellow'))

print(color_tag('<red>red text</>'))
print(color_tag('<green>green text</>'))
print(color_tag('<blue>blue text</>'))

t = 'a[3]มิใช่ลิสต์ คืนค่ามิใช่print =มิใช่เปรียบเทียบ รักมิใช่ดวงดาวที่พราวแสง'
print(highlight_words(t,['มิใช่']))
print(highlight_words(t,['ลิสต์']))
print(highlight_words(t, []))
w = ['print', 'ดาว', 'มิใช่']
z = highlight_words(t, w)
print(z)

display_tag_file('มหาจุฬาลงกรณ์-tag.txt') 