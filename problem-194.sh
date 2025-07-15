#solution 1
awk '
{
  for (i=1; i<=NF; i++)  {
    a[i, NR] = $i
  }
  max_cols = NF
  max_rows = NR
}
END {
  for (i=1; i<=max_cols; i++) {
    for (j=1; j<=max_rows; j++) {
      printf "%s%s", a[i,j], (j==max_rows ? "\n" : " ")
    }
  }
}
' file.txt


#solution 2
awk '{for(i=1;i<=NF;i++)a[i,NR]=$i;maxc=NF;maxr=NR} END{for(i=1;i<=maxc;i++){for(j=1;j<=maxr;j++){printf "%s%s",a[i,j],(j<maxr?OFS:ORS)}}}' file.txt
