# 這題是會給一個 class Iterator 的東西，然後去設計 peek function
# 做法就是在 _init_ 的時候直接把 iterator 的東西全部存起來並且宣告 position 來記錄位置點在哪
# 在 peek 的時候直接回傳該位置的值就可以了，在 next 裡面就是回傳當下的值之後把位置往後移動一格，這邊做法是先往後移動在回傳前一個數字
# 在 hasNext 裡面，就是看看說現在位置有沒有在 list 裡面就可以了

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.ls = list()
        while iterator.hasNext():
            self.ls.append(iterator.next())
        self.pos = 0
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.ls[self.pos]

    def next(self):
        """
        :rtype: int
        """
        self.pos += 1
        return self.ls[self.pos-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pos < len(self.ls)
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
