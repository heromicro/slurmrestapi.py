#!/bin/bash

openapi-generator generate -i spec/openapi.25.11.3.json  -g python --package-name slurmrestapi -o ./
