#!/bin/bash

# Immediate exit on failure
set -e

# Check all pyproject.toml files that have changed
for file in $(git diff --name-only HEAD~1..HEAD | grep pyproject.toml); do
    # Extract the current version and build the expected tag
    dirpath=$(dirname $file)
    expected_tag=$(scripts/helper.sh $dirpath --path-version)
    version=$(scripts/helper.sh $dirpath)
    # Check if the tag already exists
    if git rev-parse --verify $expected_tag^{tag} &> /dev/null; then
        echo "Tag '$expected_tag' already exists."
    else
        # Tag doesn't exist. Create tag and build/publish to PyPi
        echo "Tag '$expected_tag' does not exist. Creating new tag to trigger release."
        git tag -a $expected_tag -m "Release $version"
        git push origin tag $expected_tag
        cd $dirpath
        poetry publish --build --username="__token__" --no-interaction --password="$PYPI_TOKEN"
        cd $GITHUB_WORKSPACE
    fi              
done
