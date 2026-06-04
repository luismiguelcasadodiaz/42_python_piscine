from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Load population data and plot projections for Belgium and France.

    Loads the "population_total.csv" dataset via ``load``, filters columns
    to the year range 1800–2050, parses abbreviated population values
    (e.g., "10.5M", "300K") into integers, and displays a comparative
    line chart of both countries using matplotlib.

    Returns:
        None. Exits early if the dataset fails to load.

    See Also:
        load: Loads and indexes the CSV dataset.
    """
    # Define the year range to filter
    yr_init = "1800"
    yr_end = "2050"
    data = load("population_total.csv")
    if data is None:
        return
    cols = ["country"] + list(
        data.columns[
            data.columns.get_loc(yr_init):data.columns.get_loc(yr_end)+1
            ]
        )
    data_plot = data[cols]
    data_plot = data_plot.set_index("country")

    country_a = "Belgium"
    country_b = "Spain"

    data_country_a = data_plot.loc[country_a].apply(
        lambda x: int(
            float(x[:-1]) * (
                1_000_000_000 if x[-1] == "B"
                else 1_000_000 if x[-1] == "M"
                else 1_000 if x[-1] == "K"
                else 1
                )
            if x[-1] in ["K", "M", "B"] else int(x)
            )
        )
    data_country_b = data_plot.loc[country_b].apply(
        lambda x: int(
            float(x[:-1]) * (
                1_000_000_000 if x[-1] == "B"
                else 1_000_000 if x[-1] == "M"
                else 1_000 if x[-1] == "K"
                else 1
                )
            if x[-1] in ["K", "M", "B"] else int(x)
            )
        )

    plt.plot(data_country_a.index, data_country_a.values,
             label=country_a, color="blue", linestyle="--")
    plt.plot(data_country_b.index, data_country_b.values,
             label=country_b, color="green", linestyle=":")
    plt.title("Population Projections")
    plt.ylabel("Population")
    plt.xlabel("Year")
    plt.legend(loc="lower right", fontsize=8, frameon=False)
    plt.gca().yaxis.set_major_formatter(
        plt.FuncFormatter(lambda v, p: f"{v/1e6:.0f}M"))
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(nbins=6))
    plt.show()


if __name__ == "__main__":
    main()
