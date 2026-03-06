"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def pick(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    #<!--返回paragraghs列表中，符合select函数的第k个值--->

    # availuable_paragraghs_list=[]
    # for paragragh in paragraphs:
    #     if select(paragragh):
    #         availuable_paragraghs_list.append(paragragh)
    # if k < len(availuable_paragraghs_list):
    #     return availuable_paragraghs_list[k]
    # else:
    #     return ''
    # 构建一个都符合select的新列表，然后再返回列表中下标为k的值


    #第二种写法
    for single_paragraph in paragraphs: 
        if select(single_paragraph):
            k -= 1
            if k == -1:
                return single_paragraph
    return ''
    # 不新建列表，符合条件就k-1，把k看作处理的次数而非下表。    

    # END PROBLEM 1


def about(subject):
    """Return a select function that returns whether
    a paragraph contains one of the words in SUBJECT.

    Arguments:
        subject: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in subject]), 'subjects should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    #<!--about是一个高级函数，第一个参数传入想要搜索的词汇（列表），第二个传入一个片段（列表）-->

    def about_subject(paragraghs):
        processed_paragraphs = split(lower(remove_punctuation(paragraghs)))
        for single_subject in subject:
            if single_subject in processed_paragraphs:
                return True
        return False
    return about_subject
    # END PROBLEM 2


def accuracy(typed, source):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of SOURCE that was typed.

    Arguments:
        typed: a string that may contain typos
        source: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    source_words = split(source)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    #<!--输入typed和source为两个列表，处理过后得到以空格会划分的多元素列表，
    # typed和source中的位置必须一一对应，return正确的数量在source中的百分比，返回值为float-->

    total_count_of_accurate_words = 0

    for index in range(min(len(typed_words), len(source_words))):
        if typed_words[index] == source_words[index]:
            total_count_of_accurate_words += 1
    if len(typed_words) == 0 and len(source_words) == 0:
        return 100.0
    elif len(typed_words) == 0:
        return 0.0
    return ( total_count_of_accurate_words / len(typed_words) )  * 100

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # <!--elapsed是打字经过的时间，单位为秒。typed为列表，5个char为一组，算一个字。
    # return一分钟多少字-->

    count_of_characters = len(typed) /5
    return (count_of_characters / elapsed) * 60
    # END PROBLEM 4


############
# Phase 2A #
############


def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. If multiple words are tied for the smallest difference,
    return the one that appears closest to the front of WORD_LIST. If the
    difference is greater than LIMIT, instead return TYPED_WORD.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # assert all([lower(x) == x for x in typed_word]) and remove_punctuation(typed_word) == typed_word , "typed_word should be lowercase and shouldn't have punctuations."
    # assert all([lower(x) == x for x in word_list]) and remove_punctuation (word_list) == word_list , "word_list should be lowercase and shouldn't have puctuations."
    
    # 将diff_fuction改造为单变量函数single_input_diff_function
    # def single_input_diff_fuction(typed_word, limit):
    #     def inner(single_word_list):
    #         return diff_function(typed_word, single_word_list, limit)
    #     return inner
    # diff_function_for_min_key = single_input_diff_fuction(typed_word, limit)
    #
    # 条件判断主框架↓
    # if typed_word in word_list:
    #     return typed_word
    # else:
    #     if min([diff_function_for_min_key(_) for _ in word_list]) > limit:
    #         return typed_word
    #     else:
    #         return min(word_list, key = diff_function_for_min_key)

    # def single_input_diff_fuction(single_val_of_word_list):
    #     return diff_function(typed_word, single_val_of_word_list, limit)

    # if typed_word in word_list:
    #     return typed_word
    # else:
    #     temp = [single_input_diff_fuction(_) for _ in word_list]
    #     if min(temp) > limit:
    #         return typed_word
    #     else:
    #         return min(word_list, key = single_input_diff_fuction)
    
    # 1. 优先判断：typed_word直接在列表中，直接返回
    if typed_word in word_list:
        return typed_word
    
    # 2. 缓存所有单词的差异值（避免重复计算）
    diffs = [diff_function(typed_word, word, limit) for word in word_list]
    min_diff = min(diffs)
    
    # 3. 判断差异是否超过limit，或返回最小差异的第一个单词
    if min_diff > limit:
        return typed_word
    else:
        # 找到第一个最小差异的索引，返回对应单词
        min_index = diffs.index(min_diff)
        return word_list[min_index]

    # END PROBLEM 5


def feline_fixes(typed, source, limit):
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> feline_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> feline_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> feline_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> feline_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> feline_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    #assert False, 'Remove this line'
    if typed == source:
        return 0
    elif limit < 0:
        return 0
    elif len(typed) == 0 or len(source) == 0:
        return abs(len(typed) - len(source))
    elif typed[0] == source[0]:
        return feline_fixes(typed[1:], source[1:], limit)
    #elif limit >= 0:
    else:
        return 1 + feline_fixes(typed[1:], source[1:], limit - 1)
    # else:
    #     return 1
    # END PROBLEM 6


############
# Phase 2B #
############


def minimum_mewtations(typed, source, limit):
    """A diff function that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.
    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    #assert False, 'Remove this line'
    def add(typed, source, limit):
        return minimum_mewtations()
    def remove(typed, source, limit):
        return minimum_mewtations()

    if typed == source: # Base cases should go here, you may add more base cases as needed.
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END
    # Recursive cases should go below here
    if limit < 0: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return float('inf')
        # END
    if len(typed) == 0:
        return len(source) if len(source) <= limit else float('inf')
    if len(source) == 0:
        return len(typed) if len(typed) <= limit else float('inf')
    
    if typed[0] == source[0]:
        return minimum_mewtations(typed[1:], source[1:], limit)
    else:
        # BEGIN
        "*** YOUR CODE HERE ***"
        add = 1 + minimum_mewtations(typed, source[1:], limit - 1)
        remove = 1 + minimum_mewtations(typed[1:], source, limit - 1)
        substitude = 1 + minimum_mewtations(typed[1:], source[1:], limit - 1)
        min_edits = min(add, remove, substitude)
        return min_edits if min_edits <= limit else float('inf')
        # END


