documents = [
	{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
	{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
	{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"} ]

directories = {
	'1': ['2207 876234', '11-2'],
	'2': ['10006'],
	'3': [] }	

print('Помощник секретаря v0.01')

def read_key():
	command_key = input('Введите команду:')
	if command_key in ['p', 's', 'l',  'a', 'd', 'm', 'as']:
		return command_key
	else:
		print('Введите корректную команду')

def people_document_number():
	document_number = input('Введите номер документа:')
	for docs in documents:
		for number in docs.values():
			if document_number == number:
				print(docs['name'])

def shelf_location():
	document_number = input('Введите номер документа:')
	for shelf_number in directories.items():
		for shelf_contains in shelf_number:
			for shelf in shelf_contains:
				if document_number == shelf:
					print('Этот документ лежит на полке №: ' + shelf_number[0])
				# else:
				# 	print('Документ не найден') #не знаю как заставить это работать

def list_documents():
	for docs in documents:
		# for values in docs.values():
		print(docs['type'] + ' "' + docs['number'] + '" "' + docs['name'] + '"')

def add_document():
	doc_type = input('Введите тип документа:')
	doc_number = input('Введите номер документа:')
	doc_name = input('Введите имя:')
	doc_shelf = input('На какую полку положить документ:')
	documents.append({'type': doc_type, 'number': doc_number, 'name': doc_name})
	directories[doc_shelf] += doc_number
	print(documents)
	print(directories)


def delete_document():
	print('d')

def move_document():
	print('m')

def add_shelf():
	print('as')

input_key = read_key()

if input_key == 'p':
	people_document_number()
elif input_key == 's':
	shelf_location()
elif input_key == 'l':
	list_documents()
elif input_key == 'a':
	add_document()
elif input_key == 'd':
	delete_document()
elif input_key == 'm':
	move_document()
elif input_key == 'as':
	add_shelf()
