# Iguazio Feature Store Demo

## Motivation
**Deploying an ML-driven product that can serve online model predictions accurately as a functional part of the product is a very complex task, but it shouldn’t be that way. Iguazio can simplify this process and effectively reduce friction between data scientists and engineers.**

- MLOps Processes and Feature Store are tightly integrated for a seamless user experience and ease of use
- Facilitates interdependencies between pipeline steps
    - Data Ingest/Prep
    - Model Train/Evaluation
    - Model Deploy
    - Model Monitor
- Portable between Azure, AWS, GCP* and on-prem*
- Features
    - Support for real-time streaming
    - Batch/Real-Time Transformation
    - Versioning
    - Stateful transformations*
    - Built-in feature monitoring and concept drift*
    - Full MLOps stack*


\* Unique to Iguazio

## Getting Started
*Be sure to install latest versions of `mlrun`/`storey` and update `config.yaml` with AWS and PostgreSQL credentials*

- `fs_data_ingestion_prep.ipynb`
    - Full ingestion demo with datasets included. Can run as is. Goes through main flow of:
        - Ingesting from different data sources
        - Performing basic data transformations
        - Creating feature sets/vectors
        - Retrieving feature vectors in batch and real-time

- `fs_fraud_detection_ingest.ipynb`
    - Demo of ingestion/transformation for fraud detection with dataset included. Can run as is. Includes:
        - Defining custom transformation steps
        - More advanced filtering and feature creation