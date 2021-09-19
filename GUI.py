from gooey import Gooey, GooeyParser
import Driver as dv
@Gooey(
    program_name = "Graph Automater")
def main():
    parser = GooeyParser(description='AutGraph')

    parser.add_argument('file_directory', metavar = "File Directory", action='store', help="Location of the Excel File to process", widget='FileChooser')
    
    parser.add_argument('timeframe', metavar = "Timeframe", action='store', help=" 'Year' or specific Month (ex. March, first letter must be capital)")

    args = parser.parse_args()
    dv.Driver(str(args.file_directory), str(args.timeframe))
    
if __name__ == '__main__':
    main()