import matplotlib.pyplot as plt
import numpy as np

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
        
        fig, ax1 = plt.subplots(figsize=(12,8))
        plt.title("Keyword Search Comparison in " + self.state)
        ax1.set_ylabel("Relative Popularity", color="blue")
        
        for keyword in self.keywords:
            ax1.plot(self.df.Date, self.df[keyword], "--", c="blue", label="Searches for " + keyword)
        
        ax1.tick_params(axis='y', labelcolor="blue")
        ax2 = ax1.twinx()
        ax2.set_ylabel("Coronavirus cases", color="red")
        ax2.plot(self.df.Date, self.df.Confirmed, c="red")
        ax2.tick_params(axis='y', labelcolor="red")
        ax1.legend()
        
        file_name = self.state + "_coronavirus_trend_impacts.png"
        plt.savefig(file_name)
