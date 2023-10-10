# -*- coding: utf-8 -*-
"""
AUE 8930 HW 3 Code 
Nicholas Kilbarger

"""
import numpy
import pypng
import matplotlib

#%% Question 1
#Given an array of integers, find two numbers in it such that they can add up 
#to a specific number. You may assume there are exactly one solution, you 
#can’t use the same element twice. (Only time-complexity optimized solution 
#gets full grade)

#Example:
#Given [2, 7, 11, 4], Target = 13.
#The answer is 2 and 11.

def solution(list, num): 
    #a=0 
    #b=0 
    '''type in your solution, find a and b in array that a+b=num'''
    
    # Initialize dictionary to store numbers
    nd={}
    
    for index, b in enumerate(list):
        # Find complement number (num-n) to each index
        a= num-b
        # If the complement exists in the dictionary, return it
        if a in nd:
            return a, b
        # Add current number and index to dictionary
        nd[b]=index
        
    # Otherwise if no solution
    return None

numbers = [0, 21, 78, 19, 90, 13] 
print(solution(numbers, 21)) 
print(solution(numbers, 25)) 

# Complexity O(n) because it iterates through the list only once and uses the subtraction
#operation to find the other number

#%% Question 2
#Given a binary tree, find the max depth of it. Modify the “solution” 
#function in the question2.py (Analyze your time complexity, and only 
#time-complexity optimized solution gets full grade)

class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def solution(root):
    '''type in your solution'''
    # Check for root as starting point
    if root is None:
        return 0
    # Search branches on each side
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    # Return the maximum depth of left and right subtrees + 1 (current node)
    return max(left_depth, right_depth) + 1

#Given Binary tree
a15=TreeNode(15)
a7=TreeNode(7)
a20=TreeNode(20)
a9=TreeNode(9)
a3=TreeNode(3)
a20.left=a15
a20.right=a7
a3.left=a9
a3.right=a20
#Run Function
print(solution(a3))
# Time complexity O(n) for depth first search method (must count a node of each branch)

#%% Question 3
#You are given two non-empty linked lists representing two non-negative 
#integers. The digits are stored in reverse order and each of their nodes 
#contain a single digit. Add the two numbers and return it as a linked list.
#You may assume the two numbers do not contain any leading zero, except the 
#number 0 itself.
#Example:
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.
#Modify the “solution” class in question3.py, you may design your input to
# test it.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Define carry digit
        carry_digit=0
        # Use list node class
        ln=ListNode()
        # Define current variable for each iteration
        cur=ln
        
        while l1 or l2:
            # Check for digits to add
            a=l1.val if l1 else 0
            b=l2.val if l2 else 0
            total=a+b+carry_digit
            # Define next carry digit 
            carry_digit=total // 10
            cur.next=ListNode(total % 10)
            # Prepare next iteration
            cur=cur.next
            if l1: 
                l1=l1.next
            if l2:
                l2=l2.next
        
        if carry_digit>0:
            cur.next=ListNode(carry)
        return ln.next

# Test Input
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result=Solution.addTwoNumbers(0,l1, l2)

# Print the resulting linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("end")

print("Input:")
print_linked_list(l1)
print_linked_list(l2)
print("Output:")
print_linked_list(result)

# Time complexity O(max(length(l1),length(l2))) -> O(n) as the operations on each node are time 
# constant so the time complexity is linear in terms of the length of the lists

#%% Question 4
#Given a string s, find the length of the longest substring without repeating 
#characters. You can expect the string length is less than 100, and only 
#contains English letters.
#Example 1:
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Modify the “solution” class in question4.py, you may design your input to test it.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use set() to find unique characters
        return len(set(s))    
#Test
output=Solution.lengthOfLongestSubstring(0,"abcabcbb")
print(output)
# Time complexity O(n) for the length of the entire input string

#%% Question 5
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
#determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.
#Modify the “solution” function in the question5.py. (Analyze your time complexity)

