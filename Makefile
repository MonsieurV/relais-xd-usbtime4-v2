####### Constants ########

SHELL := /bin/bash
ROOT_DIR = $(realpath $(dir $(lastword $(MAKEFILE_LIST))))
UNAME = $(shell uname -s)
STATUS = ${ROOT_DIR}/bin/status.sh
STOP = ${ROOT_DIR}/bin/stop.sh
KILL = ${ROOT_DIR}/bin/kill.sh
RESTART = ${ROOT_DIR}/bin/restart.sh
PYTHONHOME ?= ${ROOT_DIR}/venv/
NVM_ENV ?= ${ROOT_DIR}/nvm/

ACTIVATE_VENV = source ${PYTHONHOME}bin/activate

NODE_VERSION = 0.10.22
ACTIVATE_NVM = source ${NVM_ENV}nvm.sh

PY_RUNNER = ${ACTIVATE_VENV} &&
NODE_RUNNER = ${ACTIVATE_NVM} &&

####### Functions ########

set-pid-by-name = /bin/bash -c "pgrep -fo $(2) > $(1)"

####### Installation ########

up: venv dependencies

install:
	${MAKE} up

venv:
	echo "Creating virtualenv..."
	(test -d ${PYTHONHOME} || virtualenv ${PYTHONHOME})
	${MAKE} activate

activate:
	${ACTIVATE_VENV}

####### Dependencies ########

dependencies:
	${PYTHONHOME}bin/pip install -r requirements.txt

####### Services ########

start:

stop:

status:

restart:
