
def extract_cool(row):
	return row[1]

yelp_df.map(extract_cool).mean()


yelp_df.select("cool","review_count","stars","open").filter(yelp_df.review_count >= 10).filter(yel_df.stars == 5).groupBy("stars","review_count","open").avg("cool").show()

yelp_df.select("cool","review_count","stars").filter(yelp_df.review_count >= 10).filter(yel_df.stars == 5).filter(yelp_df.open == true).groupBy("stars").avg("cool").show()

yelp_df.select("review_count","state","open").filter(yelp_df.review_count >= 10).groupBy("state","open").count().show()

yelp_df.groupBy("business_id").count()


yelp_df.registerTempTable("yelp")

filtered_yelp = sqlCtx.sql("SELECT count(*) FROM orders o WHERE o.order_status == 'SUSPECTED_FRAUD'")

sqlCtx.sql("SELECT count(*) FROM order_items o WHERE o.order_status == 'SUSPECTED_FRAUD'").show()


fm = sqlCtx.sql("Select order_item_order_id, SUM(order_item_subtotal) as total from order_items GROUP BY order_item_order_id ORDER BY total DESC").show()

sqlCtx.sql("Select order_items inner join orders")



