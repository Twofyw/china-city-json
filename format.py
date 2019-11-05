import json
import sys


def main():
    with open('city.json') as f:
        cities = json.load(f)

    result = []
    for province_code in cities:
        province = cities[province_code]
        print(province)
        province_name = province[0]['province']
        cities_in_province = [o['name'] for o in province]
        print(cities_in_province)
        result.append({'name': province_name, 'children': ['' ]})


if __name__ == '__main__':
    main()
