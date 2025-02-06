from flyer_events.data_loader import DataLoader
from flyer_events.customer_engagement import CustomerEngagement
FLYER_ID = 2020004

if __name__ == '__main__':
    file_path = 'flyer_events_dataset.csv'
    
    # Load data
    data_loader = DataLoader(file_path)
    df = data_loader.load_data()
    
    # customer engagement tasks
    if df is not None:
        processor = CustomerEngagement(df)
        processor.filter_open_events()
        # Task 1
        processor.get_unique_users()
        # Task 2
        processor.get_users_avg_time()
        # Task 3
        processor.get_flyer_mean_time(FLYER_ID)
