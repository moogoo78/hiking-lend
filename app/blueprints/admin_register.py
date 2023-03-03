from app.models import (
    Store,
    Entity,
)

ADMIN_REGISTER_MAP = {
    'store': {
        'name': 'store',
        'label': '店家',
        'display': 'title',
        'resource_name': 'stores',
        'model': Store,
        'fields': {
            'title': { 'label': '名稱' },
            'latitude_decimal': { 'label': '緯度', 'type': 'text' },
            'longitude_decimal': { 'label': '經度', 'type': 'text' },
            'address': {'label': '地址', 'type': 'textarea'}
        },
        'list_display': ('title', 'latitude_decimal', 'longitude_decimal', 'address')
    },
    'entity': {
        'name': 'entity',
        'label': '物件',
        'display': 'name',
        'resource_name': 'entities',
        'model': Entity,
        'fields': {
            'name': { 'label': '名稱' },
            'status': { 'label': '狀態' },
            'store': { 'label': '店家', 'type': 'select', 'foreign': Store, 'display': 'title'},
        },
        'list_display': ('name', 'store', 'status')
    },
}
