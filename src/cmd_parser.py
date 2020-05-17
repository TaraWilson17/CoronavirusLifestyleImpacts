import json

class CmdParser:
    def __init__(self):
        print("Taking inputs from command line...")
        self.args = None

    def parse(self):
        self.args = {"country": "USA", "state": "WA", "time": "2020-05-15"}
        print("Showing sample input:", self.args)

    def validate_inputs(self, inputs):
        pass
