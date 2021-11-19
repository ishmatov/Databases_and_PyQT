# Табличное представление списка словарей
from tabulate import tabulate


def tab1():
    tuples_list = [('Python', 'interpreted', '1991'),
                   ('JAVA', 'compiled', '1995'),
                   ('С', 'compiled', '1972')]
    columns = ['programming language', 'type', 'year']
    # Указание заголовков в параметре headers
    print(tabulate(tuples_list, headers=columns))


def tab2():
    tuples_list = {('programming language', 'type', 'year'),
                   ('Python', 'interpreted', '1991'),
                   ('JAVA', 'compiled', '1995'),
                   ('С', 'compiled', '1972')}
    # Указание первой строки таблицы как набора заголовков
    print(tabulate(tuples_list, headers='firstrow'))


def tab3():
    dicts_list = [{'programming language': 'Python',
                   'type': 'interpreted',
                   'year': '1991'},
                  {'programming language': 'JAVA',
                   'type': 'compiled',
                   'year': '1995'},
                  {'programming language': 'С',
                   'type': 'compiled',
                   'year': '1972'}]
    # Табличное представление списка словарей
    print(tabulate(dicts_list, headers='keys'))


def tab4():
    dicts_list = [{'programming language': 'Python',
                   'type': 'interpreted',
                   'year': '1991'},
                  {'programming language': 'JAVA',
                   'type': 'compiled',
                   'year': '1995'},
                  {'programming language': 'С',
                   'type': 'compiled',
                   'year': '1972'}]
    # grid-формат
    print(tabulate(dicts_list, headers='keys', tablefmt="grid"))
    # markdown-формат
    print(tabulate(dicts_list, headers='keys', tablefmt="pipe"))
    # html-формат
    print(tabulate(dicts_list, headers='keys', tablefmt="html"))


def tab_html():
    dicts_list = [{'programming language': 'Python',
                   'type': 'interpreted',
                   'year': '1991'},
                  {'programming language': 'JAVA',
                   'type': 'compiled',
                   'year': '1995'},
                  {'programming language': 'C',
                   'type': 'compiled',
                   'year': '1972'}]
    with open('table.html', 'w') as f:
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Programming language</title>
        </head>
        <body>
            {tabulate(dicts_list, headers='keys', tablefmt="html")}
        </body>
        </html>
        """
        f.write(html)


def tab5():
    dicts_list = [{'programming language': 'Python',
                   'type': 'interpreted',
                   'year': '1991'},
                  {'programming language': 'JAVA',
                   'type': 'compiled',
                   'year': '1995'},
                  {'programming language': 'C',
                   'type': 'compiled',
                   'year': '1972'}]

    # Выравнивание по центру
    print(tabulate(dicts_list, headers='keys', tablefmt="pipe", stralign="center"))


if __name__ == "__main__":
    tab_html()
