from intercom.client import Client

intercom = Client(personal_access_token='=')

all_users =intercom.users.all()

#Enter tag required
name_of_tag_required = ""


users_with_required_tag = []
#Leave blank
required_tag_id = ""

for tag in intercom.tags.all():
	if tag.name == name_of_tag_required:
		required_tag_id+= tag.id

	
	
for user in all_users:
	current_users_tags = user.tags
	for tag in current_users_tags:
		if tag.id == required_tag_id:
			users_with_required_tag.append(user.id)
	
