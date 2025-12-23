#!/bin/bash

DAY=$1
MESSAGE=$2

if [ -z "$DAY" ] || [ -z "$MESSAGE" ]; then
    echo "Usage: ./commit.sh DAY_NUMBER \"message\""
    echo "Example: ./commit.sh 1 \"2 problems, setup complete\""
    exit 1
fi

git add .
git commit -m "Day $DAY: $MESSAGE"
git push

echo "✅ Committed and pushed: Day $DAY"
