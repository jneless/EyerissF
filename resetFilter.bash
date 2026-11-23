#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
python3 filterReset.py
python3 Lenet5_Hive.py
