#!/bin/bash  -eu

DIR=${1:-source}

for ITEM in ${DIR}/*; do

    if [[ -f ${ITEM} ]] && [[ ${ITEM} == *.bak ]]; then
        chmod uo-w ${ITEM}
    elif [[ -d ${ITEM} ]] && [[ ${ITEM} == *.bak ]]; then
        chmod a-x ${ITEM}
        chmod o+x ${ITEM}
    elif [[ -d ${ITEM} ]] && [[ ${ITEM} == *.tmp ]]; then
        chmod a-rw
        chmod u+r
        chmod g+w
        chmod o+e
    elif [[ -f ${ITEM} ]] && [[ ${ITEM} == *.txt ]]; then
        chmod a-rwe
        chmod u+r
        chmod g+w
        chmod o+e
    fi

done