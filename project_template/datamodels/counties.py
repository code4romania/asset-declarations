from project_template.config.csv_counties_singleton import CsvCountiesSingleton


class Counties:
    @staticmethod
    def return_counties():
        counties = CsvCountiesSingleton().get_instance().get_sorted_counties()
        counties_as_tuplets = list()
        for county in counties:
            counties_as_tuplets.append((county, county))

        return counties_as_tuplets