def final_diff(typed, source, limit):
    """A diff function that takes in a string TYPED, a string SOURCE, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'

FINAL_DIFF_LIMIT = 6 # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(typed, source, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        source: a list of the words in the typing source
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> source = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, source, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], source, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    for i in range(len(typed)):
        if typed[i] != source[i]:
            progress = i / len(source)
            upload({'id': user_id, 'progress': progress})
            return progress
    progress = len(typed) / len(source)
    upload({'id': user_id, 'progress': progress})
    return progress
        
    # END PROBLEM 8


def time_per_word(words, timestamps_per_player):
    """Given timing data, return a match data abstraction, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        timestamps_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> get_all_words(match)
    ['collar', 'plush', 'blush', 'repute']
    >>> get_all_times(match)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    time_cost_of_timestamps_per_player_2d_list = []
    for time_cost_per_word_per_player in timestamps_per_player:   #几个玩家就执行几次，几个玩家取决于timestamps_per_player的数量，timestamps_per_player是一个二维列表。其中每一个玩家的时间戳列表是其中的元素，也是一个列表。
        #对每一个玩家的时间戳列表进行计算
        time_cost_of_timestamps_per_player_2d_list.append([time_cost_per_word_per_player[i+1] - time_cost_per_word_per_player[i] for i in range(len(words))])  #每个玩家的时间戳列表中，前一个时间戳和后一个时间戳的差值就是打一个单词的时间。每个玩家打完所有单词的时间差值列表就是time_cost_of_timestamps_per_player_2d_list中的一个元素。
    return match(words, time_cost_of_timestamps_per_player_2d_list)
    # END PROBLEM 9


def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match data abstraction as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    player_indices = range(len(get_all_times(match)))  # contains an *index* for each player
    word_indices = range(len(get_all_words(match)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    fastest_words_per_player = [[] for _ in player_indices]  # 初始化一个二维列表，外层列表的长度等于玩家数量，内层列表初始为空，用于存储每个玩家打得最快的单词。
    for word_index in word_indices:  # 遍历每个单词的索引
        fastest_player_index = 0  # 初始化最快玩家的索引为0
        for player_index in player_indices:  # 遍历每个玩家的索引
            if time(match, player_index, word_index) < time(match, fastest_player_index, word_index):  # 如果当前玩家打这个单词的时间比当前记录的最快玩家还快
                fastest_player_index = player_index  # 更新最快玩家的索引
        fastest_words_per_player[fastest_player_index].append(get_word(match, word_index))  # 将这个单词添加到对应最快玩家的列表中
    return fastest_words_per_player  # 返回每个玩家打得最快的单词列表
    # END PROBLEM 10


def match(words, times):
    """A data abstraction containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return {"words": words, "times": times}


def get_word(match, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(get_all_words(match)), "word_index out of range of words"
    return get_all_words(match)[word_index]


def time(match, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(get_all_words(match)), "word_index out of range of words"
    assert player_num < len(get_all_times(match)), "player_num out of range of players"
    return get_all_times(match)[player_num][word_index]

def get_all_words(match):
    """A selector function for all the words in the match"""
    return match["words"]

def get_all_times(match):
    """A selector function for all typing times for all players"""
    return match["times"]


def match_string(match):
    """A helper function that takes in a match data abstraction and returns a string representation of it"""
    return f"match({get_all_words(match)}, {get_all_times(match)})"

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = pick(paragraphs, select, i)
        if not source:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(source)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, source))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)