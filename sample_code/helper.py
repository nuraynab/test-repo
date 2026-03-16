
def write_to_gcs(df, bucket_name, file_path):
    """
    Writes a Pandas DataFrame to a CSV file in Google Cloud Storage.

    Args:
        df (pandas.DataFrame): The DataFrame to write.
        bucket_name (str): The name of the GCS bucket.
        file_path (str): The path to the file within the bucket (e.g., 'folder/filename.csv').
    """
    from google.cloud import storage
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_path)
    blob.upload_from_string(df.to_csv(index=False), 'text/csv')
