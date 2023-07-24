# from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# class newslabel:
#     def __init__(self, newsDf):
#         self.newsDf = newsDf
#         self.score = 0

#     def labeling_article(self):
#         if self.newsDf.shape[0] == 0:
#             return self.score
#         else:
#             list_text = self.newsDf['content'].tolist()

#             tokenizer = AutoTokenizer.from_pretrained('snunlp/KR-FinBert-SC')
#             model = AutoModelForSequenceClassification.from_pretrained('snunlp/KR-FinBert-SC')
#             senti_classifier = pipeline(task='text-classification', model=model, tokenizer=tokenizer)

#             # neutral 중립, positive 긍정, negative 부정

#             for text in list_text:
#                 if len(text) < 512:
#                     if senti_classifier(text)[0]['label'] == 'positive':
#                         self.score += 1
#                     elif senti_classifier(text)[0]['label'] == 'negative':
#                         self.score -= 1
#                     else:
#                         pass

#             return self.score 
