#!/bin/bash
curl --silent --location --output - https://raw.githubusercontent.com/PurpleBooth/change-github-default-branch.sh/main/change-github-default-branch.sh | \
    bash -s -- \
    -t ca843b9a9b8904b5bd9a2f17309a85bdd6282d8a -d main iancleary/spa-fastrf
