import webbrowser
import time
# user put in phone number
x = input('Enter Phone Number: ')
idnum_str = repr(x)
# newid is the new number format converted
newid = idnum_str[1:4] + "-" + idnum_str[4:7] + "-" + idnum_str[7:11]
webbrowser.open('https://www.whitepages.com/phone/'+''.join([x]))
time.sleep(5)
webbrowser.open_new_tab('https://www.fastpeoplesearch.com/'+''.join([newid]))
time.sleep(5)
webbrowser.open_new_tab('https://www.zabasearch.com/phone/'+''.join([x]))
time.sleep(5)
webbrowser.open_new_tab('https://www.peoplefinder.com/reverse-phone-search/'+''.join([x]))
time.sleep(5)
webbrowser.open_new_tab('https://www.spokeo.com/'+''.join([x]))
time.sleep(5)
webbrowser.open_new_tab('https://www.spytox.com/people/search?phone='+''.join([newid]))
# more website to add
