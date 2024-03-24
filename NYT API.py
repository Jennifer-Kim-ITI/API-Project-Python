#Question: "How many articles were written about the Ukraine-Russian war month-over-month from February 24, 2022, to December 1, 2023
#and do the number of articles correlate with the significant events that occurred in the conflict?"

#Import the necessary libraries
import requests, csv, time, json
from pathlib import Path

#Set up the basic authentication with parameters
curr_dir = Path.cwd()
API_KEY = "xXaHR4taA8fYNMQbOrBiYlCFnfmMFwL2"
URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

#Set up a function to pull data from the API 
def pull_data(page_num=0, q='Ukraine-Russian War'):
    """
    Pulls data from the NYT API
    
    Parameters:
    page_num (int): Page number for pagination.
    q (str): Query 
    
    Returns:
    dict: Response from the API 
    """
    parameters = {'q': q,
                 'api-key': API_KEY,
                 'fq': 'document_type("article")',
                 'begin_date': '20220224', #assuming we start from the invasion date
                 'end_date': '20231201',
                 'page': page_num}
    response = requests.get(URL, params=parameters)
    time.sleep(12) #Recommend by NYT 
    content = response.json()
    print(content['response']['meta']) #Just to show it is working and getting the data 
    return content['response']

#Created a dictionary
articles_by_month = {}

#Function to do the data extract and filter the dates of articles
def extract_pub_dates_and_count(results, articles_by_month):
    """
    Parameters:
    results (dict): API response
    articles_by_month (dict): Dictionary to store articles count by month 
    
    dict: Updated articles_by_month dictionary 
    """
    pub_dates = [article['pub_date'][:7] for article in results['docs']] 
    for pub_date in pub_dates:
        articles_by_month[pub_date] = articles_by_month.get(pub_date, 0) + 1
    return articles_by_month

#Created a function to calculate the # of pages based on the number of hits in the response 
def get_total_pages():
    """
    Reutns:
    int: Total number of pages
    """
    response = pull_data(page_num=0)
    hits = response['meta']['hits']
    return (hits // 10) + 1

#A loop to determine the total # of pages to iterate over
#Runs to pull data for each page using the pull_data function to extract the pub_dates and count 
num_pages = get_total_pages()
for page_num in range(num_pages): 
   try:
       response = pull_data(page_num)
       articles_by_month = extract_pub_dates_and_count(response, articles_by_month)
   except KeyError:
       print('Time out error. Extend time and rerun')
       break

#Sort years and count articles
sorted_months = sorted(articles_by_month.keys())
total_articles_by_month = [(month, articles_by_month[month]) for month in sorted_months]

#Print the number of articles for each year
for month, article_count in total_articles_by_month:
   print(f"Month: {month}, Articles: {article_count}")

#Write results to CSV
results_csv_path = curr_dir / "articles_by_month.csv"
with results_csv_path.open(mode='w', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(["Month", "Number of Articles"])
   writer.writerows(total_articles_by_month)