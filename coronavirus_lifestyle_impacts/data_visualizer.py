import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from datetime import timedelta
from colour import Color

class DataVisualizer:
    def __init__(self, state, keywords, all_data):
        self.state = state
        self.keywords = keywords
        self.df = all_data

    def show(self):
        print("Rendering visualization...")
        self.draw_graph()

    def draw_graph(self):
        
        fig, ax = plt.subplots(figsize=(12,8))
        plt.title("Keyword Search Comparison in " + self.state)
        ax.set_ylabel("Relative Popularity")
        ax.tick_params(axis='y')

        for keyword in self.keywords:
            ax.plot(self.df.Date, self.df[keyword], "-", label="Searches for " + keyword)

        colors = ["lightgray", "silver", "darkgray", "gray", "dimgray", "black"]

        case = 1
        color_index = 0
        y_pos = 10
        while case <= max(self.df.Confirmed):
            date_cases_reached = min(self.df[self.df.Confirmed >= case]["Date"])
            ax.axvline(date_cases_reached, c=colors[color_index], linewidth=.75)
            plt.text(x=date_cases_reached + timedelta(days=3), y=y_pos, s="Case " + str(case), backgroundcolor="white")
            y_pos += 20
            color_index += 1
            case *= 10

        ax.legend()

        file_name = self.state + "_coronavirus_trend_impacts.png"
        plt.savefig(file_name)
