from pyspark import SparkContext
from pyspark.sql import SQLContext
from  pyspark.sql.functions import input_file_name
import string
import os
from time import sleep

def parse_args():

    '''
        Parse command line arguments
    '''
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_folder', type=str, default='input',\
                                help='Location of input files')
    parser.add_argument('--output_folder', type=str, default= 'output', \
                                    help='Location of the output folder')
    args = parser.parse_args()

    return args

def quiet_logs( sc ):
    '''
        Quiel spark logs in console
    '''
    logger = sc._jvm.org.apache.log4j
    logger.LogManager.getLogger("org"). setLevel( logger.Level.ERROR )
    logger.LogManager.getLogger("akka").setLevel( logger.Level.ERROR )

def process_files(path):
    '''
        Read input file and parse words to create a words rdd

        input :
            path - location of input files
        output :
            words_rdd - rdd specifying all the distict words in the file
    '''

    text_file = sc.textFile(path)
    try:
        words_with_file = text_file.flatMap(lambda line: line.split())\
                            .map(lambda x : (x, doc)).distinct()
    except ValueError:
        print('File is empty')

    return words_with_file


if __name__ == '__main__':

    '''
        Driver function to calculate reverse index
    '''

    args = parse_args()
    input = args.input
    output = args.output

    sc = SparkContext.getOrCreate()
    quiet_logs(sc)

    words_with_file = []
    for doc in os.listdir(input):
        words_with_file.append(process_files((input + '/' + doc)))

    # Combine rdds
    combined_rdds = sc.union(words_with_file).map(lambda x: (x[0], [int(x[1])]))\
                    .reduceByKey(lambda x,y: x + y)

    # map words to a value
    word_dict = combined_rdds.map(lambda x: x[0]).zipWithIndex().collectAsMap()

    # generate reverse index
    combined_rdds = combined_rdds.map(lambda x: (word_dict[x[0]], x[1]))
