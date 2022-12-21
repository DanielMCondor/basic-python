import mechanicalsoup
import json

browser = mechanicalsoup.StatefulBrowser(user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36')
browser.open("https://eldni.com/pe/buscar-por-nombres")

browser.select_form("#buscar-por-nombres")
browser["nombres"] = "Miguel"
browser["apellido_p"] = "Lima"
browser["apellido_m"] = ""
browser.submit_selected()
table = browser.page.find('table')
if not table is None:
    h, [_, *d] = [i.text for i in table.tr.find_all('th')], [[i.text for i in b.find_all('td')] for b in table.find_all('tr')]
    table_dict = [dict(zip(h, i)) for i in d]
    table_json = json.dumps(table_dict)
    print(table_json)
    print(type(table_json))
else:
    print('No se ha encontrado el nombre o los nombres con esa referencia')

