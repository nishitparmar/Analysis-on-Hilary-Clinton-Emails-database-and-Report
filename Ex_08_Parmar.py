'''Author : Nishit Parmar
CWID: 10432431
Exercise 09
'''

import pandas as pd
#from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt

Headers = ['Id', 'DocNumber', 'MetadataSubject','MetadataTo','MetadataFrom', 'SenderPersonId','MetadataDateSent',\
        'MetadataDateReleased',	'MetadataPdfLink', 'MetadataCaseNumber', 'MetadataDocumentClass', 'ExtractedSubject',\
        'ExtractedTo', 'ExtractedFrom', 'ExtractedCc', 'ExtractedDateSent', 'ExtractedCaseNumber','ExtractedDocNumber',\
        'ExtractedDateReleased', 'ExtractedReleaseInPartOrFull', 'ExtractedBodyText', 'RawText']

file = pd.read_table('H_Clinton-emails.csv',engine='python',sep=',', header=None, names=Headers)

del file ['Id']

del file ['DocNumber']

del file ['MetadataSubject']

del file ['MetadataTo']

del file ['MetadataDateSent']

del file ['MetadataDateReleased']

del file ['MetadataPdfLink']

del file ['MetadataCaseNumber']

del file ['MetadataDocumentClass']

del file ['ExtractedSubject']

del file ['ExtractedTo']

del file ['ExtractedFrom']

del file ['ExtractedCc']

del file ['ExtractedDateSent']

del file ['ExtractedCaseNumber']

del file ['ExtractedDateReleased']

del file ['ExtractedBodyText']

del file ['ExtractedReleaseInPartOrFull']

del file ['ExtractedDocNumber']

count=[]
for i in range(len(file)):
    count.append(1)
file['count'] = count
sender= file.groupby('SenderPersonId').agg({'MetadataFrom': ['first', 'last'], 'count': 'sum'})
sorted1 = sender.sort_values([('count','sum')],ascending=False)
sendersize = sender.shape

print 'The top 15 senders are ::'
print
print '   Total no. of emails sent  |    Name of the sender: ' 
print
for row in range(15):
     print'    ',(sorted1.iloc[row,0]),'mails -',(sorted1.iloc[row,1]),'   -   ',(sorted1.iloc[row,2])
print
print 'A total of ',sendersize[0],' senders were traced.'
file_stop = open('stopwords_en (1).txt','r')
sw = []
for i in file_stop:
    sw.append( i.strip())

#Additional stopwords.
sw.append('h')
sw.append('pm')
sw.append('d')
sw.append('j')
sw.append('new')
sw.append('said')
sw.append('just')
size= file.shape
a=[]
b=[]
clean=[]
for index, row in file.iterrows():
     a.append(row['RawText'].strip().split())
for part in a:
    for words in part:    
        if words.isalpha():
            b.append(words)
        else:
            continue
for words in b:
    words.strip()
    if words.lower() not in sw:
        clean.append(words.lower())        
top20 = Counter(clean).most_common(20)
print 
print 'The top 20 words from emails content:'
for max in top20: 
    print max[0], ' - ',max[1],'times'
print
print ' Number of emails analyzed are :  ',size[0]

names = ['Hillary Clinton','Huma Abendin','Cheryl Mills','Jacob Sullivan','Sidney Blumental',\
        'Lauren Jilloty','Philippe Reines','Lona ValMoro','Ann-Marie Slaughter','Richard Verma','Melanne Verveer','Lissa Muscatine',\
         'Judith McHale',' Strobe Talbott','Betsy Ebeling','Others (160 senders)']
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
count_sum=[]
for index, row in sorted1.iterrows():
     count_sum.append(row[('count','sum')])

y_bar = count_sum[:15]

plt.figure(1)
plt.subplot(2,2,1)
plt.bar(x,y_bar)
plt.title('Top 15 senders')

plt.xticks(x,names,rotation = 'vertical')

plt.ylabel('Number of emails ')

for i in range(len(y_bar)):
    plt.text(x = x[i]-0.4 , y = y_bar[i]+0.3,s = y_bar[i], size = 9)

'''    
text1 = ' '.join(clean)

wc = WordCloud(background_color = 'white', max_words=1000)

wc.generate(text1)

wc.to_file('emails.png')

plt.figure(2)
plt.imshow(wc)
plt.axis('off')
'''
plt.show()
