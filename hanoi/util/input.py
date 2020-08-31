import argparse


def get_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num_plates", default=3,
                        help="Number of plates.", type=int)
    parsed_args = parser.parse_args(args)
    return parsed_args
