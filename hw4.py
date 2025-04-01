def rep_char(c, n):
    return c*n

def draw_line_string(msg):
    print(sp)
    print(msg)
    print(wel)
    print(sp)
    
wel = ' Welcome to Seoul. '
hel = ' Hello ' + input('Input his/her name: ') + ', '

if len(hel) > len(wel):
    n = len(hel)
else:
    n = len(wel)

sp = rep_char('-',n)

draw_line_string(hel)