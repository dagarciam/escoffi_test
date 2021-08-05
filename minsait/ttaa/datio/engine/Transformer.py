from pyspark.sql import SparkSession, DataFrame

from minsait.ttaa.datio.common.Constants import *
from minsait.ttaa.datio.common.naming.Risk import *
from minsait.ttaa.datio.common.naming.Sunedu import *
from minsait.ttaa.datio.utils.Writer import Writer


class Transformer(Writer):
    def __init__(self, spark: SparkSession):
        self.spark: SparkSession = spark
        sunedu: DataFrame = self.read_input_csv(INPUT_SUNEDU_PATH)
        risk: DataFrame = self.read_input_csv(INPUT_RISK_PATH)

        # This was a Jr Developer Try, and now he needs our help!
        self.try_one(sunedu, risk).show(truncate=False)

        ## uncomment to persist the output
        # self.write(df)

    def try_one(self, sunedu, risk) -> DataFrame:
        return sunedu. \
            join(risk, education_level_desc.column() == parameter_value_desc.column(), "inner")

    def read_input_csv(self, path) -> DataFrame:
        """
        :return: a DataFrame readed from csv file
        """
        return self.spark.read. \
            option(HEADER, True). \
            option(INFER_SCHEMA, True). \
            csv(path)
