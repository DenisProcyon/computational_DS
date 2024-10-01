# 7)
def total_registered_cases(covid_cases,country):
    for key, value in covid_cases.items():
        if country == key:
            return sum(value)
    else:
        return 'No such country registered'

covid={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
       'Italy': [6, 8, 1, 7]}
cases=total_registered_cases(covid,'Spain')
print(cases)


# 8)
def total_registered_cases_per_country(data: dict):
    return {k: sum(v) for k, v in data.items()}

print(total_registered_cases_per_country(data={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}))


# 9)

def country_with_most_cases(data: dict):
    return max(data, key=lambda i: sum(data[i]))

print(country_with_most_cases(data={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}))
