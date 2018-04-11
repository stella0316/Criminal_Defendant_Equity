from pyspark import SparkContext

#read files from folder

sc = SparkContext()

path = 'hdfs://dumbo/user/ks4841/txt_sample/'
#Get: filepath, content
data = sc.wholeTextFiles('txt_sample/*')
len_path = len(path)
data = data.map(lambda x: (x[0][len_path:],x[1]))#extract file name from path


def fetch_name(pair):
	'''
 Each pair is a fileid with file. 
 Return fileid and name of defendant
	'''

	doc_id = pair[0]
	text = pair[1]

	text = text[0:500] #take first 500 characters for easier processing
	text = text.split(' ')
	name_year = text[2].split('\n\t')
	name = name_year[0]
	year = name_year[1]
	
	return (doc_id, name, year)

data = data.map(fetch_name)

print(data.take(5)) #print to check output

data.saveAsTextFile("sample_output.csv")






