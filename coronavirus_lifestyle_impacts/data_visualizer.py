"""
Purpose:
The following module is the DataVisualizer. It is responsible for
generating a data visualization using the coronavirus and pytrends
data resulting from the DataProcessor class.

Date: 5/31/2020

Author: Tara Wilson
"""

import os
import matplotlib.pyplot as plt

class DataVisualizer:
    """
    The DataVisualizer class is used to create a visualization of the
    data aggregated by the Data Processor. It has the following attributes:

    state: the state for which the Coronavirus and Google Trends data is referencing
    keywords: the keyword(s) for which the the Google Trends data is for
    all_data: a dataframe containing all of the Coronavirus and Google Trends data
        for the specified state and keywords
    """
    OUTPUT_DIR = "outputs/"

    def __init__(self, state, keywords, all_data):
        self.state = state
        self.keywords = keywords
        self.data = all_data

    def show(self):
        """
        Calls for the visualization to be created.
        """
        self.draw_graph()

    def draw_graph(self):
        """
        Creates a png containing a visualization of the data. Marks Google
        Trend relative popularity index on the y-axis and date on the x-axis.
        Counts of Coronavirus cases are indicated on the trend lines. The figure
        is saved in the coronavirus_lifestyle_impacts folder with the state name
        in the image title.
        """
        _, axis = plt.subplots(figsize=(12, 8))
        plt.title("Keyword Search Comparison in " + self.state)
        axis.set_ylabel("Relative Popularity")
        axis.tick_params(axis='y')

        for keyword in self.keywords:
            axis.plot(self.data["Date"], self.data[keyword], "-", label="Searches for " + keyword)

        colors = ["lightgray", "silver", "darkgray", "gray", "dimgray", "black"]

        case = 1
        color_index = 0
        y_pos = 10
        size = 8
        while case <= max(self.data.Confirmed):
            date_cases_reached = min(self.data[self.data.Confirmed >= case]["Date"])
            for i, keyword in enumerate(self.keywords):
                keyword_value = self.data[self.data["Date"] == date_cases_reached][keyword]
                if i == 0:
                    axis.plot(date_cases_reached, keyword_value, marker="X", markersize=size,
                              c=colors[color_index], label="Case #" + str(case))
                else:
                    axis.plot(date_cases_reached, keyword_value, marker="X", markersize=size,
                              c=colors[color_index], label="_nolegend_")
            y_pos += 20
            color_index += 1
            case *= 10
            size += 2

        axis.legend()

        curr_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
        output_dir = curr_dir + "/" + self.OUTPUT_DIR
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        plt.savefig(output_dir + self.state + "_coronavirus_trend_impacts.png")
