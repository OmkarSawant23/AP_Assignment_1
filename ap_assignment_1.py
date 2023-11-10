"""Importing pandas as pd and matplotlib as plt to reduce complexity of code."""

import pandas as pd
import matplotlib.pyplot as plt


def yaleuni_admission():
    """
    Create function yaluni_admissions.
    It will return the dataset of admissions in Yale University as dataframe.

    Returns
    -------
    yale : pandas dataframe
        It will reture data for yale admission.

    """

    # importing the csv file
    yale = pd.read_csv("YaleAdmits.csv")

    return yale


def yale_admission_graph(yale_admission):
    """
    Create another function called as yale_admission_Graph.
    It will return the line plot of Admissions in Yale from different
    parts of America as well as from forgien countires since year 1985
    till recent years. This function will make use of previous function
    Yale_Admission for reading data

    Parameters
    ----------
    yale_admission : pandas dataframe
        This is Yale admission data.

    Returns
    -------
    None.

    """

    # For plotting figure.
    plt.figure()

    # Producing line plots using matplotlib.
    plt.plot(yale_admission["Year Entered"],
             yale_admission["NewEngland"])
    plt.plot(yale_admission["Year Entered"],
             yale_admission["NewYorkState"])
    plt.plot(yale_admission["Year Entered"],
             yale_admission["EastofMississippi"])
    plt.plot(yale_admission["Year Entered"],
             yale_admission["WestofMississippi"])
    plt.plot(yale_admission["Year Entered"],
             yale_admission["U.S.Poss.Foreign"])

    # Setting limits for y-axis for better results.
    plt.ylim(50, 600)

    # Adding title for plot.
    plt.title("Yale Admissions")

    # Adding Lables for x-axis and y-axis.
    plt.xlabel("Year of Admission")
    plt.ylabel("Number of Students")

    # adding legend outside of graph.
    plt.legend(["NewEngland", "NewYorkState", "EastofMississippi",
                "WestofMississippi",  "U.S.Poss.Foreign"],
               loc="center left", bbox_to_anchor=(1, 0.5))

    # Saving the plot as png.
    plt.savefig("Line_Plot.png")

    # Displaying the plot.
    plt.show()


def top_revenue():
    """
    Create a new function top_revenue.
    for reading a different csv file which contains data.
    of top 1000 companies in america.This function will also create
    a sub dataframe top_company which later will be used for plotting bargraph.

    Returns
    -------
    top_num_company : pandas dataframe
        This top ten companies revenue data.

    """

    # importing the csv file as dataframe.
    company = pd.read_csv("fortune1000_2023.csv")

    # Creating a new dataframe consisting of required data.
    top_num_company = company.loc[:9, ['Company', 'Revenues_M']]

    return top_num_company


def top10_revenue_bargraph(top10_revenue):
    """
    Create another function to plot the bar graph named as \
    top10_revenue_bargraph.which will display revenue of top 10 companies \
    in million USD for year 2023.

    Parameters
    ----------
    top10_revenue : pandas dataframe
        This is revenue of top 10 companies.

    Returns
    -------
    None.

    """

    # Deciding figure size.
    plt.figure(figsize=(20, 15))

    # Producing bar plot using matplotlib.
    top10_revenue.plot.bar(x="Company", y="Revenues_M", rot=60,
                           title="Revenue of Top Ten Companies", align='edge')

    # Adding Lables for x-axis and y-axis.
    plt.xlabel("Name of Companies")
    plt.ylabel("Revenue in Millions (USD)")

    # saving figure as png.
    plt.savefig("Bar_Plot.png")

    # Displaying plot.
    plt.show()


def top10_revenue_change():
    """
    Create a new function top10_revenue_change for reading a csv file.
    It contains data of top 1000 companies in america.
    This function will also create a sub dataframe top_company_revenue \
    which later will be used for plotting piechart

    Returns
    -------
    top_all_company_revenue : pandas dataframe
        This is revenue percentage change for top 10 companies.

    """

    # Importing the csv file as dataframe.

    company_1 = pd.read_csv("fortune1000_2023.csv")

    # Refining original dataframe and saving it as sub dataframe.

    top_all_company_revenue = company_1.loc[:6, [
        'Company', 'RevenuePercentChange']]

    return top_all_company_revenue


def top10_revenue_change_plot(topk_company_revenue):
    """
    Create another function to plot the pie chart named as top10_revenue_change_plot.
    which will display revenue percentage change of top 10 companies in \
    million USD for year 2023.

    Parameters
    ----------
    topk_company_revenue : Panda data frame
        This is data of Revenue percentage change.

    Returns
    -------
    None.

    """

    # plotting pie chart using matplotlib.
    plt.pie(topk_company_revenue['RevenuePercentChange'],
            labels=topk_company_revenue['Company'], autopct='%1.0f%%')

    # Adding Title for pie chart
    plt.title('Revenue Percentage Change of Top Companies in Year 2023')

    # saving pie chart as jpg.
    plt.savefig('Piechart')

    # displaying plot.
    plt.show()


# Main Program.
Yale = yaleuni_admission()
yale_admission_graph(Yale)
top_company = top_revenue()
top10_revenue_bargraph(top_company)
top_company_revenue = top10_revenue_change()
top10_revenue_change_plot(top_company_revenue)
