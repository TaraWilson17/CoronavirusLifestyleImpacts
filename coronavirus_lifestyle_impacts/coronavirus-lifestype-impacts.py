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
print("\n=========Sampling data========")
print(data_generator.covid_data.head(5))
print(data_generator.trend_data.head(5))

data_frames = [data_generator.covid_data, data_generator.trend_data]


data_processor = DataProcessor(cmd_parser.args, data_frames)
data_processor.run()
print("\nProcessed COVID Data columns\n", data_processor.clean_data_frame[0].columns)
print("\nProcessed GoogleTrends Data columns\n", data_processor.clean_data_frame[1].columns)
agg_data_frame = data_processor.agg_data_frame
agg_data_frame.to_csv('agg_data_frame.csv')
print("\nAggregated cleaned dataframe saved as agg_data_frame.csv\n")


data_visualizer = DataVisualizer(agg_data_frame)
data_visualizer.show()
