from context import coronavirus_lifestyle_impacts
import unittest
import sys
from coronavirus_lifestyle_impacts.cmd_parser import CmdParser

class UnitTests(unittest.TestCase):

    def setUp(self):
        self.cmd_parser = CmdParser()
        self.parser = self.cmd_parser.create_parser()

    def test_create_parser_state_args_pass(self):
        """
        Test create_parser() which generates state argument.
        """
        args = self.parser.parse_args(['-s', 'NY'])
        self.assertEqual(args.state, "NY")

    def test_create_parser_keywords_args_pass(self):
        """
        Test create_parser() which generates keyword argument.
        """
        args = self.parser.parse_args(['--keywords', 'Dogs, Cats'])
        self.assertEqual(args.keywords, "Dogs, Cats")

    def test_create_parser_state_and_keywords_args_pass(self):
        """
        Test create_parser() which generates state and keyword arguments.
        """
        args = self.parser.parse_args(['--keywords', 'Dogs, Cats', '--state', 'ca'])
        self.assertEqual(args.state, "ca")
        self.assertEqual(args.keywords, "Dogs, Cats")

    def test_validate_args_pass(self):
        """
        Test validate_args() which normalizes state input to state abbreviation
        and constructs keyword lists without whitespaces.
        """
        args = self.parser.parse_args(['--keywords', '  Dogs, Cats, Birds  ',
                '--state', 'Minnesota'])
        self.cmd_parser.validate_args(args)
        self.assertEqual(self.cmd_parser.state, "Minnesota")
        self.assertEqual(self.cmd_parser.keywords, ['Dogs', 'Cats', 'Birds'])


    def test_validate_lowercase_state_args_pass(self):
        """
        Test validate_args() which normalizes state input to state abbreviation
        and constructs keyword lists without whitespaces.
        """
        args = self.parser.parse_args(['--keywords', '  Dogs, Cats, Birds  ',
                '--state', 'new york'])
        self.cmd_parser.validate_args(args)
        self.assertEqual(self.cmd_parser.state, "New York")
        self.assertEqual(self.cmd_parser.keywords, ['Dogs', 'Cats', 'Birds'])



if __name__ == '__main__':
    unittest.main()
