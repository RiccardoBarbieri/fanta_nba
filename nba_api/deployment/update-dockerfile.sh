PWD=$(pwd)
if [[ ! $PWD =~ .*/nba_api$ ]] ; then
  echo "Please run this script from the project root directory"
  exit 1
fi

REGISTRY=$(cat deployment/registry)
VERSION=$(cat deployment/version)
PORT=$(cat deployment/port)

sed -e "s|<port>|$PORT|" deployment/Dockerfile.template > deployment/Dockerfile

#docker build -t "$REGISTRY"/nba_api:"$VERSION" -f deployment/Dockerfile .
