from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        # Перевірка некоректних вхідних даних
        if not isinstance(strings, list) or any(not isinstance(word, str) for word in strings):
            raise ValueError("Input must be a list of strings.")
        
        if not strings:  # Порожній список
            return ""
        
        # Якщо список містить лише один рядок, його префікс - це сам рядок
        if len(strings) == 1:
            return strings[0]
        
        # Ініціалізація префікса першим словом
        prefix = strings[0]
        
        for word in strings[1:]:
            # Знаходимо найдовший спільний префікс між prefix та word
            i = 0
            while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
                i += 1
            
            # Скорочуємо префікс до спільної частини
            prefix = prefix[:i]
            
            # Якщо префікс стає порожнім, виходимо
            if not prefix:
                return ""
        
        return prefix

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = ["singleword"]
    assert trie.find_longest_common_word(strings) == "singleword"

    print("All tests passed!")
