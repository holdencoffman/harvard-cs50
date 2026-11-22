import emoji as em

response = input('Please list your input below to be emojized:\n')
print(em.emojize(response, language='alias'))