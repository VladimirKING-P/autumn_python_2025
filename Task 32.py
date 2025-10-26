#todo: Вы пишете скрипт для очистки временных файлов. Создайте список полных путей к временным файлам (с расширениями .tmp, .bak),
# добавив к каждому путь "/tmp/".


files = [
    "document.pdf",
    "temp_backup.tmp",
    "image.jpg",
    "cache.tmp",
    "report.docx",
    "old_data.bak"
]

extension = {'.tmp', '.bak'}
paths_to_temp_files = []

for file in files:
    if any(file.endswith(ext) for ext in extension):
        paths_to_temp_files.append(f"/tmp/{file}")

print(paths_to_temp_files)
