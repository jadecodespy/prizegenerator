. ~/.bashrc 

ssh jenkins@swarm-master << EOF
cd /home/jadekanimodo/prizegenerator
. /home/jadekanimodo/.bashrc
env DATABASE_URI=${DATABASE_URI} docker stack deploy --compose-file docker-compose.yaml stackcode
EOF
