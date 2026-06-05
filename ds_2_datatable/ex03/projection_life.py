from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """Plot life expectancy versus GDP per capita for the year 1900.

    Loads two CSV datasets — income per person (PPP-adjusted GDP per
    capita) and life expectancy — merges them on the "country" index
    for the year 1900, and displays a scatter plot with a logarithmic
    x-axis. GDP values are formatted in thousands (e.g., "10k").

    Returns:
        None. Exits early if either dataset fails to load.

    See Also:
        load: Loads and returns a CSV dataset as a DataFrame.
    """    
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if income is None:
        return
    life = load("life_expectancy_years.csv")
    if life is None:
        return
    income = income.set_index("country")
    life = life.set_index("country")
    year = "1900"
    income_year = income[year].dropna().rename("dolar")
    life_year = life[year].dropna().rename("life_exp")
    data = pd.merge(income_year, life_year, on="country", how="inner")
    plt.scatter(data.dolar, data.life_exp)
    plt.title(f"Year {year}")
    plt.ylabel("Life Expectancy")
    plt.xlabel("Gross domestic product")
    plt.xscale("log")
    plt.gca().xaxis.set_major_formatter(
        plt.FuncFormatter(lambda v, p: f"{v/1_000:.0f}k")
        )
    plt.show()


if __name__ == "__main__":
    main()
