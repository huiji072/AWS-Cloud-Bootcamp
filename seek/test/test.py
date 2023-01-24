data = ['3.6', '188 reviews', 'Sydney NSW', 'Administrative Assistants (Administration & Office Support)', 'Full time']

for d in data:
    if(d >= '0' and d <= '9') and 'review' in d:
        print(d)

