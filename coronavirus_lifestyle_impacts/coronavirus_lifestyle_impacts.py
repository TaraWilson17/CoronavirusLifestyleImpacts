"""
This file runs the Coronavirus Lifestyle Impacts project. It takes in user
input through the command line by leveraging the CmdParser class to abstract
the state name and keywords that the project is being run for. The file then
goes through the three steps of the project: data generating, data processing
and data visualizing. There are seperate classes for each of these steps imported
from other files. This file prints out statements along the way as the project
progresses as well as prints the paths to where the output visualization
and aggregated data are saved.
"""

import sys
import os
from cmd_parser import CmdParser
from data_generator import DataGenerator
from data_processor import DataProcessor
from data_visualizer import DataVisualizer

CMD_PARSER = CmdParser()
CMD_PARSER.parse(sys.argv[1:])
print("Using input: state={}, keywords={}".format(CMD_PARSER.state, CMD_PARSER.keywords))

DATA_GENERATOR = DataGenerator(CMD_PARSER.state, CMD_PARSER.keywords)
print("\n=========Generating data========")
DATA_GENERATOR.run()
print(DATA_GENERATOR.covid_data.head(5))
print(DATA_GENERATOR.trend_data.head(5))

print("\n=========Processing data========")
GENERATED_DATA_FRAMES = [DATA_GENERATOR.covid_data, DATA_GENERATOR.trend_data]
DATA_PROCESSOR = DataProcessor(DATA_GENERATOR.keywords, GENERATED_DATA_FRAMES)
DATA_PROCESSOR.run()
print("\nProcessed COVID Data columns\n", DATA_PROCESSOR.clean_data_frame[0].columns)
print("\nProcessed GoogleTrends Data columns\n", DATA_PROCESSOR.clean_data_frame[1].columns)
AGGREGATED_DATA = DATA_PROCESSOR.agg_data_frame
CURR_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
OUTPUT_DIR = CURR_DIR + "/outputs/"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
CSV_FILE_PATH = OUTPUT_DIR + DATA_GENERATOR.state + "_agg_data_frame.csv"
AGGREGATED_DATA.to_csv(CSV_FILE_PATH)
print("\nAggregated cleaned dataframe saved at {}\n".format(CSV_FILE_PATH))

print("\n=========Visualizing data========")
DATA_VISUALIZER = DataVisualizer(DATA_GENERATOR.state, DATA_GENERATOR.keywords,
                                 DATA_PROCESSOR.agg_data_frame)
DATA_VISUALIZER.show()
IMG_FILE_PATH = OUTPUT_DIR + DATA_GENERATOR.state + "_coronavirus_trend_impacts.png"
print("\nVisualization saved at {}\n".format(IMG_FILE_PATH))
