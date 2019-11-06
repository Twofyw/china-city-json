import json
from pprint import pprint


def get_cities_from_province_code(province_code, cities, districts):
    province = cities[province_code]
    # print(province)
    province_name = province[0]['province']
    children = []
    for city in province:
        name = city['name']
        if name == '市辖区':  # use districts
            children += [{'name': o['name']} for o in districts[city['id']]]
        else:
            children.append({'name': name})

    return {'name': province_name, 'children': children}


def main():
    with open('city.json') as f:
        cities = json.load(f)

    with open('county.json') as f:
        districts = json.load(f)

    result = [get_cities_from_province_code(province_code, cities, districts) for province_code in cities]
    with open('cities_ywx_format.json', 'w') as f:
        json.dump(result, f, ensure_ascii=False)
    pprint(result)


if __name__ == '__main__':
    main()
