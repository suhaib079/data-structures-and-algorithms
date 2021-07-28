def left_join(synonym,antonym):
    result = []
    for key in synonym.keys():
       if key in antonym.keys():
           result.append([key,synonym[key],antonym[key]])
       else:
           result.append([key,synonym[key],'NULL'])
    return result

dictionary1 = {'fond':'enamored','wrath':'anger','diligent':'employed','outfit':'garb','guide':'usher','suhaib':'abdennabi'}
dictionary2 = {'fond':'averse','wrath':'delight','diligent':'idle','guide':'follow','flow':'jam'}

print(left_join(dictionary1,dictionary2))