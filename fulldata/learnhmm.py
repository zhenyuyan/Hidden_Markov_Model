import numpy as np
import sys
import copy
def split_xy(f_lines):
    new_f_lines = []
    for row in f_lines:
        new_f_lines.append(row.strip('\n').split(' '))
    #print(new_f_lines)
    X,Y = copy.deepcopy(new_f_lines), copy.deepcopy(new_f_lines)
    rnum = 0
    for row in new_f_lines:
       for j in range(len(row)):
           word,tag = row[j].split('_')[0],row[j].split('_')[1]
           X[rnum][j] = word
           Y[rnum][j] = tag
       rnum = rnum + 1    
    return X, Y

def constru_pai_a(tag_lines,Y):
    tag_matri = [0.0 for i in range(len(tag_lines))]
    
    for t in range(len(tag_lines)):
        tag_matri[t] = tag_lines[t].strip('\n')
    #print(tag_matri)    
    pai = np.array([ 0.0 for i in range(len(tag_lines))])
    pai_1 = np.array([ 1.0 for i in range(len(tag_lines))])
    a = np.array([[ 0.0 for i in range(len(tag_lines))]for i in range(len(tag_lines))])
    a_1 = np.array([[ 1.0 for i in range(len(tag_lines))]for i in range(len(tag_lines))])
    for row in Y:
        pai[tag_matri.index(row[0])] =  pai[tag_matri.index(row[0])] + 1
        
        for t in range(len(row)):
            #y = row[t]
            i,j = 0, 0
            y_pre = row[t - 1]
            y = row[t]
            for index in range(len(tag_matri)):
                #print('index is', index)
                if tag_matri[index] == y:
                    j = index
                    #print('j is ', j)
                            
                    if t > 0:
                        for index1 in range(len(tag_matri)):
                            if y_pre == tag_matri[index1]:
                                #print('y_pre is', y_pre)
                                i = index1
                                #print('i is ', i)
                        a[i][j] = a[i][j] + 1          
                #print(a) 
    pai = pai + pai_1
    s_pai = sum(pai)
    pai = pai/s_pai
    a = a + a_1
    #print(a)
    for i in range(len(a)):
        srow = sum(a[i])
        #print(srow)
        for j in range(len(a[i])):
              a[i][j] = float(a[i][j])/float(srow)
              
    return pai,a
    
def constru_b(tag_lines,word_lines,X,Y):
    for i in range(len(tag_lines)):
        tag_lines[i] = tag_lines[i].strip('\n')
    
    for i in range(len(word_lines)):
       #for j in range(len(word_lines[i])):
        word_lines[i] = word_lines[i].strip('\n')
        
    #print(tag_lines,word_lines)
    b = np.array([[0.0 for i in range(len(word_lines)) ] for j in range(len(tag_lines))])
    b_1 = np.array([[1.0 for i in range(len(word_lines)) ] for j in range(len(tag_lines))])
    for i in range(len(X)):
        for j in range(len(X[i])):
            m,n = 0,0
            for i_0 in range(len(tag_lines)):
                if tag_lines[i_0] == Y[i][j]:
                    #print('Y[i][j] is',Y[i][j])
                    m = i_0
                    for j_0 in range(len(word_lines)):
                        if word_lines[j_0] == X[i][j]:
                            n = j_0
                            #print('j is',j_0)
            b[m][n] =  b[m][n] + 1
    b = b + b_1
    nrow = 0
    for row in b:
        b[nrow] = b[nrow]/sum(row)
        nrow = nrow + 1
    return b              
                    
            

if __name__== "__main__":
    tr_input = sys.argv[1]
    index_word = sys.argv[2]
    index_tag = sys.argv[3]
    hmm_prior = sys.argv[4]
    hmm_emit = sys.argv[5]
    hmm_tran = sys.argv[6]
    
    
    f_index_tag = open(index_tag)
    f_index_word = open(index_word)
    f_train = open(tr_input)
    f_tr = f_train.readlines()
    
    tag_lines = f_index_tag.readlines()
    word_lines = f_index_word.readlines()
    X, Y = split_xy(f_tr)
    
    pai,a = constru_pai_a(tag_lines,Y)
    b = constru_b(tag_lines,word_lines,X,Y)
    
    f_hmm_prior = open(hmm_prior,'w')
    f_hmm_emit = open(hmm_emit,'w')
    f_hmm_tran = open(hmm_tran,'w')
    
    for line in pai:
        f_hmm_prior.write(str(line))
        f_hmm_prior.write('\n')    
    
    for line in a:     
        for w in range(len(line)):
            if w != len(line) - 1:
                f_hmm_emit.write(str(line[w]) + ' ')
            else:
                f_hmm_emit.write(str(line[w]))
        f_hmm_emit.write('\n')
        
    for line in b:
        for w in range(len(line)):
            if w != len(line) - 1:
                f_hmm_tran.write(str(line[w]) + ' ')
            else:
                f_hmm_tran.write(str(line[w]))
        f_hmm_tran.write('\n')
    f_index_tag.close()
    f_index_word.close()
    f_train.close()
    f_hmm_prior.close()
    f_hmm_emit.close()
    f_hmm_tran.close()
    