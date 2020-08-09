from amazontrends import AmazonTrends, Category

print(AmazonTrends.get_trends(category=Category.HANDMADE, debug=True))