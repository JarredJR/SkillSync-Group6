#!/bin/zsh
# Navigate to the script directory
cd "$(dirname "$0")"

echo "Building SkillSync app..."
./build.command

echo "Opening SkillSync.app..."
open dist/SkillSync.app
