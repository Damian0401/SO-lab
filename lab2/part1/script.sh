#!/bin/bash -eu

FIRST_DIR=${1}
SECOND_DIR=${2}

if [ ! -d ${FIRST_DIR} ] && [ ! -d ${SECOND_DIR} ]; then
    echo "Error"
    exit 1
fi

for ITEM in ${FIRST_DIR}/*; do
    
    FILE_NAME=${ITEM##*/}
    UPPER_CASE=$(echo ${FILE_NAME} | tr '[:lower:]' '[:upper:]')

    if [[ -L ${ITEM} ]]; then
        echo "${ITEM} is a link"
    elif [[ -f ${ITEM} ]]; then
        echo "${ITEM} is a file"
    elif [[ -d ${ITEM} ]]; then
        echo "${ITEM} is a directory"
    fi

    if [[ ! -L ${ITEM} ]]; then
        ln -s ${ITEM} ${SECOND_DIR}/${UPPER_CASE}_ln
    fi

done