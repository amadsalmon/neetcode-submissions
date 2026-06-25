class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        good_words=[]

        chars_draft = chars

        for word in words:
            is_good_word = True
            for letter in word:
                if letter in chars_draft:
                    chars_draft = chars_draft.replace(letter, '', 1)
                else:
                    is_good_word = False
                    break
            if is_good_word:
                good_words += word
            chars_draft = chars
    
        return len(good_words)
                    
