import requests
import csv
import time
import os
import argparse
import json


class AlternativeCountryParser:
    def __init__(self, cache_dir="cache"):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    def get_country_info(self, country_name):
        cache_file = os.path.join(self.cache_dir, f"{country_name.replace(' ', '_')}.json")

        if os.path.exists(cache_file):
            print(f"  Используется кэш для {country_name}")
            with open(cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)

        try:
            url = f"https://restcountries.com/v3.1/name/{country_name}"
            print(f"  Запрос к API: {url}")
            response = self.session.get(url)
            response.raise_for_status()

            data = response.json()

            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            return data
        except requests.RequestException as e:
            print(f"  Ошибка API: {e}")
            return None

    def parse_country_data(self, api_data, country_name):
        if not api_data:
            return None

        try:
            country_info = api_data[0]

            capital = country_info.get('capital', ['Not found'])[0]
            area = str(country_info.get('area', 'Not found'))
            population = str(country_info.get('population', 'Not found'))

            return {
                'country': country_name,
                'capital': capital,
                'area': area,
                'population': population
            }
        except Exception as e:
            print(f"  Ошибка обработки данных: {e}")
            return None

    def process_countries(self, input_file, output_file):
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                countries = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Файл {input_file} не найден")
            return

        results = []

        for i, country in enumerate(countries):
            print(f"Обработка {i + 1}/{len(countries)}: {country}")

            if i > 0:
                time.sleep(0.5)

            api_data = self.get_country_info(country)
            country_data = self.parse_country_data(api_data, country)

            if country_data:
                results.append(country_data)
                print(
                    f"  ✓ Данные: {country_data['capital']}, {country_data['area']} km², {country_data['population']}")
            else:
                print(f"  ✗ Данные не найдены")

        self.save_to_csv(results, output_file)
        print(f"\nРезультаты сохранены в {output_file}")

    def save_to_csv(self, data, output_file):
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['country', 'capital', 'area', 'population'])
            writer.writeheader()
            writer.writerows(data)


def main():
    parser = argparse.ArgumentParser(description='Альтернативный парсинг данных о странах')
    parser.add_argument('--input', '-i', default='countries.txt', help='Входной файл со странами')
    parser.add_argument('--output', '-o', default='countries_data.csv', help='Выходной CSV файл')

    args = parser.parse_args()

    parser = AlternativeCountryParser()
    parser.process_countries(args.input, args.output)


if __name__ == "__main__":
    main()