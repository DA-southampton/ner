fr = open("train_data.json",'r')  
file_1=open('ori_train.txt','w')
file_2=open('tag_train.txt','w')
lines=fr.readlines() 
for line in lines:
    line=eval(line)  
    text=line['text']
    text_all=[]
    for te in text:
        text_all.append(te)
    text_all_input=' '.join(text_all)
    
    postag=line['postag']
    if len(postag)>0:
        tags=[]
        for ele in postag:
            word=ele['word']
            pos=ele['pos']
            if pos=='nr':
                pos='PER'
            elif pos=='ns':
                pos='LOC'
            elif pos=='t':
                pos='T'
            elif pos=='nt':
                pos='ORG'
            else:
                pos='O'

            pos_all=[pos]*len(word)
            
            if len(pos_all)>1:
                if pos_all[0]!='O':
                    head_label ='B'+'_'+pos_all[0]
                    tags.extend([head_label])
                    tags.extend(["I_"+pos_all[0]] * (len(pos_all) - 1))
                else:
                    tags.extend(["O"]* (len(pos_all)))
            else:
                if pos_all[0]!='O':
                    tags.append('S-'+pos_all[0])
                else:
                    tags.append(pos_all[0])

            
        tag_all_input=' '.join(tags) 
        try:
            assert len(tags)==len(text_all)
            file_1.write(text_all_input+'\n')
            file_2.write(tag_all_input+'\n')
        except:
            print('error',text_all_input,tag_all_input)
        

file_1.close()
file_2.close()
