import csv
from project_template.settings.base import COUNTIES_CSV_PATH


class CsvCountiesSingleton:
    __instance = None
    __path = COUNTIES_CSV_PATH
    __cities = {}
    __counties = list()

    @staticmethod
    def get_instance():
        if CsvCountiesSingleton.__instance is None:
            CsvCountiesSingleton()
        return CsvCountiesSingleton.__instance

    def __init__(self):
        CsvCountiesSingleton.__instance = self
        with open(self.__path) as csvfile:
            reader = csv.DictReader(csvfile)
            headers = ["JUDET", "NUME"]
            for row in reader:
                self.__counties.append(row[headers[0]])

                if row[headers[0]] in self.__cities:
                    self.__cities[row[headers[0]]].append(row[headers[1]])
                else:
                    self.__cities[row[headers[0]]] = []
                    self.__cities[row[headers[0]]].append(row[headers[1]])

            self.__counties = list(set(self.__counties))
            self.__counties.sort()

    def get_sorted_counties(self):
        return self.__counties

    def get_cities_in_county(self, county):
        return self.__cities[county]
