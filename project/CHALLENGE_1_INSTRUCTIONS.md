# Using the challenge 1 shell script
### Usage
when running 

        $ bash challenge-1.sh <PHONE_NUMBER> <PATH_TO_FILE>

it will return cost of call by finding data with matching prefix (longest matching prefix).

### Paramenters 

- PHONE_NUMBER is any valid phone number with no special characters separating numbers. SHOULD contain '+' at start of phone number.
- PATH_TO_FILE is a path to data file with phone number prefix, cost data.
    - For example, when in the project/ directory the path to file would be:

        
        ```../data/route-costs-4.txt```

### Example
An example usage of the command when in the project/ directory:

        $ bash challenge-1.sh +1415234 ../data/route-costs-4.txt
            > +1415234,0.03 // returns phone number prefix, cost (key,value)


