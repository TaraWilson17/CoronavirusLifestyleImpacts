class DataGenerator:
    def __init__(self, args):
        self.args = args
        self.data_1 = None
        self.data_2 = None

    def run(self):
        print("Generating data...")
        self.data_1 = self.fetch_data_1(self.args)
        self.data_2 = self.fetch_data_2(self.args)

    def fetch_data_1(self, args):
        """
        Used to fetch from data source 1
        """
        #self.build_request_1(args)
        return "My fetched data"

    def fetch_data_2(self, args):
        """
        Used to fetch from data source 2
        """
        #self.build_request_2(args)
        pass

    # Helpers
    def build_request_1(self, args):
        pass

    def build_request_2(self, args):
        pass
