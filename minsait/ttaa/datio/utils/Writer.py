from pyspark.sql import DataFrame

from minsait.ttaa.datio.common.Constants import *

class Writer:
    def write(self, df: DataFrame):
        df \
            .write \
            .parquet(OUTPUT_PATH);
