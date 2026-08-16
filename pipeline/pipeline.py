from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

def ingest(
    url: str,
    engine,
    target_table: str,
    chunk_size: int = 100_000
):
    df_iter = pd.read_csv(
        url,
        iterator=True,
        dtype=dtype,
        parse_dates=parse_dates,
        chunksize=chunk_size
    )

    first = True

    for chunk in df_iter:
        if first:
            # Create a table
            chunk.head(n=0).to_sql(
                name=target_table,
                con=engine,
                if_exists='replace'
            )
            print("Table has been created")

            first = False

        chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists='append'
        )
        print(f"Inserted chunk: {len(chunk)} rows")


def main():
    pg_user = os.environ.get("POSTGRES_USER")
    pg_pass = os.environ.get("POSTGRES_PASSWORD")
    pg_db = os.environ.get("POSTGRES_DB")
    pg_host = os.environ.get("POSTGRES_HOST")
    pg_port = os.environ.get("POSTGRES_PORT")
    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
    target_table = 'yellow_taxi_data'
    chunk_size = 100_000

    engine = create_engine(f"postgresql+psycopg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}")

    ingest(
        url=url,
        engine=engine,
        target_table=target_table,
        chunk_size=chunk_size
    )


if __name__ == "__main__":
    main()