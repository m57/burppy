# burppy
A tool to allow you to extract fine-grained information on requests and responses that have been captured through Burp.

This is still undergoing development, currently it has recieved a huge total of 1.5 hours during a pen test to make my life easier when searching for specific headers and responses.

The usage is pretty simple:

Inside a  burp session -> highlight all requests and responses you care about -> right click -> save items 

This is just saved as an XML file formatted like so:

<items>
<item>
...
<url>...</url>
<request> ... base64 ... </request>
<response> ... base64 ... </response>
...
</item>
</items>

Will be adding more functionality in the very near future as I think this could be v. useful.

~x90
