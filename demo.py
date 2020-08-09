from amazontrends import AmazonTrends, Category

print(AmazonTrends.get_trends(category=Category.HANDMADE, max_results_per_letter=2, debug=True))