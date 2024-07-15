PWD=$(pwd)
if [[ ! $PWD =~ .*/nba_api$ ]] ; then
  echo "Please run this script from the project root directory"
  exit 1
fi

REGISTRY=$(cat deployment/registry)
VERSION=$(cat deployment/version)
PORT=$(cat deployment/port)

echo "Updating Dockerfile"

sed -e "s|<port>|$PORT|g" deployment/Dockerfile.template > deployment/Dockerfile

echo "Dockerfile updated"

#docker build -t "$REGISTRY"/nba_api:"$VERSION" -f deployment/Dockerfile .
#docker tag "$REGISTRY"/nba_api:"$VERSION" "$REGISTRY"/nba_api:latest