

# In[1]:


import sys

print('Type of sys.stdin  :', type(sys.stdin))
print('Type of sys.stdout :', type(sys.stdout))
print('Type of sys.stderr :', type(sys.stderr))
print()
print('stdout name     :', sys.stdout.name)
print('stdout encoding :', sys.stdout.encoding)


# In[1]:


import sys

# print() is essentially a wrapper around sys.stdout.write()
print('Hello from print()')
sys.stdout.write('Hello from sys.stdout.write()\n')

# Both produce identical output
# Writing errors to stderr:
sys.stderr.write('This would go to the error stream\n')


# In[2]:


import sys, time

# flush=True forces the buffer to empty immediately
for i in range(5):
    print(f'Step {i+1}...', end='', flush=True)
    time.sleep(0.7)

print(' Done!')



# In[3]:


import time

# Real-time progress with flush=True
print('Loading', end='', flush=True)
for x in range(5):
    time.sleep(1.5)
    print('.', end='', flush=False)
print(' Ready!')


# In[4]:


# *objects — multiple positional arguments, any type
print('one', 'two', 'three')           # three strings
print(42, 3.14, True, None)            # any types — converted via str()
print()                                # no args → just the end character (blank line)


# In[5]:


# sep — the string placed BETWEEN each object
print('one', 'two', 'three', sep=', ')    # CSV style
print('one', 'two', 'three', sep=' | ')   # pipe-delimited
print('one', 'two', 'three', sep='')      # no separator
print(2025, 6, 15, sep='-')               # date: 2025-6-15
print('a', 'b', 'c', sep='\n')            # each on its own line


# In[6]:


import time

# end — what comes AFTER the last object (default: newline)
print('Loading', end='')
print('.', end='')
print('.', end='')
print('. Done!')     # uses default end='\n'

print('---')

# \r overwrites current line — progress bar effect
for i in range(1, 6):
    print(f'\rProgress: {i}/5', end='', flush=True)
    time.sleep(0.2)
print('  ✓')


# In[7]:


import sys

# file — redirect to any stream or file object
print('This is normal output')
print('This is an error', file=sys.stderr)

# Write to a file
with open('/tmp/demo.txt', 'w') as f:
    print('Line 1', file=f)
    print('Line 2', file=f)
    print(42, 3.14, sep=' | ', file=f)

with open('/tmp/demo.txt') as f:
    print(f.read())


# In[8]:


# All 5 parameters together
name, score = 'Alice', 98.5
print('Name:', name, 'Score:', score, sep='  ', end='\n\n', flush=True)

# Manual equivalent:
import sys
sys.stdout.write('Name:  ' + str(name) + '  Score:  ' + str(score) + '\n\n')
sys.stdout.flush()


# In[9]:


# ── % operator (old style — still in many textbooks)
name, age, pi = 'Alice', 30, 3.14159

print('Name: %s, Age: %d' % (name, age))
print('Pi = %f' % pi)
print('Pi = %.2f' % pi)              # 2 decimal places
print('In %d days we made %.1f million %s.' % (34, 6.1, 'dollars'))


# In[ ]:


# ── .format() method
name, score = 'Bob', 98.5

print('Hello {}! Score: {}'.format(name, score))          # positional
print('{0} scored {1}. {0} wins!'.format(name, score))    # indexed (reuse)
print('{name} scored {score:.1f}'.format(name=name, score=score))  # named

# Format specifiers
print('{:>10}'.format('hi'))      # right-align in 10 chars
print('{:0>5}'.format(42))        # zero-pad
print('{:,}'.format(1000000))     # thousands separator
print('{:#x}'.format(255))        # hex with prefix: 0xff


# In[10]:


# ── f-strings — modern standard (Python 3.6+)
name, score = 'Carol', 97.333

print(f'Hello, {name}!')                        # basic
print(f'Score: {score:.2f}')                    # format spec
print(f'2 ** 10 = {2 ** 10}')                   # expression
print(f'Items: {len([1, 2, 3])}')               # function call
print(f'Upper: {name.upper()}')                 # method call

# Debug mode — Python 3.8+
x = 42
print(f'{x=}')                                  # prints: x=42

