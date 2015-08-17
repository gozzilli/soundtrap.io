#!/bin/bash

CONVERT = /usr/local/bin/convert
KEW_IN  = kew-white.gif
KEW_OUT = kew-white.mod.png

OXF_IN  = oxford-white.png
OXF_OUT = oxford-white.mod.png

DEST_SIZE = x60

all: kew oxf

kew:
	${CONVERT} ${KEW_IN} \
		-transparent white \
		-negate \
		-resize x70 \
        -bordercolor none \
		-border 40x20 \
		-resize ${DEST_SIZE} \
		${KEW_OUT}
	
oxf:
	${CONVERT} ${OXF_IN} \
    		-negate \
		-transparent black \
		-resize x70 \
        -bordercolor none \
		-border 10x5 \
		-resize ${DEST_SIZE} \
		${OXF_OUT}

# -bordercolor none -border 4x3 \