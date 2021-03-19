from fastapi import FastAPI
import requests
import os

app = FastAPI()

sensor_url = None

@app.on_event("startup")
async def startup_event():
    global sensor_url
    ip_sensor = os.environ['IP_SENSOR']
    sensor_url = 'http://{}/api/air/state'.format(ip_sensor)



@app.get('/')
def air_state():
    return requests.get(sensor_url).json()



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
 