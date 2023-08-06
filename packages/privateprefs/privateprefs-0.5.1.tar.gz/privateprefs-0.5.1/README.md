# PrivatePrefs


### Easily Keep API Keys out of GitHub 

[![Pytest - Coverage](https://img.shields.io/badge/Coverage-100%25-31c653)](https://github.com/DarrenHaba/privateprefs/actions)
[![Package CI](https://github.com/DarrenHaba/privateprefs/actions/workflows/ci.yml/badge.svg)](https://github.com/DarrenHaba/privateprefs/actions/workflows/ci.yml)
[![GitHub](https://img.shields.io/badge/license-MIT-31c653)](https://github.com/DarrenHaba/privateprefs#license)
[![PyPI - Version](https://img.shields.io/pypi/v/privateprefs.svg)](https://pypi.org/project/privateprefs)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/privateprefs.svg)](https://pypi.org/project/privateprefs)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

`privateprefs` keeps sensitive data like API Keys, email addresses, usernames, etc, out 
of your code, so sensitive data can't accidentally get added to private or public repositories like GitHub, 
GitLab, Bitbucket, etc.

-----

**Table of Contents**

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Python Docs](#python-docs)
- [CLI Docs](#cli-docs)
- [License](#license)

### The Problem
###### *Spammers and scammers can scrape code from public and even private repos* 😱
```python
secret_api_key = "mfnc80imW4RawjYwVLsArx"
my_email = "darren@spammed.com"
# @spammers please send me lots of spam and @hackers feel free to hack my accounts!
# thanks, Your Next Victim.
```

### The Solution
###### *Use `privateprefs` and never hardcode sensitive data in your code again* 😎
```python
import privateprefs as prefs
secret_api_key = prefs.load("secret_api_key")
my_email = prefs.load("my_email")
# @spammers sorry, spammers no spamming and @hackers sorry, hackers no hacking!
# thanks, Not Your Victim.
```

before this solution will work we need to 
- install `privateprefs` 
- use the command line to save/store sensitive data in key-value pairs. 
- the data is stored in a data.ini file stored on your computer
- the data.ini is stored outside your project and won't get added to repos
- use python to load the values by calling the corresponding keys

This will become clear after you [Install](#installation) `privateprefs` and follow along with the
[Getting Started](#getting-started) guide below.

## Installation
Use ``pip`` to install
```sh
pip install privateprefs
```

## Getting Started

### Save Value
###### *run command*
```sh
privateprefs save "secret_api_key" "mfnc80imW4RawjYwVLsArx"
```
This saves/sets the **value** `"mfnc80imW4RawjYwVLsArx"` to the **key** `"secret_api_key"`

### Load Value
###### *python script*
```python
import privateprefs as prefs
prefs.load("secret_api_key")  # "mfnc80imW4RawjYwVLsArx"
```
This loads/gets the **value** `"mfnc80imW4RawjYwVLsArx"` from the **key** `"secret_api_key"`

### Show Me The Data
###### *run command*
```sh
privateprefs data
```
###### *returns*
```

key-value data pairs are stored in the data.ini file located at:
C:\Users\USER_NAME\AppData\Local\privateprefs\data.ini (running windows)

data.ini file contents:
+----------------+------------------------+
|      KEY       |         VALUE          |
+----------------+------------------------+
| secret_api_key | mfnc80imW4RawjYwVLsArx |
+----------------+------------------------+

```
The file path will very on different operating systems but here are the most common:
- C:\Users\USER_NAME\AppData\Local\privateprefs\data.ini (on windows)
- ~/Library/Application Support/privateprefs/data.ini (on mac)
- ~/.local/share/privateprefs/data.ini (on linux)

The data table will list all saved/stored key-value pairs in the data.ini file.

### Open the Data File
###### *run command*
```sh
privateprefs open
```
This will open the data.ini file in the default application associated with .ini files. 
If your operating system ask you to choose an application, you can use a simple text editor
or your IDE of choice like PyCharm, IDLE, Visual Studio Code, etc.
###### *opened data.ini file (in PyCharm)*
![private prefs data.ini file](https://github.com/DarrenHaba/privateprefs/blob/master/images/privateprefs_data_file.png?raw=true)

We can add, remove, update, and delete key-value pairs by directly editing the data.ini file. 
Let's add the key `my_email` with a value of `darren@spammed.com` to the file manually.
###### *data.ini with newly added line*
![private prefs data.ini file](https://github.com/DarrenHaba/privateprefs/blob/master/images/privateprefs_date_file_add_key_value.png?raw=true)

For those who don't like to use the cli (command line interface) feel free to edit the data.ini file directly, but 
please follow a few rules to ensure you don't break the package
1. The first line must contain `[privateprefs]`
2. the next lines must be `my_key = my value` pairs
3. don't add quotes to strings like `my_key = "my value"` (don't do this!)
4. it's best to use the same name rules for keys as with [Python variables name](https://www.w3schools.com/python/gloss_python_variable_names.asp)

### Delete Value
```sh
privateprefs delete "secret_api_key"
```

### Delete All Values
###### <sub> *-- WARNING ALL SAVED DATA WILL BE PERMANENTLY DELETED --* </sub>
```sh
# don't run if you have saved data you want to keep
privateprefs delete_all
```

### Conclusion
You now have a basic understanding of how `privateprefs` works and how to use it. 
We left out a few Python functions and CLI commands, but they are covered in the docs 
below if you're interested.

## Python Docs
The following Python code assumes we have the following two saved
key-value pairs
###### *run these commands to add some data for testing*
```sh
privateprefs save my_key "my value"
privateprefs save my_other_key "my other key"
```
###### *run these commands to remove the test data when done*
```sh
privateprefs delete my_key
privateprefs delete my_other_key
```

### Load Value
```python 
from privateprefs import load

my_value = load("my_key")
print(my_value)
```
Return the `value` for the given `key` or `None` if the key doesn't exist.

### Load All Values
```python 
from privateprefs import load_keys

my_value_dict = load_keys()
my_value = my_value_dict["my_key"]
my_other_value = my_value_dict["my_other_key"]
print(f"My Value: {my_value}")
print(f"My Other Value: {my_other_value}")
```
Return all saved key-value pairs as a dictionary 

### Load Only Filtered Key Values
```python 
from privateprefs import load_keys

filter_keys = ["my_key"]
my_value_dict = load_keys(filter_keys)
my_value = my_value_dict["my_key"]
print(f"My Value: {my_value}")
does_my_other_key_exist = 'my_other_key' in my_value_dict.keys()
print(f"does_my_other_key_exist: {does_my_other_key_exist}")
```
Only returns key-value pairs that are in the `filter_keys` list

### Load All Values as List of Tuples
```python 
from privateprefs import load_keys

my_tuple_list = load_keys(return_as_list=True)
for my_tuple in my_tuple_list:
    print(f"Tuple: {my_tuple}")
    my_key = my_tuple[0]
    my_value = my_tuple[1]
    print(f"key: {my_key}")
    print(f"value: {my_value} \n")
```
Return all saved key-value pairs as a dictionary 

### Delete Value
```python 
from privateprefs import delete

delete("my_key")
```
Delete the value for a given key 

### Delete All Values
###### <sub> *-- WARNING ALL SAVED DATA WILL BE PERMANENTLY DELETED --* </sub>
```python 
from privateprefs import delete_all

# don't run if you have saved data you want to keep
delete_all()
```
Delete all saved/stored values

###### Python Note:
Note there are no functions to save values using Python; this is by design, by forcing 
everyone to save values only using the CLI or editing the data.ini file ensures that 
hardcoded values will never end up in version control repositories.

But never say never. If you dig around in the package core, you can find the save functions, 
but using the internal Python save functions means hard-coding sensitive data directly in 
Python and defeating the purpose of this package.

## CLI Docs

### Help
```sh
privateprefs -h
```
Display the potential arguments and options to use.

### Save
```sh
privateprefs save my_key "My Value"
```
Save a key-value pair to the data.ini file, quotes required if there are spaces in the string.

### Load
```sh
privateprefs load my_key
```
Load a value for the given key.

### Delete
```sh
privateprefs delete my_key
```
Delete the value for the given key.

### Delete All
```sh
privateprefs delete_all
```
Deletes all values.

### Data
```sh
privateprefs data
```
Display the data.ini file path and its contents as a data table.

### Open
```sh
privateprefs open
```
Open the data.ini file in the application associated with opening .ini file extension.

### Pre-Uninstall
```sh
privateprefs pre_uninstall
```
Removes all files and folders created by this package.

## License
`privateprefs` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
