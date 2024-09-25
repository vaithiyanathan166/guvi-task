import requests

# Step 1: Fetch the Data
response = requests.get('https://restcountries.com/v3.1/all')
data = response.json()

# Step 2: Define the Classes
class Currency:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return f"Currency(name={self.name}, code={self.code})"

class Language:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Language(name={self.name})"

class Country:
    def __init__(self, name, capital, region, subregion, population, languages, currencies):
        self.name = name
        self.capital = capital
        self.region = region
        self.subregion = subregion
        self.population = population
        self.languages = [Language(lang) for lang in languages]
        self.currencies = [Currency(cur['name'], cur['code']) for cur in currencies]

    def __repr__(self):
        return (f"Country(name={self.name}, capital={self.capital}, region={self.region}, "
                f"subregion={self.subregion}, population={self.population}, "
                f"languages={self.languages}, currencies={self.currencies})")

# Step 3: Parse the Data
countries = []
for item in data:
    name = item.get('name', {}).get('common', 'Unknown')
    capital = item.get('capital', ['Unknown'])[0]
    region = item.get('region', 'Unknown')
    subregion = item.get('subregion', 'Unknown')
    population = item.get('population', 0)
    languages = list(item.get('languages', {}).values())
    currencies = [{'name': cur['name'], 'code': cur.get('code', 'Unknown')} for cur in item.get('currencies', {}).values()]
    
    country = Country(name, capital, region, subregion, population, languages, currencies)
    countries.append(country)

# Step 4: Implement Methods (Example usage)
def print_countries(countries):
    for country in countries:
        print(country)

# Print out the list of countries
print_countries(countries)


import requests

# Define the Classes
class Currency:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return f"Currency(name={self.name}, code={self.code})"

class Language:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Language(name={self.name})"

class Country:
    def __init__(self, url):
        self.url = url
        self.countries = []
        self.fetch_data()

    def fetch_data(self):
        response = requests.get(self.url)
        data = response.json()
        
        for item in data:
            name = item.get('name', {}).get('common', 'Unknown')
            capital = item.get('capital', ['Unknown'])[0]
            region = item.get('region', 'Unknown')
            subregion = item.get('subregion', 'Unknown')
            population = item.get('population', 0)
            languages = list(item.get('languages', {}).values())
            currencies = [{'name': cur['name'], 'code': cur.get('code', 'Unknown')} for cur in item.get('currencies', {}).values()]
            
            country = {
                'name': name,
                'capital': capital,
                'region': region,
                'subregion': subregion,
                'population': population,
                'languages': [Language(lang) for lang in languages],
                'currencies': [Currency(cur['name'], cur['code']) for cur in currencies]
            }
            self.countries.append(country)

    def print_countries(self):
        for country in self.countries:
            print(f"Country(name={country['name']}, capital={country['capital']}, region={country['region']}, "
                  f"subregion={country['subregion']}, population={country['population']}, "
                  f"languages={country['languages']}, currencies={country['currencies']})")

# Usage
url = 'https://restcountries.com/v3.1/all'
country_data = Country(url)
country_data.print_countries()

import requests

class Country:
    def __init__(self):
        self.url = 'https://restcountries.com/v3.1/all'
        self.data = self.fetch_data()

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch data. Status code {response.status_code}")
            return []

    def __repr__(self):
        return f"Country(url={self.url})"

# Usage
country_instance = Country()
print(country_instance.data)  # This will print the fetched JSON data

import requests

def fetch_country_data(url='https://restcountries.com/v3.1/all'):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data. Status code {response.status_code}")
        return []

# Usage
data = fetch_country_data()
print(data)  # This will print the fetched JSON data

import requests

class DataFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Check if the request was successful
            data = response.json()
            return data
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

class CountryInfo:
    def __init__(self, data):
        self.data = data

    def display_country_currency_info(self):
        if not self.data:
            print("No data available.")
            return
        
        for item in self.data:
            country_name = item.get('name', {}).get('common', 'Unknown')
            currencies = item.get('currencies', {})
            currency_info = []
            
            for currency_code, currency_details in currencies.items():
                currency_name = currency_details.get('name', 'Unknown')
                currency_symbol = currency_details.get('symbol', 'None')
                currency_info.append(f"{currency_name} ({currency_symbol})")
            
            currency_info_str = ', '.join(currency_info) if currency_info else 'No currencies'
            
            print(f"Country: {country_name}")
            print(f"  Currencies: {currency_info_str}")

# Usage
url = 'https://restcountries.com/v3.1/all'
fetcher = DataFetcher(url)
data = fetcher.fetch_data()

info = CountryInfo(data)
info.display_country_currency_info()

import requests

