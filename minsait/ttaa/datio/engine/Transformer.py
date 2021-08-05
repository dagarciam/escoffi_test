import pyspark.sql.functions as f
from pyspark.sql import SparkSession, WindowSpec, Window, DataFrame, Column

from minsait.ttaa.datio.common.Constants import *
from minsait.ttaa.datio.utils.Writer import Writer


class Transformer(Writer):
    def __init__(self, spark: SparkSession):
        self.spark: SparkSession = spark
        sunedu: DataFrame = self.read_input(INPUT_SUNEDU_PATH)
        risk: DataFrame = self.read_input(INPUT_SUNEDU_PATH)
        sunedu.printSchema()
        risk.printSchema()
        ## uncomment to persist the output
        # self.write(df)

    def read_input(self, path) -> DataFrame:
        """
        :return: a DataFrame readed from avro file
        """
        return self.spark.read.parquet(path)
