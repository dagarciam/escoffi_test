import pyspark.sql.functions as f
from pyspark.sql import SparkSession, WindowSpec, Window, DataFrame, Column

from minsait.ttaa.datio.common.Constants import *
from minsait.ttaa.datio.utils.Writer import Writer


class Transformer(Writer):
    def __init__(self, spark: SparkSession):
        self.spark: SparkSession = spark
        df: DataFrame = self.read_input(INPUT_SUNEDU_PATH)
        df.printSchema()
        # self.write(df)

    def read_input(self, path) -> DataFrame:
        """
        :return: a DataFrame readed from avro file
        """
        return self.spark.read.format("com.databricks.spark.avro").load(path)
