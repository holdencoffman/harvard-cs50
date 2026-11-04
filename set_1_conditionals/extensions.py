response = input('Please enter file name below:\n').lower().strip()

search_list = {
   'gif': 'image/gif',
   'jpg': 'image/jpeg',
   'jpeg': 'image/jpeg',
   'png': 'image/png',
   'pdf': 'application/pdf',
   'txt': 'text/plain',
   'zip': 'application/zip'
}

ending_section = response.split('.')[-1]

result = search_list.get(ending_section)
if result:
   print(result)
else:
   print('application/octet-stream')