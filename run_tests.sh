#!/usr/bin/env bash
set +x
echo "Running a set of example commands to test the script";

DIDFAIL=0

python3 test18.py
retVal=$?
if [ $retVal -ne 0 ]; then
    DIDFAIL = $retVal
    echo "Error"
fi

python3 18daycycle.py 1988-02-02
retVal=$?
if [ $retVal -ne 0 ]; then
    DIDFAIL = $retVal
    echo "Error"
fi


python3 18daycycle.py 1988-02-02 debug
retVal=$?
if [ $retVal -ne 0 ]; then
    DIDFAIL = $retVal
    echo "Error"
fi


python3 18daycycle.py 1943-07-16 json
retVal=$?
if [ $retVal -ne 0 ]; then
    DIDFAIL = $retVal
    echo "Error"
fi


python3 18daycycle.py help
retVal=$?
if [ $retVal -ne 0 ]; then
    DIDFAIL = $retVal
    echo "Error"
fi


python3 18daycycle.py 1943-07-16
retVal=$?
if [ $retVal -ne 0 ]; then
    DIDFAIL = $retVal
    echo "Error"
fi

if [ $DIDFAIL -ne 0 ]; then
    echo "An error occurred, something is broken."
else
    echo "Tests complete. Everything working."
fi