class DataFetcher:
    def __init__(self, url):
        self.url = url
        self.countries_data = []

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Check if the request was successful
            self.countries_data = response.json()
        except requests.RequestException as e:
            print(f"An error occurred while fetching data: {e}")
            self.countries_data = []

    def get_countries_with_dollar(self):
        countries_with_dollar = []

        for country in self.countries_data:
            # Check if country has any currency with 'Dollar' in the name
            currencies = country.get('currencies', {})
            for code, currency in currencies.items():
                if 'Dollar' in currency.get('name', ''):
                    countries_with_dollar.append(country.get('name', {}).get('common', 'Unknown'))

        return countries_with_dollar

    def display_countries_with_dollar(self):
        countries = self.get_countries_with_dollar()
        if countries:
            print("Countries that use the Dollar as currency:")
            for country in countries:
                print(country)
        else:
            print("No countries with Dollar as currency found.")

# Usage
url = 'https://restcountries.com/v3.1/all'
fetcher = DataFetcher(url)

# Fetch data from the URL
fetcher.fetch_data()

# Display countries that use the Dollar as currency
fetcher.display_countries_with_dollar()

import requests

class DataFetcher:
    def __init__(self, url):
        self.url = url
        self.countries_data = []

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Check if the request was successful
            self.countries_data = response.json()
        except requests.RequestException as e:
            print(f"An error occurred while fetching data: {e}")
            self.countries_data = []

    def get_countries_with_euro(self):
        countries_with_euro = []

        for country in self.countries_data:
            # Check if country has any currency with 'Euro' in the name
            currencies = country.get('currencies', {})
            for code, currency in currencies.items():
                if 'Euro' in currency.get('name', ''):
                    countries_with_euro.append(country.get('name', {}).get('common', 'Unknown'))

        return countries_with_euro

    def display_countries_with_euro(self):
        countries = self.get_countries_with_euro()
        if countries:
            print("Countries that use the Euro as currency:")
            for country in countries:
                print(country)
        else:
            print("No countries with Euro as currency found.")

# Usage
url = 'https://restcountries.com/v3.1/all'
fetcher = DataFetcher(url)

# Fetch data from the URL
fetcher.fetch_data()

# Display countries that use the Euro as currency
fetcher.display_countries_with_euro()

import requests

class BreweryFetcher:
    def __init__(self):
        self.base_url = "https://api.openbrewerydb.org/breweries"

    def get_breweries_by_state(self, state):
        try:
            response = requests.get(self.base_url, params={"by_state": state})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching breweries in {state}: {e}")
            return []

    def list_breweries(self, states):
        for state in states:
            breweries = self.get_breweries_by_state(state)
            if breweries:
                print(f"Breweries in {state}:")
                for brewery in breweries:
                    print(brewery['name'])
                print("\n")  # Separate output for each state

# Usage
fetcher = BreweryFetcher()
states = ["Alaska", "Maine", "New York"]
fetcher.list_breweries(states)


Breweries in Alaska:
Anchorage Brewing Company
Bleeding Heart Brewery
Devil's Club Brewing Company

import requests


# Using Classes and Methods to perform api testing
class MyJSON:
    def __init__(self, url):
        self.url = url


    # fetch the api status code
    def api_status_code(self):
        # response variable to store the api data
        response = requests.get(self.url)
        return response.status_code
   
    # fetch the entire api data
    def fetch_api_data(self):
        if self.api_status_code() == 200:
            return requests.get(self.url).json()
        else:
            return "ERROR - 404"
       
    # fetch the header data or meta information
    def fetch_headers(self):
        if self.api_status_code() == 200:
            response = requests.get(self.url)
            return response.headers
        else:
            return "ERROR - 404"


    # fetch data based on id
    def fetch_data_by_id(self, id):
        if self.api_status_code() == 200:
            # convert int to string
            id = str(id)
            for data in self.fetch_api_data():
                if data['id'] == id:
                    print("FOOD NAME" , data['food_name'])
                    print("COUNTRY", data['country'])
                    print("CREATED", data['created_at'])  


    def test_api_data_by_id(self, id):
        if self.api_status_code() == 200:
            id = str(id)
            for data in self.fetch_api_data():
                if data['id'] == id:
                    if data['food_name'] == "Sweet":
                        print("Success, Food Name Matched")
                    else:
                        print("Wrong Food Name")
                else:
                    "No Data ID"


    def insert_data(self, data):
        if self.api_status_code() == 200:
            response = requests.post(self.url, json=data)
            if response:
                return True
            else:
                return False


    def count_total_foods(self, country):
        if self.api_status_code() == 200:
            counter = 0
            for data in self.fetch_api_data():
                if data['country'] == country:
                    counter += 1
            return counter
        else:
            return "ERROR 404"
                   




json_object = MyJSON("https://62513902977373573f4567fb.mockapi.io/pizza/pizza_names")
data = {
"food_name": "Sweet",
"country": "India"
}
# print(json_object.api_status_code())
# print(json_object.fetch_api_data())
# print(json_object.fetch_headers())
# json_object.fetch_data_by_id(26)
# json_object.test_api_data_by_id(26)
# json_object.insert_data(data)
# json_object.test_api_data_by_id(100)
# print(json_object.count_total_foods("china"))

