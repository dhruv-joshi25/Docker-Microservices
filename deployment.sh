!#/bin/bash
docker-compose -f docker-compose.yml down
echo "Stopping and removing existing containers..."
docker-compose -f docker-compose.yml up -d --build
echo "Deployment completed successfully!"