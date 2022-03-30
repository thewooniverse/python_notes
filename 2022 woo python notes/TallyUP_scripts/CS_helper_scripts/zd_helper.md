NOTE:
OK - project unscrapped since this can still be useful for things OTHER than zendesk;

This project can be rescoped for additional file formats, for example it can be used as a helper tool for the discord bot! (to export csv or copy ready format) and for handy things like email signoffs anyway;

- tldr; it can still be used for multiformat stuff.


# introduction
It has a set of commands that copies paste-ready markdown(or HTML) texts into clipboard for use in zendesk.

* The script must get the correct template(s) listed under keyword
* The script must support copying the text into the correct in markdown that is PASTE READY into zendesk tickets.

### musings
What will be in the clipboard? Likely the username since it gets copy pasted the most.
Or will the ticket ask for the username with needUsername() and needAmount() - if so amount probably can be entered at a later date.
Need to carefully consider the UX of how I am gonna use the script itself - or what will be maximum useful for me so that the code itself is useful for me, and that I don't waste time when I am coding.
I also need to design it in such a way that it is useful for me.

I MAY want to do some OOP for this project too but needlessly complex for the script.
Eventually I can also do stuff from better touch pro.

**Usecases:**
>> that I don't have to look at or search the templates separately and can get stuff via keyword (eg. zdt.py disconnect_refund) - I could define needUsername() with regex;
>> asks to pick variations? -> need to figure out how this works, or variations can simply be syntaxical like zdt.py dcr_2. Dialogue? Syntax based?




# usage
zdt.py dcr -> lists variations, one selected -> requests username, tokens. provided -> copies paste ready markdown template that is populated.
would actually be useful to support tidbits as well like zdt.py signoff


python3 zd_templator.py list {style};
lists all available keywords and content template in a pretty format.
l is optional for verbose style, to print out the contents of the file as well

python3 zd_templator.py get [keyword] [var (optional)]
python3 zd_templator.py add [keyword]
python3 zd_templator.py del [keyword]


# architecture
- shelf_file / db - dict db that stores the templates and keyword pairs
- zdt.py - main script that interacts with user
- zdt_helper.py - helper functions (optional)


# order of operations
1. try out the py mdutils -> zendesk
2. 



# references
https://pypi.org/project/mdutils/
https://support.zendesk.com/hc/en-us/articles/4408846544922-Formatting-text-with-Markdown
https://python-markdown.github.io/ - This one is more intended for markdowon -> HTML 
