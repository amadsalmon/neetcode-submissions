class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_draft = chars

        total = 0

        good_words=[]

        for word in words:
            is_good_word = True
            for letter in word:
                if letter in chars_draft:
                    print(f"removing {letter} from {chars_draft}")
                    chars_draft = chars_draft.replace(letter, '', 1)
                    print(f"  now chars_draft: {chars_draft}")
                else:
                    is_good_word = False
                    break
            if is_good_word:
                good_words += word

            chars_draft = chars
        print(good_words)
    
        return len(good_words)
                    
            

        