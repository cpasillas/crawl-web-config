#!/bin/sh

DATA_ROOT={{data_root}}

RCDIR=$DATA_ROOT/rcs

RCDIR_TK=$RCDIR/turkey-0.20
INPROGRESSDIR_TK=$RCDIR_TK/running
TTYRECDIR_TK=$RCDIR_TK/ttyrecs/$1
DEFAULT_RC=../settings/init.txt
PLAYERNAME=$1

echo MAKING RCDIR
mkdir -p $RCDIR_TK

echo MAKING PROGRESS DIR
mkdir -p $INPROGRESSDIR_TK

echo MAKING TTYREC DIR
mkdir -p $TTYRECDIR_TK

if [ ! -f ${RCDIR}/${PLAYERNAME}.rc ]; then
    cp ${DEFAULT_RC} ${RCDIR}/${PLAYERNAME}.rc
fi
