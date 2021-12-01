#!/bin/bash
set -e

if [ -z "$AZP_URL" ]; then
  echo 1>&2 "error: missing AZP_URL environment variable"
  exit 1
fi

if [ -z "$AZP_TOKEN_FILE" ]; then
  if [ -z "$AZP_TOKEN" ]; then
    echo 1>&2 "error: missing AZP_TOKEN environment variable"
    exit 1
  fi

  AZP_TOKEN_FILE=/azp/.token
  echo -n $AZP_TOKEN > "$AZP_TOKEN_FILE"
fi

unset AZP_TOKEN

TOOL_DIR="$AZP_WORK"/_tool
mkdir -p "$TOOL_DIR"/Python/3.9.5
python3.9 -m venv "$TOOL_DIR"/Python/3.9.5/x64
touch "$TOOL_DIR"/Python/3.9.5/x64.complete
ln -s "$TOOL_DIR"/Python/3.9.5 "$TOOL_DIR"/Python/3.9 

export AGENT_ALLOW_RUNASROOT="1"
cleanup() {
  if [ -e config.sh ]; then
    print_header "Cleanup. Removing Azure Pipelines agent..."

    # If the agent has some running jobs, the configuration removal process will fail.
    # So, give it some time to finish the job.
    while true; do
      ./config.sh remove --unattended --auth PAT --token $(cat "$AZP_TOKEN_FILE") && break

      echo "Retrying in 30 seconds..."
      sleep 30
    done
  fi
}

export VSO_AGENT_IGNORE=AZP_TOKEN,AZP_TOKEN_FILE
source ./env.sh

echo "1. Configuring Azure Pipelines agent..."

./config.sh --unattended \
  --agent "${AZP_AGENT_NAME:-$(hostname)}" \
  --url "$AZP_URL" \
  --auth PAT \
  --token $(cat "$AZP_TOKEN_FILE") \
  --pool "${AZP_POOL}" \
  --work "${AZP_WORK:-work}" \
  --replace \
  --acceptTeeEula & wait $!

echo "2. Running Azure Pipelines agent..."

trap 'cleanup; exit 0' EXIT
trap 'cleanup; exit 130' INT
trap 'cleanup; exit 143' TERM

./run.sh "$@" &

wait $!