def count_substring(string, sub_string):
    c=0
    
    for i in range (0,len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            c=c+1
    return c
    