months = input('Enter months: ')
#if months == 'September' or months =='October' or months =='November':
#    print('The season is Autumn')
if months in ['September','October','November']:
    print('The season is Autumn')
elif months in ['December', 'January','February']:
    print('The season is Winter')
elif months in ['March', 'April', 'May']:
    print('The season is Spring')
elif months in ['June','Juli','August'] :
    print('The season is Summer')