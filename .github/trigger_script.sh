#!/bin/bash

# Check all pyproject.toml files that have changed
for file in $(git diff --name-only HEAD~1..HEAD | grep pyproject.toml); do
    # Extract the current version and buikd the expected tag
    dirpath=$(dirname $file)
    expected_tag=$(.github/helper.sh $dirpath --path-version)
    version=$(.github/helper.sh $dirpath)
    # Check if the tag already exists
    if git rev-parse --verify $expected_tag^{tag} &> /dev/null; then
        echo "Tag '$expected_tag' already exists."
    else
        echo "Tag '$expected_tag' does not exist. Creating new tag to trigger release."
        git tag -a $expected_tag -m "Release $version"
        #git push origin tag $expected_tag
    fi              
done
