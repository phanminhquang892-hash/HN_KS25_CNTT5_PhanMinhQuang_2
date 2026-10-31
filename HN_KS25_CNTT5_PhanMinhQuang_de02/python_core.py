raw_devices = [
    {'device_code': 'D301', 'type': 'laptop', 'price': 18500000, 'status': 'in_stock'},
    {'device_code': ' d101 ', 'type': 'phone', 'price': 6900000, 'status': 'in_stock'},
    {'device_code': 'D202', 'type': 'tablet', 'price': 9500000, 'status': 'out_of_stock'},
    {'device_code': 'D102', 'type': 'phone', 'price': 4200000, 'status': 'discontinued'},
    {'device_code': 'D302', 'type': 'laptop', 'price': 22000000, 'status': 'in_stock'}
]

def clean_and_validate_devices(devices):
    result = []
    for item in devices:
        code = item['device_code'].strip().upper()
        if len(code) < 2 or code[0] != 'D' or code[1:].isdigit() == False:
            continue
        new_item = item.copy()
        new_item['device_code'] = code
        result.append(new_item)
    return result

def search_devices(devices, max_price, status=None):
    result = []
    for item in devices:
        if item['price'] <= max_price and (status is None or item['status'] == status):
            result.append(item)
    return result

def sort_devices_by_price_desc(devices):
    result = devices.copy()
    for i in range(len(result) - 1):
        for j in range(len(result) - i - 1):
            if result[j]['price'] < result[j + 1]['price']:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

if __name__ == '__main__':
    cleaned = clean_and_validate_devices(raw_devices)
    print('Danh sách đã chuẩn hóa:', cleaned)
    print('Tìm kiếm:', search_devices(cleaned, 10000000, 'in_stock'))
    print('Sắp xếp giảm dần:', sort_devices_by_price_desc(cleaned))
