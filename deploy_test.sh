#!/bin/bash

CIRCUITPY_LOCATION=$1

cp code/envmon.py $CIRCUITPY_LOCATION/.
cp code/envmon_tests.py $CIRCUITPY_LOCATION/.
cp code/report.py $CIRCUITPY_LOCATION/.
cp code/report_tests.py $CIRCUITPY_LOCATION/.
cp code/test_main.py $CIRCUITPY_LOCATION/code.py
