"""
ID: sukru2
LANG: PYTHON2
TASK: prefix
"""

fin = open ("prefix.in", 'r')
fout = open ("prefix.out", 'w')

ll = []
while True:
    line = fin.readline().strip()
    if line == ".":
        break

    ll.extend(line.split(" "))

S = fin.readline().strip()
check = True
while check:
    try:
        line = fin.readline().strip()
        if len(line) == 0:
            raise
        S += line
    except:
        check = False

class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

    def __str__(self):
        return "%s" % (str(self.isEndOfWord))

class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in xrange(length):
            # if current character is not present
            if key[level] not in pCrawl.children:
                pCrawl.children[key[level]] = self.getNode()

            pCrawl = pCrawl.children[key[level]]

        pCrawl.isEndOfWord = True

    def search(self, S, ind):
        global newkeep

        pCrawl = self.root
        length = len(S)
        for level in xrange(ind, length):
            if S[level] not in pCrawl.children:
                break

            if pCrawl.children[S[level]].isEndOfWord:
                newkeep.add(level)

            pCrawl = pCrawl.children[S[level]]

S = S.lower()
t = Trie()
for key in ll:
    t.insert(key.lower())


newkeep = set()
mox = -1
dp = set()

t.search(S, 0)
keep = newkeep
newkeep = set()

while len(keep) > 0:
    for ind in keep:
        if ind in dp:
            continue

        if ind > mox:
            mox = ind

        dp.add(ind)
        t.search(S, ind+1)


    keep = newkeep
    newkeep = set()


#print mox + 1
fout.write("%d\n" % (mox+1))
