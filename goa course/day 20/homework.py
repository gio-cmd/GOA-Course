haystack = ["boom", 1999, "needle", "parents", 10,]
def find_needle(haystack):
    index = haystack.index('needle')
    return 'found the needle at position {}'.format(index)
find_needle