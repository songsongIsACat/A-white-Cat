# 求区间范围
class Solution:
    def summaryRanges(self, nums):
        resultList = []
        # startInt = endInt = nums[0]
        if len(nums) == 0:
            return resultList
        elif len(nums) == 1:
            # startInt = str(nums[0])
            resultList.append(str(nums[0]))
            return resultList
        else:
            startInt = endInt = nums[0]
            for x in range(1, len(nums) + 1):
                # startInt = nums[0]
                # endInt = startInt[0]
                # resultList.append(nums[x])
                if x != len(nums):
                    if nums[x] - 1 == nums[x - 1]:
                        endInt = nums[x]
                    else:
                        if startInt != endInt:
                            resultList.append("%d->%d" % (startInt, endInt))
                        else:
                            resultList.append("%d" % startInt)
                        startInt = endInt = nums[x]
                else:
                    # resultList.append("%d"% endInt)
                    if startInt != endInt:
                        resultList.append("%d->%d" % (startInt, endInt))
                    else:
                        resultList.append("%d" % startInt)
        return resultList


# 找出字符串中第一个匹配项的下标
"""重点：使用find()函数"""


class Solution11:
    def strStr(self, haystack, needle):
        return haystack.find(needle)


# 除掉非字母和数字的字符，并全部转换为小写，判断是否为回文数
"""重点：#PS:使用倒序切片可以解决为空字符串的场景；关键字isalnum:判断是否为字符串或数字"""


class Solution12:
    def isPalindrome(self, s):
        ss = ""
        for i in s:
            if i.isalnum():
                ss += i.lower()
        l = ss[::-1]
        if ss == l:
            return True
        else:
            return False


# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。如，"ace"是"abcde"的一个子序列，而"aec"不是
"""重点：可以使用Counter计数，并且使用集合运算"""


class Solution13:
    def isSubsequence(self, s, t):
        y = b = 0
        for x in s:
            for i in range(y, len(s)):
                if x == s[i]:
                    y = i + 1
                    b += 1
                    break
        if b == len(t):
            return True
        else:
            return False


# 7.23：给你两个字符串：r和 m，判断 r能不能由 m里面的字符构成。如果可以，返回 true ；否则返回 false 。m中的每个字符只能在 r中使用一次
"""重点：1、在遍历比较中，可使用len函数减少一部分的循环次数，优化代码；
         2、字符串无法直接移除某个元素，无法使用remove函数，可将字符串转为列表，或者使用replace替换删除
         3、可以使用Counter计数，并且使用集合运算"""
from collections import Counter


class Solution15:
    # 方法1：使用遍历判断，如果在，就删除
    def canConstruct1(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):  # len函数可以减少部份用例的遍历次数
            return False
        for i in ransomNote:
            # 字符串无法直接移除某个元素，无法使用remove函数，可将字符串转为列表，或者使用replace替换删除
            magazine = list(magazine)
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return True

    # 方法2：使用counter函数
    def canConstruct2(self, ransomNote, magazine):
        # if len(ransomNote) > len(magazine):
        #     return False
        return Counter(magazine) <= Counter(ransomNote)  # 此写法只支持py3


# 7.23：给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律---单词规律
"""重点：主要是使用字典的映射关系进行判断
        2、使用Len函数节约一部分循环判断
        3、使用两个字典确认一一对应的关系"""


class Solution14:
    def wordPattern(self, pattern, s):
        p_dict = {}
        k_dict = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        for p, k in zip(pattern, s):
            if (p in p_dict and p_dict[p] != k) or (k in k_dict and k_dict[k] != p):
                return False
            else:
                p_dict[p] = k
                k_dict[k] = p
        return True


# 7.23：给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词(若 s 和 t 中每个字符出现的次数都相同)
"""重点：使用Counter"""


class Solution16:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        else:
            return False


# 7.23：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target的那两个整数，并返回它们的数组下标
"""重点：无"""


class Solution17:
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for x in range(i + 1, len(nums)):
                if nums[i] + nums[x] == target:
                    return [i, x]


# 7.24：整数转罗马数字   3749--700   58
"""重点：分段处理，且需要处理为0的特殊情况"""
class Solution18:
    def intToRoman(self, num):
        roman_dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M",
                      4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
        n_sum = ""
        i = len(str(num))-1
        for k in str(num):
            k = int(k)
            if 1<=k<=3:
                n_sum += roman_dict[10**i] * k
                i -= 1
            elif 5<=k<=8:
                n = k // 5
                n_sum += roman_dict[5*10**i] + roman_dict[10**i] * (k-5)
                i -= 1
            elif k in (4,9):
                n_sum += roman_dict[k*10**i]
                i -= 1
            else:
                i -= 1     #注意：为0的情况
        return n_sum

#7.24：快乐数111
"""重点："""
class Solution19:
    def isHappy(self, n):
        #i_sum = 0
        i_sum_list = []
        while True:
            i_sum = 0    #不能把这个放外面，因为每次和都需要清零重算
            for i in str(n):
                i_sum += int(i) ** 2
            if i_sum == 1:
                return True
            elif i_sum in i_sum_list:
                return False
            else:
                n = i_sum
                i_sum_list.append(i_sum)

## 求最长公共前缀  ["flower","flow","flight"]
# class Solution2:
#     def longestCommonPrefix(self, strs):
#         commonResult = ""
#         for i in range(len(strs[0])):
#             for x in strs:
#                 for y in x:



if __name__ == "__main__":
    myTest = Solution19()
    # print(myTest.canConstruct2("aab", "baa"))
    a = "abba"
    b = "dog dog dog dog"
    print(myTest.isHappy(19))

    # print(myTest.isSubsequence("abc", "ahbgdc"))
    # a = [-1]
    # print(myTest.summaryRanges(a))
    # print(type(" "))
