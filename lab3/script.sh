# grep

## 10 unique addresses
cat access_log | grep -o "^[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*" | sort -u | head -10

## requests with 'denied' in link
cat access_log | grep "/denied"

## requests send from 64.242.88.10
cat access_log | grep "^64\.242\.88\.10\s"

## requests send from FQDN
cat access_log | grep -E "^[^ ]*\.[^ ]*\.[a-z]{2,3}\s"


# cut + grep

## only people with odd id
cat yolo.csv | grep -E "^[0-9]*[13579]," | cut -f 1,2,3 -d "," --output-delimiter=" " >&2

## first_name of everyone who is worth $2.99, $5.99 or $9.99
cat yolo.csv | grep "\$[259]\.99[MB]$" | cut -f 2 -d ","


# sed

## replace $HEADER$ with /temat/ in all files in groovies directory
find groovies -type f -exec sed -i 's/\$HEADER\$/\/temat\//g' {} \;

## add "String marker = '/!@$%/'" to each class
find groovies/ -type f -exec sed -E -i "/^class/a String marker = '\/\!@\$%\/'" {} \;


# >, >> 2> + grep + /dev/null + tee

## save lines with '.conf' at the end to find_results.log and errors to errors.log
./fakaping.sh 2> errors.log | grep "\.conf$" | tee find_results.log

## redirect stdout to nothing and sort stderr
./fakaping.sh 2>&1 1>/dev/null | sort

## display and save to denied.log all errors that contains 'permission denied', ignose case matching
./fakaping.sh 2>&1 1>/dev/null | grep -i "permission denied" | sort -u | tee denied.log
