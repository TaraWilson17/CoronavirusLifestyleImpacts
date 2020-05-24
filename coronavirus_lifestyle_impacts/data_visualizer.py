import matplotlib.pyplot as plt
import numpy as np

class DataVisualizer:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def show(self):
        print("Rendering visualization...")
        self.draw_graph(self.data_frame)

    def draw_graph(self, data_frame):
        N = 50
        x = np.random.rand(N)
        y = np.random.rand(N)
        colors = np.random.rand(N)
        area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

        plt.scatter(x, y, s=area, c=colors, alpha=0.5)
        plt.savefig("test_image.png")
        plt.savefig("test_image.pdf")
