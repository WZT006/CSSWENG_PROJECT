from gooey import Gooey, GooeyParser

@Gooey()
def main():
    parser = GooeyParser(description='Test GUI')

    parser.add_argument('file_directory', action='store', help="Location of the Excel File to process", widget='FileChooser')
    
    parser.add_argument('timeframe', action='store', help="Month (Year for year report), format 'Month' :")

    parser.parse_args()
    
if __name__ == '__main__':
    main()