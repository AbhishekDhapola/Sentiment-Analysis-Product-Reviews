import random
import requests
import pandas as pd
# List of 10 products
products = ["Product A", "Product B", "Product C", "Product D", "Product E",
            ]

# List of 40 random review types with longer texts
review_types = [
    "I am extremely satisfied with the performance of this product. It exceeded my expectations in every way.",
    "My experience with this product was terrible. The quality was poor, and it did not meet my needs at all.",
    "The average quality of this product makes it a decent choice. However, there is room for improvement.",
    "The service provided was superb! The support team was responsive, and I had a great overall experience.",
    "This product is not worth the money. I regret making this purchase as it did not live up to its promises.",
    "I highly recommend this product to everyone. It offers outstanding value and delivers exceptional results.",
    "The customer support for this product was poor. I faced issues and did not receive satisfactory assistance.",
    "The performance of this product is excellent. It outshines similar products in the market.",
    "While the product could be better, it still provides satisfactory results. I have mixed feelings about it.",
    "The outstanding value offered by this product makes it a worthwhile investment. I am highly impressed.",
    "My purchase was disappointing. The product did not meet my expectations, and I had a regrettable experience.",
    "The impressive features of this product set it apart from the competition. It's a great choice for enthusiasts.",
    "The design of this product is horrible. It lacks aesthetics and usability, making it a poor choice.",
    "I received satisfactory results from this product. It met my basic requirements, but there is room for improvement.",
    "Top-notch performance is the defining characteristic of this product. It exceeded my expectations.",
    "The quality of this product is awful. I encountered issues, and it did not live up to its claims.",
    "I received good customer service for this product. The support team was helpful and addressed my concerns.",
    "My overall experience with this product was mediocre. It neither impressed me nor disappointed me.",
    "The exceptional value provided by this product makes it stand out. I consider it a smart investment.",
    "This product is a waste of money. I had a terrible experience, and I do not recommend it to others.",
    "Fantastic! This product exceeded my expectations, and I am thrilled with the results.",
    "Horrendous! Avoid this product at all costs. It is a complete letdown and not worth your money.",
    "Decent. This product offers an acceptable level of performance. It's neither outstanding nor terrible.",
    "Amazing! I am impressed with the quality and features of this product. It's a must-have for enthusiasts.",
    "Dreadful. This product is a disaster. I regret my purchase, and it failed to deliver on its promises.",
    "Okay. The product is fine, but there is nothing exceptional about it. It meets basic requirements.",
    "Brilliant! This product stands out with its exceptional features and top-tier performance.",
    "Appalling! Stay away from this product. It is a disgrace, and I had an awful experience.",
    "Meh. This product is average, and I neither love it nor hate it. It's an okay choice.",
    "Phenomenal! This product exceeded my wildest expectations. It's a game-changer in its category.",
    "Disgusting. I regret buying this product. It is of poor quality, and I am highly dissatisfied.",
    "Acceptable. The product meets the minimum requirements, but it falls short of being outstanding.",
    "Spectacular! This product wowed me with its exceptional performance and innovative features.",
    "Atrocious! Avoid this product like the plague. It is a disaster, and I had a horrible experience.",
    "Fine. The product is fine, and it performs adequately. It meets basic expectations.",
    "Incredible! This product is a masterpiece. It excels in every aspect, and I am thoroughly impressed.",
    "Displeasing. I had a disappointing experience with this product. It did not live up to its claims.",
    "Top quality! This product sets the standard for excellence. It is a top-quality choice for consumers."
]

data = {
    "Product": [],
    "Review": [],
    "Sentiment": []
}

# Simulate reviews for each product
for product in products:
    for _ in range(40):
        # Select a random review type
        review_text = random.choice(review_types)

        # Simulate a POST request to the sentiment analysis API
        api_endpoint = "http://localhost:5000/analyze_sentiment"   # Replace with your actual API endpoint
        response = requests.post(api_endpoint, json={"review_text": review_text})

        # Check the sentiment prediction from the response
        if response.status_code == 200:
            result = response.json()
            sentiment_prediction = result.get("sentiment")
            print(f"Product: {product}, Review: '{review_text}', Sentiment Prediction: {sentiment_prediction}")
            # Append data to lists
            data["Product"].append(product)
            data["Review"].append(review_text)
            data["Sentiment"].append(sentiment_prediction)
        else:
            print(f"Error: {response.status_code}")
# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_file_path = "simulation_output.xlsx"
df.to_excel(output_file_path, index=False)