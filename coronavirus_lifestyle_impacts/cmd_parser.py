"""
This is the interface between the end-user and our service. The CommandLineParser
will take the user command, validates the inputs, and pass it down to the
downstream services. It is lightweight and should always return a response to
the end user.
"""

import argparse
import us

class CmdParser:
    """
    CmdParser class which contains logic to take command line arguments, parse
    based on restrictions, and validate the parsed values.
    """
    STATE = "state"
    KEYWORDS = "keywords"
    DEFAULT_KEYWORDS = "Bars near me, Home workouts"
    CLI_DESCRIPTION = "Coronavirus Lifestyle Impacts CLI"

    def __init__(self):
        self.args = None
        self.state, self.keywords = None, None

    def parse(self, args):
        """
        The main parse logic which calls the following helper functions
        - create_parser()
        - validate_args()
        and generates required arguments for next module.

        Input: command line arguments in a list
        Return: None
        """
        parser = self.create_parser()
        self.args = parser.parse_args(args)
        self.validate_args(self.args)

    def create_parser(self):
        """
        Creates a Python argparser object by reading in command line arguments
        and performs preliminary validation.

        Two arguments expecting from user:
        --state: a list of US state names
        --keywords: a list of lifestyle related keywords, delimited by comma
        """
        parser = argparse.ArgumentParser(description=self.CLI_DESCRIPTION)
        parser.add_argument("-s", "--" + self.STATE, action="store", default="WA",
            required=False, help="the US state to pull the data from. Can take\
                    either full name and abbreviation. Default: \"Washington\"")
        parser.add_argument("-k", "--" + self.KEYWORDS, action="store",
                default=self.DEFAULT_KEYWORDS, required=False,
                help="the comma delimited search keyword string. Default: \
                        \"Bars near me, Home workouts\" ")
        return parser

    def validate_args(self, args):
        """
        Validates the parsed arguments.

        - For state, raise an exception if the input state is not a valid US state.
        - For keywords, strip leading and trailing whitespaces in keyword and
          reformat from a keyword string to a keyword list.

        Inputs: a parsed argparser object
        Return: None
        Throws: ValueError if input arguments contains invalid state values
        """
        try:
            self.state = us.states.lookup(args.state).abbr
            keywords_string = args.keywords.strip()
            self.keywords = keywords_string.split(",")
            for i, keyword in enumerate(self.keywords):
                self.keywords[i] = keyword.strip()
        except Exception as error:
            raise ValueError("Encountered argument validation error: {}".format(error))
