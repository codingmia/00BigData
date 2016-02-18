# Following code are executed as scripts
# through the iPython in Cloudera CDH

show_views_file = sc.textFile("/user/cloudera/sj_input2/join2_gennum?.txt")


def split_show_views(line):
	line = line.strip()
	key_value = line.split(",")
	show = key_value[0]
	view = key_value[1]
    return (show, views)

show_views = show_views_file.map(split_show_views)

show_views.collect()

show_channel_file = sc.textFile("input/join2_genchan?.txt")

show_channel_file.take(2)

	
def split_show_channel(line):
	show, channel = line.split(",")
	return (show, channel)

show_channel = show_channel_file.map(split_show_channel)

show_channel.collect()

joined_dataset = show_views.join(show_channel)

def extract_channel_views(show_views_channel):
	show = show_views_channel[0]
	views_channel = show_views_channel[1]
	views = int(views_channel[0])
	channel = views_channel[1]
	return(channel,views)
	
channel_views = joined_dataset.map(extract_channel_views)

def sumX(a, b):
	some_result = a + b
	return some_result

channel_views.reduceByKey(sumX).collect()
