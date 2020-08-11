#zodiac_list = ['쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이', '닭', '개', '돼지']

def zodiac_animals(birth_year):
    my_zodiac = ''
    years = [1900+12*i for i in range(0,11)]
    for year in years:
        if birth_year == year:
            my_zodiac = '쥐'
        elif birth_year == year+1:
            my_zodiac = '소'
        elif birth_year == year+2:
            my_zodiac = '호랑이'
        elif birth_year == year+3:
            my_zodiac = '토끼'
        elif birth_year == year+4:
            my_zodiac = '용'
        elif birth_year == year+5:
            my_zodiac = '뱀'
        elif birth_year == year+6:
            my_zodiac = '말'
        elif birth_year == year+7:
            my_zodiac = '양'
        elif birth_year == year+8:
            my_zodiac = '원숭이'
        elif birth_year == year+9:
            my_zodiac = '닭'
        elif birth_year == year+10:
            my_zodiac = '개'
        elif birth_year == year+11:
            my_zodiac = '돼지'
        else:
            continue
        return my_zodiac

mine = zodiac_animals(1998)
print(mine)