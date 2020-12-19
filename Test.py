# name=input('Enter form name: ')
name = 'Test-Form'
html = open(name+'.html', 'w')
def tab(n):
    str = ''
    for i in range(n):
        str += '    '
    return str

def markdownToHtml(text):
    return text

html.write('<!doctype html>'+'\n')
html.write('<html>'+'\n')
html.write(tab(1)+'<head>'+'\n')
html.write(tab(2)+'<title>')
html.write(name)
html.write('</title>'+'\n')
html.write(tab(1)+'</head>'+'\n')
html.write(tab(1)+'<body>'+'\n')
html.write(tab(2)+'<form>'+'\n')
n = int(input('Enter number of questions: '))
for i in range(n):
    html.write(tab(3)+'<hr>'+'\n')
    html.write(tab(3)+'<div>'+'\n')
    ques = input('Enter the question: ')
    ques = markdownToHtml(ques)
    html.write(tab(4)+ques+'<br>'+'\n')
    html.write(tab(4)+'<input type="text" placeholder="Enter your name">'+
    '<br>'+'\n')
    html.write(tab(4)+'<input type="submit" value="submit">'+'\n')
    html.write(tab(3)+'</div>'+'\n')
html.write(tab(3)+'<hr>'+'\n')
html.write(tab(2)+'</form>'+'\n')
html.write(tab(1)+'</body>'+'\n')
html.write('</html>'+'\n')
