# regex-dictionary 
Python type to use regex as keys in dict

# Install
```bash
pip install regex-dictionary
```
# Usage
```
>>> from regex_dictionary import RegexDict
>>> d = RegexDict({"simple_key": "simple_value", "regex_key.*": "simple_value"})
>>> d["simple_key"]
'simple_value'
>>> d["regex_key_some_stuff"]
'simple_value'
>>> d.get("regex_key_some_stuff", "default")
'simple_value'
>>> d.get("some_stuff_regex_key_some_stuff", "default")
'default'
>>> for k, v in d.items():
...     print(k, v)
...
re.compile('^simple_key$') simple_value
re.compile('^regex_key.*$') simple_value
```

