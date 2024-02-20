#!/bin/bash

# This script is used for batch running the scripts
# Usually generated by the script generator script_generator.py in the root directory

script_dir=$(dirname "$0")/scripts

for script in "$script_dir"/*.sh; do
    if [ "$script" = "$script_dir/runner.sh" ]; then  # Dont run yourself
        continue
    fi
    echo "Queueing $script"
    qsub "$script"
done
