# messages first
messages = []

def get_messages():
	return messages
	
def create_message(name, message):
	name = name[:70]
	message = message[:999]
	new_message = {
		"id": len(messages),
		"name": name,
		"text": message
	}
	messages.append(new_message)
	print(new_message)
	return new_message
	
def update_message(id, new_name, new_message):
	if messages["id"]: #if it exists
		new_message = {
			"id": id,
			"name": new_name,
			"text": new_message
		}
		messages["id"] == new_message
	else:
		new_message = create_message("Fez", "Someone tried to update non-existent message #{0} with name '{1}', and text '{2}'.")
	print(new_message)
	return new_message

def delete_message(id):
	global messages
	if id == "all":
		messages = []
	else:
		messages.pop(int(id))
	return messages
		
