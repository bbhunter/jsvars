# jsvars
Get variable names from a js file or a list of js urls. 
```
Usage: 
cat test.js | jsvars
cat urls.txt | jsvars -u
```
The -s flag will enable smart detection using the nostril library. This will eliminate random var names from obfuscated js but it will also likely miss some legitimate variables. To use it you'll have to install nostril using: 

```
pip3 install git+https://github.com/casics/nostril.git

