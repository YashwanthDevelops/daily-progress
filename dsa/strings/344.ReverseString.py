class Solution:
    def reverseString(self, s: List[str]) -> None:
        right = len(s)-1
        for i in range(int(len(s)/2)):
            temp = s[i]
            s[i] = s[right-i]
            s[right-i] = temp
        print(s)
