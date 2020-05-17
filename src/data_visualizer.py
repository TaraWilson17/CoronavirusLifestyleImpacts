class DataVisualizer:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def show(self):
        print("Rendering visualization...")
        self.draw_graph(self.data_frame)

    def draw_graph(self, data_frame):
        pass
