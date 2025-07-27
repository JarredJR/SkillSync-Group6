#!/bin/zsh

# Navigate to the script directory
cd "$(dirname "$0")"

echo "Cleaning old build..."
rm -rf build dist

echo "Packing SkillSync with data folder..."
flet pack main.py --name "SkillSync" --add-data "data:data"

echo "Build finished! App is in the dist/ folder."
