#!/bin/bash

SOURCE_DIR=${1:-lab_uno}
RM_LIST=${2:-2remove}
TARGET_DIR=${3:-bakap}

if [[ ! -d ${TARGET_DIR} ]]; then
    mkdir ${TARGET_DIR}
fi

FILES_TO_REMOVE=$(cat ${RM_LIST})

for ITEM in ${FILES_TO_REMOVE}; do

    if [[ -f ${SOURCE_DIR}/${ITEM} ]]; then
        rm -r ${SOURCE_DIR}/${ITEM}
    fi

done

for ITEM in ${SOURCE_DIR}/*; do

    if [[ -f ${ITEM} ]]; then
        mv ${ITEM} ${TARGET_DIR}
    elif [[ -d ${ITEM} ]]; then
        cp -r ${ITEM} ${TARGET_DIR}
    fi

done

COUNTER=0

for ITEM in ${SOURCE_DIR}/*; do

    COUNTER=$((COUNTER+1))

done

if [[ ${COUNTER} -gt 0 ]]; then
    echo "there's something left!"

    if [[ ${COUNTER} -ge 2 ]]; then
        echo "at least two files left"
    fi

    if [[ ${COUNTER} -gt 4 ]]; then
        echo "more than 4 files left"
    fi

    if [[ ${COUNTER} -le 4 ]] && [[ ${COUNTER} -ge 2 ]]; then
        echo "at least two files left but no more than 4"
    fi
else
    echo "someone was here"
fi