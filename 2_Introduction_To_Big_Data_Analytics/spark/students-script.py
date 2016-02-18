# Following code are executed as scripts
# through the iPython in Cloudera CDH

students = sc.parallelize([[100,"Alice",8.5,"Computer Science"],[101,"Bob",7.1,"Engineering"],[102,"Carl",6.2,"Engineering"]])

def extract_grade(row):
	return row[2]

students.map(extract_grade).mean() //return 7.26666

//Find maximum
def extract_degree_grade(row):
	return (row[3], row[2])

degree_grade_RDD = students.map(extract_degree_grade)

degree_grade_RDD.collect()

// You get
[('Computer Science', 8.5),
 ('Engineering', 7.0999999999999996),
 ('Engineering', 6.2000000000000002)]


degree_grade_RDD.reduceByKey(max).collect()


=============================================================
students_df = sqlCtx.createDataFrame(students, ["id", "name", "grade", "degree"])
students_df.printSchema()

//You get, you read from students, so data will be load in to the schema.
root
 |-- id: long (nullable = true)
 |-- name: string (nullable = true)
 |-- grade: double (nullable = true)
 |-- degree: string (nullable = true)



students_df.agg({"grade":"mean"}).collect()
students_df.groupBy("degree").max("grade").collect()

//You get
[Row(degree=u'Computer Science', MAX(grade#4)=8.5),
 Row(degree=u'Engineering', MAX(grade#4)=7.0999999999999996)]


from pyspark.sql.types import *
schema = StructType([
StructField("id", LongType(), True),
StructField("name", StringType(), True),
StructField("grade", DoubleType(), True),
StructField("degree", StringType(), True)]) 


--Load a JSON file

students_json = [
'{"id":100, "name":"Alice", "grade":8.5, "degree":"Computer Science"}',

'{"id":101, "name":"Bob", "grade":7.1, "degree":"Engineering"}']

with open("students.json", "w") as f: f.write("\n".join(students_json))

--Dump

cat students.json

--Create a DataFrame with Json file

sqlCtx.jsonFile("file:///home/cloudera/ipython-1.2.1/students.json").show()

--CSV

--Restart pyspark

PYSPARK_DRIVER_PYHON=ipython pyspark --packages com.databricks:spark-csv_2.10:1.3.0

yelp_df = sqlCtx.load(
source="com.databricks.spark.csv",
header = 'true',
inferSchema = 'true',
path = 'file:///usr/lib/hue/apps/search/examples/collections/solr_configs_yelp_demo/index_data.csv') 
