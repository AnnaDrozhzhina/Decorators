#Применить написанный логгер к приложению из любого предыдущего д/з.

from Second_task import logger

list_of_lists_1 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]

@logger(path='task_3.log')
def flat_generator(list_):
	for el in list_:
		for i in el:
			yield i

res = []

for item in flat_generator(list_of_lists_1):
	res.append(item)

if __name__ == '__main__':
    print(res)







