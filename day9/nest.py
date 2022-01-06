# Nesting Lists and dictionaries
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Frankfurt", "Hamburg"],
}

# Nest a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Frankfurt", "Hamburg"], "total_visits": 5},
}

# Nest dictionary in a list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Frankfurt", "Hamburg"],
        "total_visits": 5
    },
]
