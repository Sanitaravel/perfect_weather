import requests
from bs4 import BeautifulSoup
import time

site = 'https://ru.wikipedia.org'
cities = dict()


def set_cities():
    response = requests.get(f'{site}/wiki/Список_городов_России')
    table = BeautifulSoup(response.text, "html.parser").find('table')
    tr = table.findAll('tr')
    td = []
    for i in range(2, len(tr)):
        td.append(tr[i].findAll('td'))
    a = []
    for i in td:
        a.append(i[2].find('a'))
    for i in a:
        cities[i.get('title')] = [i.get('href')]


def set_temperatures(key, value):
    response = requests.get(f'{site}{value}')
    html = BeautifulSoup(response.text, "html.parser")
    table = html.find_all('table', class_='wikitable')
    if len(table) == 0:
        cities[key].append(None)
        return
    find = False
    for i in table:
        if len(i.find_all('tr')) > 0:
            if len(i.find_all('tr')[0].find_all('th')) > 0:
                if len(i.find_all('tr')[0].find('th').get_text().split()) > 0:
                    if i.find_all('tr')[0].find('th').get_text().split()[0] == "Климат":
                        table = i
                        find = True
                        break
    if not find:
        cities[key].append(None)
        return
    tr = table.find_all("tr")[2:]
    th = None
    find = False
    for i in tr:
        if len(i.find_all("th")) > 0:
            if i.find_all("th")[0].get_text().split()[0] == "Средняя" and \
               i.find_all("th")[0].get_text().split()[1] == "температура,":
                th = i.find_all("th")[1:-1]
                find = True
    if not find:
        cities[key].append(None)
        return
    temperatures = []
    for i in th:
        temperatures.append(float(i.get_text().replace(",", ".").replace("−", "-")))
    cities[key].append(temperatures)


