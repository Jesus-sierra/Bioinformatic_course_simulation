#rosalind3.py
#This script processes a Strings and lists
#Author: Jesus Sierra
#Date: 22/05/2024
string = "XuuCB9uAiH8XmeS0KGd41YQ4vDYfkOgbJSArctomysZBEncq8Wb8JTAWQ0dT74FP8xW4AT6septentrionalis1YILNGEuXpexpzX5M3GFsSv2K6M6NYw9nwQqXqtpiFAP3nJvgP7PPAgUGjM49ydrcIOFPKboV5tsCHOfWk5P6NuVzGG5QBNHVN8Nk2"
a = 34
b = 41
c = 71
d = 85
def ros3(string):
    part1 = string[a:b+1]
    part2 = string[c:d+1]
    print(part1, part2)
ros3(string)
