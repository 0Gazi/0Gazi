from tinydb import TinyDB, Query
import uuid

# 2. TinyDB'yi başlatın ve JSON verisini yükleyin
db = TinyDB('db.json')
table = db.default('items')

# 3. Hedef öğeyi bul
target_item_id = 'buraya güncellemek istediğiniz öğenin UUID'
Item = Query()
target_item = table.get(Item.uuid == target_item_id)

# 4. UUID'yi güncelle
if target_item:
    new_uuid = str(uuid.uuid4())  # Yeni bir UUID oluşturun
    table.update({'uuid': new_uuid}, doc_ids=[target_item.doc_id])

# db.close()  # Eğer işiniz bittiğinde veritabanını kapatmanız gerekiyorsa bunu yapın.
