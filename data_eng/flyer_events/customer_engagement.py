import pandas as pd
from functools import wraps
from .logger import setup_logger

class CustomerEngagement:
    def __init__(self, df):
        self.df = df
        self.open_events = None
        self.logger = setup_logger("CustomerEngagement")

    def handle_exceptions(func):
        """Catch and log exceptions."""
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                self.logger.error(f"Error in {func.__name__}: {str(e)}")
                raise
        return wrapper

    @handle_exceptions
    def filter_open_events(self):
        """
        Filter flyer_open events and calculate time spent on flyers.
        """
        self.open_events = self.df[self.df['event'] == 'flyer_open']
        self.open_events = self.open_events.sort_values(['user_id', 'timestamp'])
        self.open_events['next_timestamp'] = self.open_events.groupby('user_id')['timestamp'].shift(-1)
        self.open_events['time_spent'] = (self.open_events['next_timestamp'] - self.open_events['timestamp']).dt.total_seconds()
        self.open_events = self.open_events[(self.open_events['time_spent'] > 0)]

        self.logger.info("Flyer events filtered and calculated time spent on flyers.")

    def get_unique_users(self):
        """
        Calculate number of unique users.
        """
        unique_users = self.df['user_id'].nunique()
        self.logger.info(f"Unique users: {unique_users}")
        return unique_users
    
    @handle_exceptions
    def get_users_avg_time(self):
        """
        Calculate mean time spent across flyers by each user.
        Returns:
        users_avg_time (pd.DataFrame): dataframe with avg time for users
        """
        output_file = "average_time_per_user.csv"
        users_avg_time = self.open_events.groupby('user_id')['time_spent'].mean().reset_index()
        users_avg_time.columns = ['user_id', 'avg_time_spent']
        users_avg_time['avg_time_spent'] = users_avg_time['avg_time_spent'].round(2)
        users_avg_time.to_csv(output_file)
        self.logger.info(f"Average time per user saved to {output_file}")
        return users_avg_time

    @handle_exceptions
    def get_flyer_mean_time(self, flyer_id: int):
        """
        Calculate mean time users spent on a flyer.
        Args:
        flyer_id (int): used to filter flyer_open events for mean calculation

        Returns:
        average_time_flyer (float): Return mean time for passed flyer_id 
        or NaN if flyer_id is not found.
        """
        filtered_df = self.open_events[self.open_events['flyer_id'] == flyer_id]
        if filtered_df.empty:
            self.logger.warning(f"No records found for flyer ID {flyer_id}.")
            return float('nan')

        average_time_flyer = filtered_df['time_spent'].mean()
        self.logger.info(f"Average time spent on flyer ID {flyer_id}: {average_time_flyer:.2f} seconds")
        return average_time_flyer
