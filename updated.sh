#!/bin/bash
DATE="2\ April\ 2023"
find . -name "*.html" -type f -exec sed -i '' -e 's/^.*Last\ Update.*$/                    Last\ Update\:\ '"$DATE"'/g' {} \;