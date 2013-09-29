#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        SortedDict
# Purpose:
#
# Author:      Filip Kral
#
# Created:     29/09/2013
# Copyright:   (c) filipkral.com 2013
# Licence:     MIT License http://choosealicense.com/licenses/mit/
#-------------------------------------------------------------------------------

class SortedDict(dict):
    """A dictionary which remembers order of keys and iterates over items in the same order. This classs is considerably slower than the built in dict, but has the benefit of remembering order of keys (stored as an extra list)"""

    def __init__(self, mapping=[]):
        """Create an instance of sorted dictionary.
        mapping, optional list of key vlue pairs to start with, e.g. [("a", "one"), ("b", "two")]
        """
        self.orderedkeys = []
        if len(mapping) > 0:
            self.appendmapping(mapping)

    def appendmapping(self, mapping):
        """Add key - value pais to the dictionary.
        mapping, list of key vlue pairs to add, e.g. [("a", "one"), ("b", "two")]
        If key already exists in the dictionary, the item will be replaced without warning and order of that key will not be changed!
        """
        if len(mapping) > 0:
            for k,v in  mapping:
                dict.update(self, {k:v})
                if k not in self.orderedkeys:
                    self.orderedkeys.append(k)

    def update(self, d):
        """Update the dictionary with a new dictionary.
        d, dictionary to update with. Works just like dict.update.
        Not that order of the keys in d is cannot be pre-defined.
        """
        for k,v in d.iteritems():
            dict.update(self, {k:v})
            if k not in self.orderedkeys:
                self.orderedkeys.append(k)

    def sortkeys(self):
        """Sorts the keys of the dictionary"""
        self.orderedkeys.sort()

    def __delitem__(self, y):
        dict.__delitem__(self, y)
        if y in self.orderedkeys:
            self.orderedkeys.remove(y)

    def __repr__(self):
        comma = "," if len(self.orderedkeys) > 1 else ""
        rets = []
        for k,v in self.iteritems():
            rets.append("%s: %s" % (k, v))
        ret = "{" + ", ".join(rets) + "}"
        return ret

    def __setitem__(self, i, y):
        dict.__setitem__(self, i, y)
        if y not in self.orderedkeys:
            self.orderedkeys.append(i)

    def toDict(self):
        """Return a deep copy of this dictionary as plain dict"""
        ret = {}
        for k,v in self.iteritems():
            ret.update({k:v})
        return ret

    def clear(self):
        """Remove all items"""
        self.sortkeys = []
        dict.clear(self)

    def copy(self):
        """copy like dict.copy()"""
        return SortedDict(list(self.items()))

    def fromkeys(self, S, v = None):
        """New SortedDict with keys from S and values equal to v.
        v defaults to None. Order of keys follows iter(S).
        """
        mapping = [(k,v) for k in iter(S)]
        return SortedDict(mapping)

    def items(self):
        """list of (key, value) pairs from the dictionary as 2-tuples, in order"""
        for k in self.orderedkeys:
            yield (k, self[k])

    def iteritems(self):
        """an iterator over th (key, value) pairs in the dictionary, in order"""
        for k in self.orderedkeys:
            yield k, self[k]

    def iterkeys(self):
        """an iterator over the keys in the dictionary"""
        for k in self.orderedkeys:
            yield k

    def itervalues(self):
        """an iterator over the values in the dictionary"""
        for k in self.orderedkeys:
            yield self[k]

    def keys(self):
        """Return list of keys of the dictionary, in order"""
        return self.orderedkeys

    def pop(self, k, d = None):
        """Remove specified key and return the corresponding value.
        If key is not found, d is returned if given, None if d is not given (difference from dict.pop)"""
        ret = dict.pop(self, k, d)
        if k in self.orderedkeys:
            self.orderedkeys.remove(k)
        return ret

    def popitem(self):
        """Remove and return last (key, value) pair as a 2-tuple, raise KeyError if the dictionary is empty."""
        if len(self) > 0:
            lastkey = self.orderedkeys[-1]
            self.orderedkeys = self.orderedkeys[:-1]
            v = dict.pop(self, lastkey)
            return (lastkey, v)
        else:
            raise KeyError()

    def setdefault(self, k, d = None):
        """Return D.get(k, d), also set D[k] = d if k not in D"""
        if k not in self.orderedkeys:
            self.orderedkeys.append(k)
        ret = dict.setdefault(self, k,d)
        return ret

    def values(self):
        """Return list of values in the dictionary"""
        return [self[k] for k in self.orderedkeys]


if __name__ == '__main__':
    # tests
    d = SortedDict([(1,"one"),(2, "two")])
    print d

    d.appendmapping([(4, "four"), (3, "three")])
    print d

    d.sortkeys()
    print d

    d.update({9:"nine"})
    d.update({8:"eight"})
    print d.pop(10)
    print d

    print d.popitem()
    print d

    print d.pop(4)
    print d
