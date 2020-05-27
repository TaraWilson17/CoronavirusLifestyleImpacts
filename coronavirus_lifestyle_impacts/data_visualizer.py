import matplotlib.pyplot as plt
import numpy as np

class DataVisualizer:
    def __init__(self, state, keywords, all_data):
        self.state = state
        self.keywords = keywords
        self.all_data = all_data

    def show(self):
        print("Rendering visualization...")
        self.draw_graph()

    def draw_graph(self):
        
        N = 50
        x = np.random.rand(N)
        y = np.random.rand(N)
        colors = np.random.rand(N)
        area = (30 * np.random.rand(N))**2 

        plt.scatter(x, y, s=area, c=colors, alpha=0.5)
        plt.savefig("test_image.png")