def main():
    set_cities()
    count = 0
    for key, value in cities.items():
        set_temperatures(key, value[0])
    mean_temperatures = [0] * 12
    for key, value in cities.items():
        if value[1] is not None:
            if len(value[1]) == 12:
                count += 1
                for i in range(12):
                    try:
                        mean_temperatures[i] += value[1][i]
                    except IndexError:
                        print(f"{key} {value}")
    for i in range(12):
        mean_temperatures[i] /= count

    for i in range(12):
        delta = 0.0
        city = None
        for key, value in cities.items():
            if value[1] is not None:
                if len(value[1]) == 12:
                    if value[1][i]-mean_temperatures[i] > delta:
                        delta = value[1][i]-mean_temperatures[i]
                        city = key
        if i == 0:
            print(
                f"Самый жаркий город в России в январе относительно среднего города - {city}. Он теплее на {delta} °C"
            )
        elif i == 1:
            print(
                f"Самый жаркий город в России в феврале относительно среднего города - {city}. Он теплее на {delta} °C"
            )
        elif i == 2:
            print(
                f"Самый жаркий город в России в марте относительно среднего города - {city}. Он теплее на {delta} °C"
            )
        elif i == 3:
            print(
                f"Самый жаркий город в России в апреле относительно среднего города - {city}. Он теплее на {delta} °C"
            )
        elif i == 4:
            print(
                f"Самый жаркий город в России в мае относительно среднего города - {city}. Он теплее на {delta} °C"
            )
        elif i == 5:
            print(
                f"Самый жаркий город в России в июне относительно среднего города - {city}. Он теплее на {delta} °C"
            )
        elif i == 6:
            print(
                f"Самый жаркий город в России в июле относительно среднего города - {city}. Он теплее на {delta} °C"
            )
        elif i == 7:
            print(
                f"Самый жаркий город в России в августе относительно среднего города - {city}. Он теплее на {delta} °C"
            )
        elif i == 8:
            print(
                f"Самый жаркий город в России в сентябре относительно среднего города - {city}. Он теплее на {delta} °C"
            )
        elif i == 9:
            print(
                f"Самый жаркий город в России в октябре относительно среднего города - {city}. Он теплее на {delta} °C"
            )
        elif i == 10:
            print(
                f"Самый жаркий город в России в ноябре относительно среднего города - {city}. Он теплее на {delta} °C"
            )
        else:
            print(
                f"Самый жаркий город в России в декабре относительно среднего города - {city}. Он теплее на {delta} °C"
            )

    for i in range(12):
        delta = 0.0
        city = None
        for key, value in cities.items():
            if value[1] is not None:
                if len(value[1]) == 12:
                    if mean_temperatures[i]-value[1][i] > delta:
                        delta = mean_temperatures[i]-value[1][i]
                        city = key
        if i == 0:
            print(
                f"Самый холодный город в России в январе относительно среднего города - {city}. Он холоднее на {delta} °C"
            )
        elif i == 1:
            print(
                f"Самый холодный город в России в феврале относительно среднего города - {city}. Он холоднее на {delta} °C"
            )
        elif i == 2:
            print(
                f"Самый холодный город в России в марте относительно среднего города - {city}. Он холоднее на {delta} °C"
            )
        elif i == 3:
            print(
                f"Самый холодный город в России в апреле относительно среднего города - {city}. Он холоднее на {delta} °C"
            )
        elif i == 4:
            print(
                f"Самый холодный город в России в мае относительно среднего города - {city}. Он холоднее на {delta} °C"
            )
        elif i == 5:
            print(
                f"Самый холодный город в России в июне относительно среднего города - {city}. Он холоднее на {delta} °C"
            )
        elif i == 6:
            print(
                f"Самый холодный город в России в июле относительно среднего города - {city}. Он холоднее на {delta} °C"
            )
        elif i == 7:
            print(
                f"Самый холодный город в России в августе относительно среднего города - {city}. Он холоднее на {delta} °C"
            )
        elif i == 8:
            print(
                f"Самый холодный город в России в сентябре относительно среднего города - {city}. Он холоднее на {delta} °C"
            )
        elif i == 9:
            print(
                f"Самый холодный город в России в октябре относительно среднего города - {city}. Он холоднее на {delta} °C"
            )
        elif i == 10:
            print(
                f"Самый холодный город в России в ноябре относительно среднего города - {city}. Он холоднее на {delta} °C"
            )
        else:
            print(
                f"Самый холодный город в России в декабре относительно среднего города - {city}. Он холоднее на {delta} °C"
            )

    for i in range(12):
        delta = 10000000.0
        city = None
        for key, value in cities.items():
            if value[1] is not None:
                if len(value[1]) == 12:
                    if abs(mean_temperatures[i]-value[1][i]) < delta:
                        delta = value[1][i]-mean_temperatures[i]
                        city = key
        if i == 0:
            print(
                f"Самый стандартный город в России в январе относительно среднего города - {city}."
            )
        elif i == 1:
            print(
                f"Самый стандартный город в России в феврале относительно среднего города - {city}."
            )
        elif i == 2:
            print(
                f"Самый стандартный город в России в марте относительно среднего города - {city}."
            )
        elif i == 3:
            print(
                f"Самый стандартный город в России в апреле относительно среднего города - {city}."
            )
        elif i == 4:
            print(
                f"Самый стандартный город в России в мае относительно среднего города - {city}."
            )
        elif i == 5:
            print(
                f"Самый стандартный город в России в июне относительно среднего города - {city}."
            )
        elif i == 6:
            print(
                f"Самый стандартный город в России в июле относительно среднего города - {city}."
            )
        elif i == 7:
            print(
                f"Самый стандартный город в России в августе относительно среднего города - {city}."
            )
        elif i == 8:
            print(
                f"Самый стандартный город в России в сентябре относительно среднего города - {city}."
            )
        elif i == 9:
            print(
                f"Самый стандартный город в России в октябре относительно среднего города - {city}."
            )
        elif i == 10:
            print(
                f"Самый стандартный город в России в ноябре относительно среднего города - {city}."
            )
        else:
            print(
                f"Самый стандартный город в России в декабре относительно среднего города - {city}."
            )


if __name__ == '__main__':
    main()
