import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

class DataVisualizer:
    def __init__(self, state, keywords, all_data):
        self.state = state
        self.keywords = keywords
        self.df = all_data

    def show(self):
        print("Rendering visualization...")
        self.draw_graph()

    def draw_graph(self):
        #'Date', 'Confirmed', 'ConfirmedChange', 'Deaths', 'DeathsChange', 'Recovered', 'RecoveredChange', 'Country', 'State', 'Bars near me', 'Home workouts']
        
        fig, ax = plt.subplots(figsize=(12,8))
        plt.title("Keyword Search Comparison in " + self.state)
        ax.set_ylabel("Relative Popularity")
        
        for keyword in self.keywords:
            ax.plot(self.df.Date, self.df[keyword], label="Searches for " + keyword)
        
        ax.tick_params(axis='y')
        
        date_first_case = min(self.df[self.df.Confirmed >= 1]["Date"])
        ax.axvline(date_first_case, c="black")
        plt.text(x=date_first_case,y=10, s="First case")
        
        date_100_cases = min(self.df[self.df.Confirmed >= 100]["Date"])
        ax.axvline(date_100_cases, c="black")
        plt.text(x=date_100_cases,y=30, s="100\ncases")
        
        date_1000_cases = min(self.df[self.df.Confirmed >= 1000]["Date"])
        ax.axvline(date_1000_cases, c="black")
        plt.text(x=date_1000_cases,y=50, s="1,000\ncases")
        
        date_10000_cases = min(self.df[self.df.Confirmed >= 10000]["Date"])
        ax.axvline(date_10000_cases, c="black")
        plt.text(x=date_10000_cases,y=70, s="10,000\ncases")
        
        ax.legend()
        
        file_name = self.state + "_coronavirus_trend_impacts.png"
        plt.savefig(file_name)
