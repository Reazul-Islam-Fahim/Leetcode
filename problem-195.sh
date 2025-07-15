#solution 1
sed -n '10p' file.txt


#solution 2
awk 'NR==10' file.txt

