# deploy-model-gcp-app-engine
An example of model deployment on GCP App Engine using FastAPI

To send a sample request locally run `python call_endpoint.py`. To run the REST API locally run `uvicorn main:app` and connect to *localhost:8000/docs*. To deploy the REST API app on google cloud run `bash deploy.sh`. When the app is deployed check GCP App Engine default service for app URL.

The repo assumes that the model predicting heart failure is deployed on GCP endpoint `3582296844224430080` in project `ai4medicine-cloud` in region `europe-west3`. If not, adjust endpoint definition in *call_endpoint.py* and *main.py*.

The model input is a list of integers of length 5. The features are the following: Age, Maximal heartrate, resting blood pressure is more than 120 bpm (1 or 0), cholesterol level is more than 200 (1 or 0), sex (1 male 0 female).