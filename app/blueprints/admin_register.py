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
        },
        'list_display': ('title',)
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
        },
        'list_display': ('name', 'status')
    },
}
