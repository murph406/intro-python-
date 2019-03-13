#!/usr/bin/env python3


class PText(object):
    wordsByPrefix = None

    rankByWord = None

    keyMap = {'1': "'-", '2': 'abc', '3': 'def',
              '4': 'ghi', '5': 'jkl', '6': 'mno',
              '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def __init__(self):
        self.keyPresses = []
        PText.wordsByPrefix = ()
        PText.rankByWord = ()
        self._performCaching()

    def match(self, word):
        """Checks if all the current keypresses exactly match the letters
        of word.
        >>> pt = PText()
        >>> pt.add('222')
        >>> pt.match('backlog')  # 2->b, 2->a, 2->c so yes
        True
        >>> pt.match('a')  # too short, cannot match 222
        False
        """

        if len(word) < len(self.keyPresses):
            return False
        for i in range(len(self.keys)):
            letter = word[i]
            keystroke = self.keyPresses[i]
            goodLetters = PText.keyMap[keystroke]
            if letter not in goodLetters:
                return False
        return True

    def possiblePrefixes(self):
        """Generate a list of all 3-character prefixes that can be
        generated from the beginning key presses.
        >>> pt = Ptext()
        >>> pt.add('234')
        >>> [prefix for prefix in pt.possiblePrefixes()]
        ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
        """
        if len(self.keyPresses) < 3:
            raise ValueError
        ret = []
        for c1 in PText.keyMap[self.keyPresses[0]]:
            for c2 in PText.keyMap[self.keyPresses[1]]:
                for c3 in PText.keyMap[self.keyPresses[2]]:
                    ret.append(c1 + c2 + c3)
        return ret

    def _performCaching(self):
        """Read word list into data structures that we will use:
        wordsByPrefix -- a dictionary that contains a list of words in rank
                         order for each 3-letter prefix encountered in the
                         word list
        rankByWord -- a dictionary that maps each word to its rank
        If these are already filled in (not None), then return immediately.
        Reads the word list file, WORD_LIST_FILE, which has all possible
        English words (that we will consider) listed in rank order.
        """
        x = {}
        y = {}

        file = open(WORD_LIST_FILE, 'r')
        rank = 1
        for word in file:
            if word[-1:] == '\n':
                word = word[:-1]
            if len(word) >= 3:
                prefix = word[:3].lower()
                if prefix in y:
                    y[prefix].append(word)
                else:
                    y[prefix] = [word]
                x[word] = rank
                rank += 1
        file.close()
        PText.rankByWords = x
        PText.wordsByPrefix = y
        

    def add(self, keyPresses):
        """Append a new key press (or a sequence of them) onto current word.
        keyPress -- '2', '3', ..., '9' from telephone keypad
        """
        self.keyPresses.extend(keyPresses)

    def backspace(self):
        """Remove last key press from current word (backspace)."""
        
        self.keyPresses.pop(keyPresses)

    def possible(self):
        """Returns a list of possible words given the current key sequence.
        Assumes at least 3 keystrokes have been entered (raises ValueError
        otherwise). Returned in rank order.
        """
        self._performCaching()
        if len(self.keyPresses) < 3:
            raise ValueError("Not Enough Keys for Predicting Word")
    
        x = PText.wordsByPrefix
        retValue = []
        for prefix in self.possiblePrefixes():
            if prefix in x:
                wordList = x[prefix]
                for word in wordList:
                    if self.matches(word):
                        retValue.append(word)
        retValue.sort(key=lambda word: PText.rankByWord[word])
        return retValue

    def best(self):
        """Return the most likely English word for the current key sequence.
        Assumes at least 3 keystrokes have been entered (raises ValueError
        otherwise). If there a no words that match the current key sequence,
        ValueError is raised.
        """
        if len(self.keypresses) < 3:
            raise ValueError('Need at least 3 keys')
        words = self.possible()
        if len(words) > 0:
            return words[0]
