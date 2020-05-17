class DataProcessor:
    def __init__(self, args, data_frames = []):
        self.args = args
        self.input_data_frames = data_frames
        self.agg_data_frame = None

    def run(self):
        print("Processing data...")
        self.validate_data_frame()
        self.aggregate_data_frames()

    def validate_data_frame(self, data_frame = None):
        pass

    def aggregate_data_frames(self, data_1 = None, data_2 = None, schema = None):
        pass

    # More data processing
