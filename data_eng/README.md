## Data Engineering Tasks

Package dependencies are listed in `requirements.txt`

To Install dependencies `pip install -r requirements.txt`

To run `python main`

## Task 4
    a. 1 Million Events (~10 MB of data) - Pandas can easily handle 10MBs of data. 
    b. 1 Trillion Events (~10 TB of data) - For scaling the solution to 1TB one potential solution could be to
    use cloud storage for data storage and Python Dask to leverage parallel processing and distributed compute.
    Reason for suggesting Dask is it is relatively simple to use, aligns well with pandas dataframe and allows
    many of the same methods as this solution is already using to be reused. To my understanding, Dask takes inspiration
    from Map-Reduce architecture to achieve parallel and distributed processing. 
    
Looking forward to discuss this during the interview!