class Solution:
    def isValid(self, s: str) -> bool:
        # Define empty stack data structure to store previous bracket
        st = []
        # Dictionary to store the mapping of open and close bracket types
        b_map = {")": "(", "}": "{", "]": "["}
        # Loop through length of input string
        for b in s:
            # If the bracket is a closing bracket
            if b in b_map:
                # Pop the top element from the stack if it is non-empty, else assign a dummy value "#"
                top = st.pop() if st else '#'
                # Compare the popped element with the opening bracket
                if b_map[b] != top:
                    # If these do not match, string is invalid
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                st.append(b)
        
        # If the stack is empty at the end, all brackets have been closed correctly
        return not st

    # Test Case
    input_string = '(){}[]'
    is_valid = isValid(0,input_string)
    print("Is the input string valid?", is_valid)

# This algorithm has a time complexity of O(n) to compare each character n of the input string

#%% Question 6
#Use OpenCV to do a bilateral filter to an image, modify from question6.py, you may 
#use your favorite image, visualize the images before and after the filtering using 
#matplotlib.

import cv2 
import matplotlib

# Read the image. 
img = cv2.imread('Original.jpg') 
#img = img.resize(1000,1000)

# Apply bilateral filter

# Define the diameter of the pixel neighborhood (large values for larger blurs)
d = 15

# Define the standard deviation of the color space (small values for more color filtering)
sigma_color = 75

# Define the standard deviation of the coordinate space (small values for more spatial filtering)
sigma_space = 150

# Apply bilateral filter to the input image
filtered_img = cv2.bilateralFilter(img, d, sigma_color, sigma_space)

# Display the original and filtered images
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0); cv2.destroyAllWindows(); cv2.waitKey(1)
# Save the output. 
cv2.imwrite('bilateral.jpg', filtered_img) 

#%% Question 7
#Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding 
#up all the values along the path equals the given sum. (Note: A leaf is a node with no children.)
#Example: 
#Given the below binary tree and sum = 22,
#      5
#     / \
#    4   8
#   /   / \
#  11  13  4
# /  \      \
#7    2      1
#return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
#Modify the “solution” class in question7.py, test the above example and design your 
#test case.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        #Define a depth first search function, passing current node and sum
        def DFS(node,c_sum):
        
            # Check for starting point
            if not node:
                return False
            #Add node
            c_sum +=node.val
            
            # If leaf node and the current sum matches target sum, return True
            if not node.left and not node.right and c_sum == target:
               return True
            
            # Recursively traverse left and right subtrees, return True if path found
            return DFS(node.left, c_sum) or DFS(node.right, c_sum)
    
        # Check for root of tree
        if not root:
            return False
        
        return DFS(root, 0)
    
    
# Test Case
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left = TreeNode(13)
root.right.right.right = TreeNode(1)

target = 22
result = Solution.hasPathSum(0,root, target)
print("A root-to-leaf path sum equal to", target, "exists", result)

#%% Question 8 
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word 
#or phrase, typically using all the original letters exactly once.

#Example 1:
#Input: s = "anagram", t = "nagaram"
#Output: true

#Example 2:
#Input: s = "rat", t = "car"
#Output: false

#Constraints:
#1 <= s.length, t.length <= 5 * 104
#s and t consist of lowercase English letters.
#Modify the “solution” function in the question8.py. (Analyze your time complexity)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Compare string length first
        if len(s) != len(t):
            return False
        
    # Check counts of each character in each string to determine anagram
        
        # Create dictionaries to store character frequencies
        s_char = {}
        t_char = {}
        
        # Count character frequencies in string s using get()
        for char in s:
            s_char[char] = s_char.get(char, 0) + 1
        
        # Count character frequencies in string t
        for char in t:
            t_char[char] = t_char.get(char, 0) + 1
        
        # Compare character frequencies in both strings
        return s_char == t_char

# Test Cases
s = "anagram"
t = "nagaram"
result = Solution.isAnagram(0,s, t)
print(result)  # Output: True

s = "rat"
t = "car"
result = Solution.isAnagram(0,s, t)
print(result)  # Output: False

# Overall Time Complexity is O(n) where n is the length of each of the two strings (should be the same) 
# because the for loops count each character in each of the strings for the whole string

#%% PART B

#%% 1) Demo existing reference and get to know the behaviour of its path search.		(2’)
	#The demo run file is: examples/occupancy_map_8n.py
    

#%% 2) Implement occupancy gridmap-based Dijkstra for same functionality as (1a)  	(18’)
	#If you prefer, you can use this as the template to revise:
		#Homework3/map-path-search/a_star_occupancy.py

