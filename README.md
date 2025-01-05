## Machine Learning Sensor Project

Directory structure:
└── Delight-In-Sensor-Fault-Detection/
    ├── README.md
    ├── app.py
    ├── requirements.txt
    ├── setup.py
    ├── upload_data.py
    ├── config/
    │   └── model.yaml
    ├── notebooks/
    │   └── wafer_23012020_041211.csv
    ├── prediction_artifacts/
    │   └── test.csv
    ├── predictions/
    │   └── prediction_file.csv
    ├── src/
    │   ├── __init__.py
    │   ├── exception.py
    │   ├── logger.py
    │   ├── components/
    │   │   ├── __init__.py
    │   │   ├── data_ingestion.py
    │   │   ├── data_transformation.py
    │   │   └── model_trainer.py
    │   ├── constant/
    │   │   └── __init__.py
    │   ├── pipeline/
    │   │   ├── __init__.py
    │   │   ├── predict_pipeline.py
    │   │   └── train_pipeline.py
    │   └── utils/
    │       ├── __init__.py
    │       └── main_utils.py
    ├── static/
    │   └── css/
    │       └── style.css
    └── templates/
        └── upload_file.html
