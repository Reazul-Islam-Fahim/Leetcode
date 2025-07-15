#solution 1
tr -s ' ' '\n' < words.txt | grep -v '^$' | sort | uniq -c | sort -nr | awk '{print $2, $1}'

#solution 2
tr ' ' '\n' < words.txt | awk 'NF' | sort | uniq -c | sort -nr | awk '{print $2, $1}'
