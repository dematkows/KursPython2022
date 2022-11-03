# 1
items = ['tent', 'money', 'bag']
with open('save.txt', mode='w') as f:
    for i in items:
        f.write(str(i) + '\n')

# 2
with open('save.txt', mode='w') as f:
    f.write('\t'.join(items))
