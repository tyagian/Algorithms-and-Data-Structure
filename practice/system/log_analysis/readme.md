
#How to run:

| $python <filename> <start-time> <end-time>

# output
```
python3 log_analysis.py logs.txt 1493969101.638 1493969101.667
Between time 1493969101.638  &  1493969101.667 :
player.vimeo.com returned 0.35% of 5xx errors
vimeo.com returned 0.38% of 5xx errors
```

```
Time Complexity: O(n), linear
1. We can improve performance if old logs are saving in subdirectories name with date, month or year using os.walk('<directory_path>')
2. If we know log files have timestamp in sorted order then we can break the for loop when range of timestamp is greater than range. 
 ```