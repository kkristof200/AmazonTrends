from amazontrends import AmazonTrends, Category

print(AmazonTrends.get_trends(category=Category.PREMIUM_BEAUTY, max_results_per_letter=10, debug=True))