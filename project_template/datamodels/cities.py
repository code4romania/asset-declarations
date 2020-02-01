from project_template.config.csv_counties_singleton import CsvCountiesSingleton


class Cities:
    @staticmethod
    def return_cities_from_county(county):
        return (
            CsvCountiesSingleton().get_instance().get_cities_in_county(county)
        )
