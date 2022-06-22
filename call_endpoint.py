from google.cloud import aiplatform

patient = [65, 87, 1, 1, 1]

endpoint = aiplatform.Endpoint(
    endpoint_name="3582296844224430080",
    project="ai4medicine-cloud",
    location="europe-west3"
)

prediction = endpoint.predict(instances=[patient])
print(prediction.predictions[0])
print(prediction.deployed_model_id)
