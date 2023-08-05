#!/usr/bin/env bash

set -e -o pipefail -u

self_dir=$(cd "$(dirname "$0")" &>/dev/null; pwd -P)
self_name=$(basename -s .sh "$0")

git ls-files ':!*.awk' ':!*.md' ':!*.py' '!*.rst' \
  | xargs awk -f "$self_dir/$self_name.awk"
