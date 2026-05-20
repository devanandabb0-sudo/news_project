import json
import boto3
import os

from datetime import datetime

s3 = boto3.client("s3")

BUCKET_NAME = os.environ.get(
    "S3_BUCKET_NAME"
).strip()


def save_to_s3(news_data):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"raw-news/news_{timestamp}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=json.dumps(news_data),
        ContentType="application/json"
    )

    print("Uploaded successfully")  