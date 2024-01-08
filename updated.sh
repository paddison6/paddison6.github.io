#!/bin/bash
DATE="8 January 2024"
find . -name "*.html" -type f -exec sed -i '' -e 's/^.*Last\ Update.*$/                    Last\ Update\:\ '"$DATE"'/g' {} \;