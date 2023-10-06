from pipelines.training_pipeline import train_pipeline
from zenml.client import Client

if __name__ == "__main__":
    # Run the pipeline

    print(Client().active_stack.experiment_tracker.get_tracking_uri())

    train_pipeline(data_path="/home/neon/Documents/projects/customer_satisfaction/data/olist_customers_dataset.csv")
    
#mlflow server --backend-store-uri "file:/home/neon/.config/zenml/local_stores/5f162882-4a6e-4b03-a19c-c9376c426ba0/mlruns"
#mlflow ui --backend-store-uri "file:/home/neon/.config/zenml/local_stores/5f162882-4a6e-4b03-a19c-c9376c426ba0/mlruns"