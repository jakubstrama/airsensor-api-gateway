 # build Docker
    docker build -t airsensor-api-gateway .
 
 # Run Docker
    docker run -d --restart --name airsensor-api-gateway -e IP_SENSOR='192.168.5.152' -p 80:80 airsensor-api-gateway