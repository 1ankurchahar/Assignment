# Q1
def helper(from_row, from_column, to_row, to_column, map_matrix,visited):
	if not checkValid(from_row,from_column,map_matrix,visited): return False	
	if(from_row==to_row and from_column==to_column): return True
	visited[from_row][from_column]=True

	return helper(from_row+1,from_column,to_row,to_column,map_matrix,visited) or helper(from_row-1,from_column,to_row,to_column,map_matrix,visited) or helper(from_row,from_column+1,to_row,to_column,map_matrix,visited) or helper(from_row,from_column+1,to_row,to_column,map_matrix,visited)
def checkValid(row,col,map_matrix,visited):
    if row >= 0 and col >= 0 and row < len(map_matrix) and col < len(map_matrix[0]):
      if map_matrix[row][col] and not visited[row][col]:
        return True
    return False
def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    visited=[[False for _ in (map_matrix)] for _ in map_matrix[0]]
    return helper(from_row,from_column,to_row,to_column,map_matrix,visited)
if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];
    print(route_exists(0, 0, 2, 2, map_matrix))

# Q2
from collections import Counter
from collections import OrderedDict


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        ranks = [(-counter['score'], counter['games_played'], i, name)
                 for i, (name, counter) in enumerate(self.standings.items())]

        return sorted(ranks)[rank-1][3]


table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))

# Q3
import math
def find_roots(a, b, c):
    d=math.sqrt((b*b)-(4*a*c))
    if d > 0:
        return ((-b + d)/(2 * a),(-b - d)/(2 * a))
    else:
        return (-b / (2*a),-b / (2*a))
   

print(find_roots(2, 10, 8))

# Q4
import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])


def contains(root, value):
    if root is None:
        return False
    elif root.value == value:
        return True
    elif root.value >= value:
        return contains(root.left, value)
    else:
        return contains(root.right, value)


n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)

print(contains(n2, 3))


# Q5
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        playlist = {self}
        song = self.next
        while song:
            if song in playlist:
                return True
            else:
                playlist.add(song)
                song = song.next
        return False


first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second)
second.next_song(first)

print(first.is_repeating_playlist())

# Q6
def pipeline(*funcs):
	def helper(arg):
		ans=arg
		for func in funcs:
			ans=func(ans)
		return ans
	return helper
fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0


# Q7
def count_numbers(sorted_list, less_than):
	low,high=0,len(sorted_list)
	while(low<=high):
		mid=low + (high-low)//2
		if(less_than<=sorted_list[mid]): high=mid-1
		else: low=mid+1
	return low
if __name__ == "__main__":
	sorted_list = [1, 2, 5, 7]
	print(count_numbers(sorted_list, 4)) # should print 2



# Q8
def group_by_owners(files):
	ans={}
	for key,val in files.items():
		if val not in ans.keys():
			ans[val]=[key]
		else: ans[val].append(key)
	return ans	
if __name__ == "__main__":
	files = {
	'Input.txt': 'Randy',
	'Code.py': 'Stan',
	'Output.txt': 'Randy'
	}
	print(group_by_owners(files))

# Q9
class TextInput:
  ans=""
  def add(self,s):
    self.ans+=s
  def get_value(self):
    return self.ans
  
class NumericInput(TextInput) :
  def add(self,num):
    if(num.isnumeric()):
      self.ans+=num

if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())



# Q10

def find_two_sum(numbers, target_sum):
	seen={}
	for i in range(len(numbers)):
		if target_sum - numbers[i] in seen:
			return (seen[target_sum-numbers[i]],i)
		seen[numbers[i]]=i
	return None
if __name__ == "__main__":
	print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
