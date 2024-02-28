from statistic import array_info, array_info_by_numpy
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='NumberFileInfo',
                                     description="""This program can calculate min, max, mean, median,
                                      maximum length of increasing and decreasing sequences (numpy variant
                                      is not include this options) from file or array"""
                                     )
    parser.add_argument("-f", "--file", nargs='?', default="10m.txt", help='File name, (default: 10m.txt)')
    parser.add_argument('-t', '--type_calculation', choices=['own', 'numpy'],
                        help="""type calculation own developed or use numpy (default: own). 
                        For use numpy you should install this module.""", default='own')
    parser.add_argument('-a', '--array', nargs='+', type=int,
                        help='Array for calculate. If it is defined then the file name is ignore')
    parser.print_help()
    args = parser.parse_args()
    print("Start data processing")
    if args.array is not None:
        data_array = args.array
    else:
        data_array = args.file
    calculation_func = array_info_by_numpy if args.type_calculation == 'numpy' else array_info
    print(calculation_func(data_array))