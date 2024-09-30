import pandas as pd
from pathlib import Path

def get_average_rate(data: pd.DataFrame, each_country_rate: bool, countries: list[str] = None,):
    """
    if each_conutry_rate is True will print death rate for each country in a group 
    
    if countries var is None, will calculate for the whole dataframe
    """
    if countries is not None:
        data = data[data["Country"].isin(countries)]

    rates = []
    for i in range(len(data)):
        # check if we can use this value in calculations
        confirmed = data["Confirmed"].iloc[i]
        country = data["Country"].iloc[i]
        if pd.isna(confirmed) or confirmed == 0:
            print(f'{data["Country"].iloc[i]} has no confirmed data')
            continue

        # append to list to calculate avg. after
        rates.append(data["Deaths"].iloc[i] / confirmed)

        if each_country_rate:
            print(f'{country} has a death rate to confirmed of {round(data["Deaths"].iloc[i] / confirmed, 3)}% (rounded)')

    # in case len is zero
    if len(rates) > 0:
        return sum(rates) / len(rates)

def get_high_active_cases_country(data: pd.DataFrame, active_cases: int):
    # returns all data rows with conutry column of each row larger than passed number
    return data[data["Active"] > active_cases]["Country"].tolist()

def get_data(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def main():
    # getting data with pathlib obj. var. passed
    path = Path(__file__).parent / "data/covid.csv"
    data = get_data(path)

    active_cases = [500, 1000, 5000]
    
    # iterate through each option of active cases
    for active_cases_limit in active_cases:
        # get countries with respective active cases number
        countries = get_high_active_cases_country(data=data, active_cases=active_cases_limit)
        
        # get avg. death rate for the whole group
        rate = get_average_rate(data=data, each_country_rate=False, countries=countries)

        print(f'For a group of {len(countries)} countries with active cases of more than {active_cases_limit} the average death / confirmed rate is {round(rate, 3)}% (rounded)')

        print(f'Countries - {countries}\n')

if __name__ == "__main__":
    main()