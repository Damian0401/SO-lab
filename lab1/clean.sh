#!/bin/bash

SOURCE_DIR=${1:-lab_uno}
RM_LIST=${2:-2remove}
TARGET_DIR=${3:-bakap}

mkdir ${SOURCE_DIR}
mkdir ${SOURCE_DIR}/sample1
mkdir ${SOURCE_DIR}/sample2

touch ${SOURCE_DIR}/test1
touch ${SOURCE_DIR}/test2
touch ${SOURCE_DIR}/test3
touch ${SOURCE_DIR}/sample1/test4
touch ${SOURCE_DIR}/sample2/test5
touch ${SOURCE_DIR}/test6
touch ${SOURCE_DIR}/test7
touch ${SOURCE_DIR}/test8

rm *.zip

echo -e "test1\ntest2\ntest3" > ${RM_LIST}