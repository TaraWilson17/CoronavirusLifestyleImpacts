#!/usr/bin/env python3

from cmd_parser import CmdParser
from data_generator import DataGenerator
from data_processor import DataProcessor
from data_visualizer import DataVisualizer

# This is the entry point of our tool

cmd_parser = CmdParser()
cmd_parser.parse()

data_generator = DataGenerator(cmd_parser.args)
data_generator.run()

data_frames = [data_generator.data_1, data_generator.data_2]
data_processor = DataProcessor(cmd_parser.args, data_frames)
data_processor.run()
agg_data_frame = data_processor.agg_data_frame

data_visualizer = DataVisualizer(agg_data_frame)
data_visualizer.show()
