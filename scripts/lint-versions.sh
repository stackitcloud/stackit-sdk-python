#!/usr/bin/env bash

# Immediate exit on failure
set -e

echo ">> Linting SDK module versions..."

# Check all pyproject.toml files 
for file in $(find . -print | sed 's|^./||' | grep -E "(^services/[^/]+/pyproject.toml$|^core/pyproject.toml$)"); do
    # Extract the current version 
    dirpath=$(dirname "$file")
    version=$(scripts/helper.sh "$dirpath")

    # skip iaasalpha
    case "$dirpath" in
        "services/iaasalpha")
            continue
            ;;
    esac

    # special handling for CDN (is in v2 by accident)
    if [[ "$dirpath" == "services/cdn" ]]; then
        if [[ ! "$version" =~ ^v?[0-2]\.[0-9]+\.[0-9]+$ ]]; then
            echo ">> $dirpath"
            echo "The version '$version' is invalid."
            exit 1
        fi
        continue
    fi

    # verify version
    if [[ ! "$version" =~ ^v?[0-1]\.[0-9]+\.[0-9]+$ ]]; then
        echo ">> $dirpath"
        echo "The version '$version' is invalid."
        exit 1
    fi
done
