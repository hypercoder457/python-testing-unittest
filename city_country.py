def form_city_country_string(city: str, country: str, population: str = '') -> str:
    if population:
        return f"{city}, {country}, population {population}"
    else:
        return f"{city}, {country}"
