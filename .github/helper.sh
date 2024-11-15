#!/bin/bash

# Check if the directory is provided as an argument
if [ $# -lt 1 ] || [ $# -gt 2 ]; then
  echo "Usage: $0 <directory> [option]"
  echo "Options:"
  echo "  -v | --version      Print just the version number"
  echo "  -p | --path-version Print the concatenation of the path and the version"
  exit 1
fi

# Check if the directory exists
if [ ! -d "$1" ]; then
  echo "Directory '$1' does not exist"
  exit 1
fi

# Append a trailing slash to the path if it's not already present
if [ "${1: -1}" != "/" ]; then
  path="$1/"
else
  path="$1"
fi

# Change into the directory and run the command
cd "$path" || exit 1
version=$(poetry version)

# Get the version number
version_number="${version##* }"

# Get the path and version string
path_version="$path$version_number"

# Handle options
if [ $# -eq 1 ]; then
  # Default behavior: print just the version number
  echo "$version_number"
elif [ "$2" = "-v" ] || [ "$2" = "--version" ]; then
  # Print just the version number
  echo "$version_number"
elif [ "$2" = "-p" ] || [ "$2" = "--path-version" ]; then
  # Print the concatenation of the path and the version
  echo "$path_version"
else
  echo "Invalid option: '$2'"
  exit 1
fi