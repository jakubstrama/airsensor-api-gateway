 # build Docker
    docker build -t airsensor-api-gateway .
 
 # Run Docker
    docker run -d --name airsensor-api-gateway --restart unless-stopped -e IP_SENSOR='192.168.5.152' -p 8080:80 airsensor-api-gateway