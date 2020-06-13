import json
import csv
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, CategoriesOptions, ConceptsOptions, EmotionOptions, RelationsOptions, SemanticRolesOptions, SentimentOptions

authenticator = IAMAuthenticator('mKzR3k6BF2W3tMUmoX3_Xvxze4LL0-f_q8FM5QMsFIFY')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)
from ibm_watson import IAMTokenManager

iam_token_manager = IAMTokenManager(apikey='mKzR3k6BF2W3tMUmoX3_Xvxze4LL0-f_q8FM5QMsFIFY')
token = iam_token_manager.get_token()

from ibm_cloud_sdk_core.authenticators import BearerTokenAuthenticator

# in the constructor, assuming control of managing the token
authenticator1 = BearerTokenAuthenticator(token)
natural_language_understanding1 = NaturalLanguageUnderstandingV1(version='2019-07-12',
                        authenticator=authenticator1)
f_name = input("enter file in csv format")
x = 0
intext = []
with open("C:\\Users\\HP\\Desktop\\"+f_name+".csv") as file:
    data = list(csv.reader(file))
#print(type(data[0]))
strin = " ".join(str(x) for x in data)
#print(type(strin))
#print(file)
natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/c70c1850-5873-495c-b449-d84d30415f06')
natural_language_understanding.set_disable_ssl_verification(True)
response = natural_language_understanding.analyze(
    text=strin,
    features=Features(
        categories=CategoriesOptions(limit=3),
        )).get_result()
#d = dict.items(response.catego)
#print(d)

cat1 = response['categories']
#get('score')
#.get('label')
#print(cat1)
di1 = cat1[0]
di2 = cat1[1]
di3 = cat1[2]
#print(di1, di2, di3)
#print(di1['score'], di1['label'])


with open('C:\\Users\\HP\\Desktop\\catop.csv', 'a', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow([f_name,di1['score'], di1['label']])
    writer.writerow([f_name, di2['score'], di2['label']])
    writer.writerow([f_name, di3['score'], di3['label']])


#print(json.dumps(response, indent=2))