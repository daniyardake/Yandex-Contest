# -*- coding: utf-8 -*-

#%%

infilename = 'input.txt'
outfilename = 'output.txt'
infile = open(infilename)
outfile = open(outfilename, 'w')

linenum = 0
numbers = []
patterns = []
N = M = 1000
for line in infile:
    line = line.rstrip("\r\n")
    if linenum == 0:
        N = int(line)
    elif linenum <= N:
        numbers.append(line)
    elif linenum == N + 1:
        M = int(line)
    else:
        patterns.append(line)
        
    if linenum > N + M:
        break
    linenum += 1

formatted = []
skip_symbols = ['+', ' ', '(', ')', '-']
for num in numbers:
    for sample in patterns:
        i = j = 0
        while i < len(num) and j < len(sample):
            if sample[j:j+2] == " -":
                break
            if num[i] in skip_symbols:
                i += 1
                continue
            if sample[j] in skip_symbols:
                j += 1
                continue
            if sample[j] == 'X':
                pass
            elif num[i] != sample[j]:
                break
            i += 1
            j += 1
        
        candidate = ''
        if i == len(num) and sample[j:j+2] == " -":
            i = j = 0
            while i < len(num) and j < len(sample):
                if num[i] in skip_symbols:
                    i += 1
                    continue
                if sample[j] in skip_symbols:
                    candidate += sample[j]
                    j += 1
                    continue
                if sample[j] == 'X':
                    candidate += num[i]
                else:
                    candidate += sample[j]
                i += 1
                j += 1
            
            candidate += sample[j:len(sample)]
            formatted.append(candidate)
            break
    
for num in formatted:
    outfile.write(num + '\n')

outfile.close()
infile.close()

#%%
