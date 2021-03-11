from listops import evenfilter,vowelfilter,stringmapper,greatesteven
import functools

lista = [3243,233565756,23,12,5435,32,53,22,5351,354356,3432]
listb=['India','Pakistan','China','Japan','Egypt','Thailand','Philiphines','Newzealand','Bosnia']

print(list(filter(evenfilter,lista)))
print(list(filter(vowelfilter,listb)))
print(list(map(stringmapper,listb)))
print(functools.reduce(greatesteven,lista))

