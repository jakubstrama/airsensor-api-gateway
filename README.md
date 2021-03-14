 # build Docker
    docker build -t airsensor-api-gateway .
 
 # Run Docker
    docker run -d --name airsensor-api-gateway -p 80:80 airsensor-api-gateway