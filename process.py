// codeme71 2025 

import cgi, cgitb, subprocess
cgitb.enable()

form = cgi.FieldStorage()

# Получаем число из формы
number = form.getvalue('number')

# Выполняем вашу пользовательскую программу
process = subprocess.run(['/usr/bin/kiss', number], capture_output=True, text=True)
output = process.stdout

print("Content-type:text/html\r\n\r\n")
print(f"<p>Результат: {output}</p>") 

