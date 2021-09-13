from gooey import Gooey, GooeyParser

@Gooey(
    program_name = "Test GUI")
def main():
    parser = GooeyParser(description='Test GUI')

    parser.add_argument('file_directory', metavar = "File Directory", action='store', help="Location of the Excel File to process", widget='FileChooser')
    
    parser.add_argument('timeframe', metavar = "Timeframe", action='store', help="Year (ex. 2020) or specific Month (ex. March, first letter must be capital)")

    args = parser.parse_args()
    print("File chosen: " + args.file_directory)
    print("Timeframe (Year/Month): " + args.timeframe)
    
if __name__ == '__main__':
    main()