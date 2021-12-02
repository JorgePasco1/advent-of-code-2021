#!/bin/bash
exercise_number=$1
exercise_name=$2

if test -z "$exercise_number" || test -z "$exercise_name"
then
  echo "Usage: $0 <exercise_number> <exercise_name>"
  exit 1
fi

if (( $exercise_number < 11 ));
then
  parent_dir="01-10"
  exercise_number="0$exercise_number"
elif (( $exercise_number < 21 ));
then
  parent_dir="11-20"
else
  parent_dir="21-31"
fi

mkdir -p $parent_dir/$exercise_number-$exercise_name
touch $parent_dir/$exercise_number-$exercise_name/README.md
touch $parent_dir/$exercise_number-$exercise_name/input.txt
cp ./skeleton.py $parent_dir/$exercise_number-$exercise_name/main.py
