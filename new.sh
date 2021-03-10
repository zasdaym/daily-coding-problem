#!/usr/bin/env bash

set -o errexit

last_number=$(ls | grep -o "[0-9][0-9][0-9]" | tail -n 1)
new_number=$(printf "%03d" $(expr ${last_number} + 1))

problem_code="problem-${new_number}"
mkdir -p ${problem_code}
touch ${problem_code}/README.md
touch ${problem_code}/solution.py
echo "${problem_code} created"
