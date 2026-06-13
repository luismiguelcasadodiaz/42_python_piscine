from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Load life expectancy data and plot projections for Spain.

    Loads the "life_expectancy_years.csv" dataset via ``load``, extracts
    the row for Spain, converts the year index to integers, and displays
    a line chart of life expectancy over time using matplotlib.

    See Also:
        load: Loads and indexes the CSV dataset by country.
    """
    data = load("life_expectancy_years.csv")
    if data is None:
        return
    country = "Spain"
    data_plot = data.loc[country]
    data_plot.index = data_plot.index.astype(int)

    plt.plot(data_plot)
    plt.title(f"{country} Life expectancy Projections")
    plt.ylabel("Life Expectancy")
    plt.xlabel("Vear")
    plt.show()


if __name__ == "__main__":
    main()