# Conditional
print(f"Grade: {'A' if score >= 90 else 'B'}")


# In[ ]:


# All three styles side by side
name, score = 'Dave', 95.7

old_style  = 'Student: %s | Score: %.1f' % (name, score)
format_str = 'Student: {} | Score: {:.1f}'.format(name, score)
f_str      = f'Student: {name} | Score: {score:.1f}'

print(old_style)
print(format_str)
print(f_str)
print('All equal?', old_style == format_str == f_str)


# In[11]:


# Creating strings
s1 = 'single quotes'
s2 = 'double quotes'    # both work identically
s3 = str(42)            # from int
s4 = str([1, 2, 3])     # from list

print(s1, s2, s3, s4)

# Immutability demo
word = 'hello'
try:
    word[0] = 'H'        # This FAILS
except TypeError as e:
    print(f'Error: {e}')

# Create a NEW string
word = 'H' + word[1:]
print(f'New string: {word}')


# In[12]:


# Indexing and slicing:  s[start:stop:step]   (stop is EXCLUSIVE)
s = 'Hello, Python!'

print('Length    :', len(s))
print('s[0]      :', s[0])       # first char
print('s[-1]     :', s[-1])      # last char
print('s[0:5]    :', s[0:5])     # 'Hello'
print('s[7:]     :', s[7:])      # 'Python!'
print('s[:5]     :', s[:5])      # 'Hello'
print('s[::2]    :', s[::2])     # every other char
print('s[::-1]   :', s[::-1])    # REVERSED


# In[13]:


# String operators
a, b = 'Hello', 'World'

print(a + ' ' + b)          # concatenation
print(a * 3)                 # repetition
print('ello' in a)           # membership → True
print('xyz' not in a)        # membership → True

# Lexicographic comparison
print('apple' < 'banana')    # True
print('ABC' == 'abc')        # False — case sensitive!
print('ABC'.lower() == 'abc')  # True — normalize first


# In[14]:


# split() — string → list
sentence = '  hello   world   python  '

# No arg: any whitespace, removes empty strings
print(sentence.split())                     # ['hello', 'world', 'python']

# With separator: exact match, KEEPS empty strings
csv = 'alice,bob,,carol'
print(csv.split(','))                       # ['alice', 'bob', '', 'carol']

# maxsplit — limit splits
path = 'usr/local/bin/python'
print(path.split('/', maxsplit=1))          # ['usr', 'local/bin/python']

# rsplit — split from the right
print(path.rsplit('/', maxsplit=1))         # ['usr/local/bin', 'python']


# In[15]:


# join() — list → string
# Called on the SEPARATOR, takes an iterable of strings
words = ['Hello', 'world', 'Python']

print(' '.join(words))            # space-separated
print(', '.join(words))           # comma-separated
print(''.join(words))             # no separator
print('\n'.join(words))           # each word on own line

# Numbers must be converted to str first
nums = [1, 2, 3, 4, 5]
print('-'.join(str(n) for n in nums))       # '1-2-3-4-5'

# Common pattern: split → process → join
text = 'hello world python'
result = ' '.join(w.capitalize() for w in text.split())
print(result)                              # 'Hello World Python'


# In[16]:


# strip() — remove leading/trailing characters
msg = '   Hello, Python!   '
print(repr(msg.strip()))          # both ends
print(repr(msg.lstrip()))         # left only
print(repr(msg.rstrip()))         # right only

# Custom char set
print(repr('###hello###'.strip('#')))         # 'hello'
print(repr('...hello!!!'.strip('.!')))        # 'hello'

# GOTCHA: strips any combination of the characters!
print(repr('pythonpy'.strip('py')))           # 'thon' — strips p, y, h from ends!


# In[17]:


# removeprefix() and removesuffix() — Python 3.9+
# Matches the EXACT substring — safe alternative
url = 'https://www.example.com'
print(url.removeprefix('https://'))     # 'www.example.com'
print(url.removeprefix('http://'))      # unchanged — no match, no error

fname = 'report_2025.pdf'
print(fname.removesuffix('.pdf'))       # 'report_2025'
print(fname.removesuffix('.docx'))      # unchanged

