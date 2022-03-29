# introduction
It has a set of commands that copies paste-ready markdown(or HTML) texts into clipboard for use in zendesk.

* The script must get the correct template listed under keyword

* The script must support copying the correct


What will be in the clipboard? Likely the username since it gets copy pasted the most.
Or will the ticket ask for the username with needUsername() and needAmount() - if so amount probably can be entered at a later date.
Need to carefully consider the UX of how I am gonna use the script itself - or what will be maximum useful for me so that the code itself is useful for me, and that I don't waste time when I am coding.

Usecases:
>> that I don't have to look at or search the templates separately and can get stuff via keyword (eg. zdt.py )



# usage
**python3 zd_templator.py list [l(optional)];**
lists all available keywords and content template in a pretty format.
l is optional for verbose mode, to print out the contents of the file as well


python3 zd_templator.py get [keyword] [var (optional)]
python3 zd_templator.py add [keyword]
python3 zd_templator.py del [keyword]



# architecture


