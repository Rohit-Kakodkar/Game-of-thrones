import sys
sys.path.append('../data')

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

def spark_conf(master):
    '''
        Spark config inputs to increase throughput of spark Streaming
            input - master : DNS of spark master node
            rvalue - spark_config object
    '''

    # spark config
    sc_conf = SparkConf()
    sc_conf.setAppName("DroneDetect")
    sc_conf.set("spark.executor.memory", "1000m")
    sc_conf.set("spark.executor.cores", "2")
    sc_conf.set("spark.executor.instances", "15")
    sc_conf.set("spark.driver.memory", "5000m")

    return sc_conf

if __name__ == '__main__':

    sc = SparkContext(conf = sc_conf).getOrCreate()
    quiet_logs(sc)
    text_file = sc.text_file("data/indexing/1")

    