# The difference:
print('pypython'.strip('py'))           # 'thon'  — strips chars from both ends
print('pypython'.removeprefix('py'))    # 'python' — only removes if exact prefix


# ### `replace()` — Substitution

# In[18]:


text = 'bat ball bay'
print(text.replace('ba', 'ro'))           # all occurrences
print(text.replace('ba', 'ro', 1))        # only first

# Delete by replacing with empty string
print('Hello, World!'.replace(',', '').replace('!', ''))

# Normalize path separators
p = 'Users\\Alice\\Documents'
print(p.replace('\\', '/'))


# ### `casefold()` — Unicode-aware Normalization
# 
# > Use `casefold()` over `lower()` for any international text comparison.

# In[19]:


german = 'Straße'

print(german.lower())        # 'straße'  — ß preserved
print(german.casefold())     # 'strasse' — ß → ss

# Case-insensitive comparison
print('Straße'.casefold() == 'STRASSE'.casefold())   # True  ✓
print('Straße'.lower()    == 'strasse'.lower())       # False ✗

# Normalize user input
user = '  YES  '
if user.strip().casefold() == 'yes':
    print('User confirmed')


# ### `startswith()` and `endswith()` — Edge Checking
# 
# > ★ Tuple argument: check multiple prefixes/suffixes in one call.

# In[20]:


fname = 'report_2025.pdf'
print(fname.endswith('.pdf'))             # True
print(fname.startswith('report'))         # True

# Tuple argument — any match returns True
print(fname.endswith(('.pdf', '.docx', '.txt')))   # True
print(fname.startswith(('report', 'summary')))     # True

# Practical: file type validation
def is_image(f):
    return f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))

print(is_image('photo.JPG'))              # True
print(is_image('document.pdf'))           # False

# Comment detection
lines = ['# comment', 'x = 5', '// also comment', 'y = 10']
code_lines = [l for l in lines if not l.startswith(('#', '//'))]
print(code_lines)


# ### `splitlines()` — Multi-line Text

# In[21]:


multiline = 'Python is easy.\nPython is powerful.\nPython is fun.'
lines = multiline.splitlines()
print(lines)
print(f'Lines: {len(lines)}')

# Why NOT split('\n')?
windows_text = 'line1\r\nline2\r\nline3'    # Windows line endings
print(windows_text.split('\n'))            # ['line1\r', ...] ← \r stuck!
print(windows_text.splitlines())           # ['line1', 'line2', 'line3'] ✓

# keepends=True
print(multiline.splitlines(keepends=True))


# ### `count()` — Counting Occurrences

# In[22]:


text = 'python developer'
print(text.count('o'))            # 2 — all occurrences
print(text.count('o', 5))         # 1 — search from index 5
print(text.count('on'))           # 1 — counts substrings

# Non-overlapping!
print('aaa'.count('aa'))          # 1, not 2

sentence = 'the cat sat on the mat by the cat'
print(f"'the' appears {sentence.count('the')} times")
print(f"'cat' appears {sentence.count('cat')} times")

# In[23]:


print('apple' == 'apple')         # True
print('apple' == 'Apple')         # False — case sensitive!
print('apple' < 'banana')         # True — 'a' < 'b'
print('Z' < 'a')                  # True — uppercase < lowercase in Unicode!

# Sorting
words = ['banana', 'Apple', 'cherry', 'avocado']
print(sorted(words))                        # uppercase first
print(sorted(words, key=str.casefold))      # case-insensitive

# Membership check — case-insensitive
blocked = ['admin', 'root', 'system']
username = 'Admin'
if username.casefold() in [b.casefold() for b in blocked]:
    print(f"'{username}' is a blocked username")


# In[24]:


import io, sys

def simulate_input(mock):
    old = sys.stdin
    sys.stdin = io.StringIO(mock)
    result = input('Enter: ')
    sys.stdin = old
    return result

val = simulate_input('42\n')
print(f'Value: {repr(val)}, type: {type(val).__name__}')   # str, not int!
print(f'As int + 1: {int(val) + 1}')

# Real usage patterns:
# name = input('Enter your name: ')
# age  = int(input('Enter your age: '))
# pi   = float(input('Enter pi: '))


