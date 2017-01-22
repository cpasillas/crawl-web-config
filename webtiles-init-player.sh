#!/bin/sh

RCDIR_T=/data/rcs/trunk
RCDIR_19=/data/rcs/0.19
INPROGRESSDIR_T=$RCDIR_T/running
INPROGRESSDIR_19=$RCDIR_19/running
TTYRECDIR_T=$RCDIR_T/ttyrecs/$1
TTYRECDIR_19=$RCDIR_19/ttyrecs/$1
DEFAULT_RC=../settings/init.txt
PLAYERNAME=$1

mkdir -p $RCDIR_T
mkdir -p $RCDIR_19
mkdir -p $INPROGRESSDIR_T
mkdir -p $INPROGRESSDIR_19
mkdir -p $TTYRECDIR_T
mkdir -p $TTYRECDIR_19

if [ ! -f ${RCDIR}/${PLAYERNAME}.rc ]; then
    cp ${DEFAULT_RC} ${RCDIR}/${PLAYERNAME}.rc
fi
