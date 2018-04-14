# Hidden_Markov_Model
This is a HMM model for labeling tags for natural language processing. We are using forward-backward algorithm for decoding. Follow the following procedure to run the code and check the result.
1. Open learnhmm.py, open a terminal
2. Try the learg data set. Drag out the data in 'fulldata' file. Type in command line: $python learnhmm.py trainwords.txt index_to_word.txt index_to_tag.txt hmmprior.txt hmmemit.txt hmmtrans.txt. Result of prior matrix, emition probability matrix, transition probability matrix will be shown in hmmprior.txt hmmemit.txt hmmtrans.txt.
3. Use forward-backward algorithm for decoding the test data set. Type in command line: $python forwardbackward.py testwords.txt index_to_word.txt index_to_tag.txt hmmprior.txt hmmemit.txt hmmtrans.txt predict_output.txt. Result of prediction will be shown in predict_output.txt. It may take several minutes to run the code.
4. You can also play with the toy data set.
