Pikapy - Mass Pokemon Go Account Creator and ToS verifier
==============================================================

Description
-----------
Automatically creates Pokemon Trainer Club accounts, and reads the ToS making them usable after the recent Niantic patch.


Use
---
**Command line interface:**

After installing the package run 'pikapy' from the terminal to create a new accounts.
Optional parameters include *--username*, *--password*, *--email*, *--count*
Use *--help* for command line interface help.

Example 1 (Create entirely random new account)::

    ~pikapy
    Created new account:
      Username:  dGXJXnAzxqmjbaP
      Password:  yUbiAgcXhBrEwHk
      Email   :  TVKzlu1AcW@6yxi6.com
      
Example 2 (Create 2 accounts with the same password)::

    ~pikapy -p password -c 2
    Created new account:
      Username:  dGXJXnAzxqmjbaP
      Password:  password
      Email   :  TVKzlu1AcW@6yxi6.com
    Created new account:
      Username:  vKEkp19eb0l4mFW
      Password:  password
      Email   :  TVKzlu1AcW@6yxi6.com
      
Example 3 (Create a new account with specified parameters)::

    ~pikapy --username=mycustomusername --password=hunter2 --email=verifiable@lackmail.ru
    Created new account:
      Username:  mycustomusername
      Password:  hunter2
      Email   :  verifiable@lackmail.ru


Extra Options:

- *--email-tag*: Add the username as a tag to the email (e.g. address+username@gmail.com)
Output is saved both as a list of usernames, and pokemongo-map ready -u username1 -u username2 -username3... format

Suggested Use:
-------------
    
    ~pikapy -p masterpassword -c 100

This will generate 100 Pokemon Go accounts with random username and password==masterpassword
Next step would be inputting all the usernames from the generated .txt file into the pokemongo-map.


Planning to make it fully autonomous in the close future.
    

Installation
------------

Install from Github using pip::

    ~pip install git+https://github.com/skvvv/PTCAccount
    
    
    If given errors try (Arch linux users will most likely have to do this):
    
    
    ~sudo pip2 install git+https://github.com/skvvv/PTCAccount
