import csv
from datetime import datetime, timedelta
import glob

def filter_tweets(start_date, end_date, input_path, output_file):
    
    # Converting start and end dates strings to datetime objects
    
    start_datetime = datetime.strptime(start_date.strip(), "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date.strip(), "%Y-%m-%d")

    # Adjusting the end datetime to include the entire end day
    
    end_datetime += timedelta(days=1)

    filtered_tweets = []  # List to store filtered tweets

    # Iterating over CSV file in the input path
    
    for file_path in glob.glob(input_path):
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader) 

            # Indices of columns
            
            tweet_id_index = header.index("id")
            created_at_index = header.index("created_at")
            tweet_text_index = header.index("text")

            for row in reader:
                tweet_id = row[tweet_id_index]
                created_at = datetime.strptime(row[created_at_index].split("+")[0].strip(), "%Y-%m-%d %H:%M:%S")
                tweet_text = row[tweet_text_index]

                # Checking if tweet is within the specified time period or not 
                
                if start_datetime <= created_at <= end_datetime:
                    
                    # Appending only the necessary columns to the filtered_tweets list
                    
                    filtered_tweets.append((created_at, tweet_text))

    # Writing the filtered tweets to the output file
    
    with open(output_file, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        
        # Writing the header row without the "tweet_id" column
        
        writer.writerow(["created_at", "text"])

        for tweet in filtered_tweets:
            writer.writerow(tweet)

    print("Filtered tweets saved to", output_file)

start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")
input_path = input("Enter the path to input CSV files: ")
output_file = input("Enter the output file name: ")

filter_tweets(start_date, end_date, input_path, output_file)

