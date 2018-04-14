import numpy as np
import sys

def learn_alpha_beta(test_line,pai,a,b,index_tags,index_words):
    alphas = np.array([[0.0 for j in range(len(index_tags))]for i in range(len(test_line))])
    betas = np.array([[0.0 for j in range(len(index_tags))]for i in range(len(test_line))])
    index = 0
    for item in test_line:
        item = item.strip('\n')
        l = item.split('_')
        word = l[0]
        tag = l[1]
        i_word = index_words.index(word)
        print(i_word)
        i_tag = index_tags.index(tag)
        if index == 0:
            alphas[index] = b[:,i_word] * pai
            print( b[:,i_word] * pai)
        else:
            alphas[index] = b[:,i_word] * (np.dot(a.T,alphas[index - 1]))
            #print(np.dot(a.T,alphas[index - 1]))
        index = index + 1    
    #print(alphas)
    index = len(betas) - 1
    
    while index  >= 0:   
        if index == len(betas) - 1:
            betas[index] = np.array([1.0 for i in range(len(betas[0]))])
        else:
            term = test_line[index + 1].strip('\n')
        #print(term)
            l = term.split('_')
            word = l[0]
            tag = l[1]
            #print('word and tag are', word, tag)
            i_word = index_words.index(word)
            # i_tag = index_tags.index(tag)
            #print('i_word and i_tag are', i_word, i_tag)
            #print('b is', b)
            #print('ith word is', i_word)
            #print('b[i] is',b[:,i_word])
            # print('index is',index)
            betas[index] = np.dot(a , b[:,i_word]* betas[index + 1])
        index = index - 1
   
    #print(betas)
    return alphas,betas

def predict_file(infile,outfile,pai,a,b,index_tags,index_words):
    f_in = open(infile,'r')
    f_out = open(outfile,'w')
    for test_line in f_in:
        test_line = test_line.strip('\n').split(' ')
        #print('the test line is',test_line)
        alphas,betas = learn_alpha_beta(test_line,pai,a,b,index_tags,index_words)
        index = 0
        for item in test_line:
            word = item.split('_')[0]
            P = alphas[index] * betas[index]
            P = list(P)
            i = P.index(max(P))
            print('i is',i)
            print('P is',P)
            f_out.write(word + '_' + index_tags[i] + ' ')
            index = index + 1  
        f_out.write('\n')    
    f_in.close()
    f_out.close()
'''    
test_line = np.array(['fish_B','you_A','eat_A'] )
index_tags = ['A','B']
index_words = ['you','eat','fish']  
pai = np.array([4/5,1/5])
a = np.array([[1/3,2/3],[2/3,1/3]])
b = np.array([[1/2,3/8,1/8],[1/6,1/6,2/3]])
learn_alpha_beta(test_line,pai,a,b,index_tags,index_words)  
predict_file('toytest_re.txt','predict_output_re.txt',pai,a,b,index_tags,index_words) 

'''
if __name__== "__main__":
    
    test_input = sys.argv[1]
    index_to_word = sys.argv[2]
    index_to_tag = sys.argv[3]
    hmm_prior = sys.argv[4]
    hmm_emit = sys.argv[5]
    hmm_trans = sys.argv[6]
    predicted_file = sys.argv[7]
    
    #f_hmm_prior = open(hmm_prior,'r')
    #prior = f_hmm_prior.readlines()
    
    
    pai = np.loadtxt(hmm_prior,dtype = float)
    a = np.loadtxt(hmm_emit,dtype = float)
    b = np.loadtxt(hmm_trans,dtype = float)
    
    print(pai,a)
    
    f_in_word = open(index_to_word,'r').readlines()
    f_in_tag = open(index_to_tag,'r').readlines()
    index_words = []
    for i in f_in_word:
        i = i.strip('\n')
        index_words.append(i)
    index_tags = []
    for j in f_in_tag:
        j = j.strip()
        index_tags.append(j)
    
    predict_file(test_input,predicted_file,pai,a,b,index_tags,index_words)    
    #print(index_words,index_tags)
    