# In[25]:


# Simulated tokenization demo
line = '10 25 30 45 50'

numbers = list(map(int, line.split()))
print('Numbers:', numbers)
print('Sum:    ', sum(numbers))
print('Average:', sum(numbers) / len(numbers))

# Unpack with *rest
a, b, *rest = map(int, line.split())
print(f'First: {a}, Second: {b}, Rest: {rest}')


# In[26]:


# Type conversion gotchas
print(bool('False'))    # True  ← non-empty string is ALWAYS truthy!
print(bool(''))         # False ← only empty string is falsy
print(bool('0'))        # True  ← '0' is not the number 0

# The right way to parse boolean input:
def parse_bool(s):
    return s.strip().casefold() in ('yes', 'true', '1', 'y')

print(parse_bool('YES'))    # True
print(parse_bool('no'))     # False
print(parse_bool('True'))   # True


# In[27]:


def reverse_string(s):
    pass  # your code here

print(reverse_string('hello'))   # olleh
print(reverse_string('Python'))  # nohtyP
print(reverse_string(''))        # ''
print(reverse_string('a'))       # a


# In[28]:


# ── Solutions ──
def reverse_slice(s): return s[::-1]
def reverse_join(s):  return ''.join(reversed(s))
def reverse_loop(s):
    result = ''
    for ch in s:
        result = ch + result
    return result

for fn in [reverse_slice, reverse_join, reverse_loop]:
    print(fn('Python'))


# In[32]:


def is_palindrome(s):
    pass  # your code here

print(is_palindrome('racecar'))          # True
print(is_palindrome('hello'))            # False
print(is_palindrome('A'))               # True
print(is_palindrome('Race Car'))         # True
print(is_palindrome('Never odd or even')) # True


# In[33]:


# ── Solution ──
def is_palindrome(s):
    cleaned = ''.join(c for c in s.casefold() if c.isalnum())
    return cleaned == cleaned[::-1]

tests = ['racecar', 'hello', 'A', 'Race Car', 'Never odd or even']
for t in tests:
    print(f'{str(is_palindrome(t)):5} ← "{t}"')


# In[34]:


def count_vowels(s):
    pass

print(count_vowels('Hello World'))  # 3
print(count_vowels('Python'))       # 1
print(count_vowels('AEIOU'))        # 5
print(count_vowels('xyz'))          # 0


# In[35]:


# ── Solution ──
def count_vowels(s):
    return sum(1 for c in s.casefold() if c in 'aeiou')

# Alternative using count()
def count_vowels_v2(s):
    return sum(s.casefold().count(v) for v in 'aeiou')

for fn in [count_vowels, count_vowels_v2]:
    print(fn('Hello World'), fn('Python'), fn('AEIOU'))


# In[36]:


def word_frequency(sentence):
    pass

print(word_frequency('the cat sat on the mat by the Cat!'))


# In[37]:


# ── Solution ──
def word_frequency(sentence):
    cleaned = ''.join(c if c.isalnum() or c == ' ' else ' ' for c in sentence)
    words = cleaned.casefold().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

freq = word_frequency('the cat sat on the mat by the Cat!')
for word, count in sorted(freq.items(), key=lambda x: -x[1]):
    print(f'  {word:12} {count}')



# In[38]:


def caesar(text, shift):
    pass

print(caesar('Hello!', 3))     # Khoor!
print(caesar('Khoor!', -3))    # Hello!
print(caesar('xyz', 3))        # abc


# In[39]:


# ── Solution using translate() + maketrans() ──
def caesar(text, shift):
    shift = shift % 26
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table = str.maketrans(lower + upper,
                          lower[shift:] + lower[:shift] +
                          upper[shift:] + upper[:shift])
    return text.translate(table)

print(caesar('Hello, World!', 13))              # ROT13
print(caesar(caesar('Secret Message', 7), -7))  # encode → decode → original

for t in ['Hello!', 'xyz', 'Python 3.11']:
    encoded = caesar(t, 5)
    decoded = caesar(encoded, -5)
    print(f'  {t!r:20} → {encoded!r:20} → {decoded!r}')

