from pyspark import SparkConf, SparkContext
import re

conf = SparkConf().setAppName("WordCount_Spark").setMaster("local[*]")
sc = SparkContext(conf=conf)

# Lecture du fichier depuis HDFS
text = sc.textFile("hdfs:///user/samah/bigdata_project/input/corpus_fr.txt")

# Nettoyage + découpage
words = text.flatMap(lambda line: re.findall(r"[a-zàâçéèêëîïôûùüÿñæœ]+", line.lower()))

# WordCount
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# Sauvegarde dans HDFS
word_counts.saveAsTextFile("hdfs:///user/samah/bigdata_project/output_spark")

sc.stop()
