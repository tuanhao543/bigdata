from pyspark import SparkContext


sc = SparkContext()


data = sc.parallelize([10, 4, 33, 20, 5])


sum = data.sum()

print(sum)


