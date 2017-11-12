# Created by: Tochukwu Iroakazi
# Created on: Nov 2016
# Created for: ICS3U
# This program displays marks


def marks_number(number):
    if level == '4+' :
      score = 95
      return score
    elif level == '4':
       score = 90
       return score
    elif level == '4-' :
       score = 80
       return score
    elif level == '3+' :
       score = 78
       return score
    elif level == '3':
       score = 73
       return score
    elif level == '3-':
       score = 70
       return score
    elif level == '2+':
       score = 69
       return score
    elif level == '2':
       score = 65
       return score
    elif level == '2-':
       score = 60
       return score
    elif level == '1+':
       score = 59
       return score
    elif level == '1':
       score = 59
       return score
    elif level == '1-':
       score = 50
       return score
    elif level == 'R':
       score = 30
       return score
    else:
       score = -1
       return score

level = str(raw_input('Type in your level :'))
number = marks_number(level)
print(number)


# input is for integers
# raw_input for string 

