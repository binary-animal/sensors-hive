# API

Сообщение об ошибке всегда имеет следующий вид:

```
{
    "status": "ERROR",
    "error_msg": "%error_message%"    
}
```

Ответ на успешно выполненный запрос всегда имеет следующий вид:

```
{
    "status": "OK",
    "data": ...запрошенные данные...  
}
```    


## Авторизация

### Вход в систему

#### Запрос

```
POST /api/login

{
    "login": "%user_login%",
    "password": "%user_password%"    
}
```    
#### Ответ

```
"data": {
    "id": "%user_id%",
    "token": "%auth_token%"
}
```    

### Выход из системы

#### Запрос

```
POST /api/logout

{
    "token": "%auth_token%"
}
```    
#### Ответ

```
"data": {}
```

###  Обновление токена авторизации

#### Запрос

```
POST /api/newtoken

{
    "token": "%auth_token%"
}
```    
#### Ответ

```
"data": {
    "token": "%new_auth_token%"
}
```

## Получение структуры улья

### Получение списка сенсоров улья

#### Запрос

```
POST /api/sensors

{
    "token": "%auth_token%",
    "filters": {
        "ids": [
            %id1%,
            ...
            %idN%
        ],
        "groups": [
            %group_id1%,
            ...
            %group_idN%        
        ],
        "types": [
            %type1%,
            ...
            %typeN%  
        ],
        "location": {
            "long": "%longitude%",
            "lat": "%latitude%",
            "radius": "%radius%"
        }
    }
}
```    
#### Ответ

```
"data": [
    {
        "id": "%sensor_id%",
        "type": "%sensor_type%",
        "model": "%sensor_model%",
        "name": "%sensor_name%",
        "description": "%sensor_description%",
        "units": "%sensor_units%",
        "group": "%sensor_group_id%",
        "range": {
            "min": "%minimal_value%",
            "max": "%maximal_value%"
        },
        "location": {
            "long": "%longitude%",
            "lat": "%latitude%"
        },
        "value": "%current_value%",
        "controls": [
            {
                "id": "%control_id%",
                "type": "%control_type%",
                "name": "%control_name%",
                "description": "%control_description%",
                "units": "%control_units%",
                "range": {
                    "min": "%minimal_value%",
                    "max": "%maximal_value%"
                },
                "value": "%current_value%",
                "default_value": "%default_value%"
            },
            ...
        ]
    },
    ...
]
```

### Получение списка управляющих параметров улья

#### Запрос

```
POST /api/controls

{
    "token": "%auth_token%",
    "filters": {
        "ids": [
            "%id1%",
            ...
            "%idN%"
        ],
        "groups": [
            "%group_id1%",
            ...
            "%group_idN%"        
        ],
        "types": [
            "%type1%",
            ...
            "%typeN%"  
        ]
    }    
}
```    
#### Ответ

```
"data": [
    {
        "id": "%control_id%",
        "type": "%control_type%",
        "name": "%control_name%",
        "description": "%control_description%",
        "units": "%control_units%",
        "groups": [
            "%control_group_id1%",
            ...
            "%control_group_idN%",
        ],
        "range": {
            "min": "%minimal_value%",
            "max": "%maximal_value%"
        },
        "value": "%current_value%",
        "default_value": "%default_value%"
    },
    ...
]
```
### Получение списка групп сенсоров улья

#### Запрос

```
POST /api/sensorgroups

{
    "token": "%auth_token%",
    "ids": [
        "%id1%",
        ...
        "%idN%"
    ]    
}
```    
#### Ответ

```
"data": [
    {
        "id": "%sensor_group_id%",
        "name": "%sensor_group_name%",
        "description": "%sensor_group_description%",
        "sensors": [
            "%id1%",
            ...
            "%idN%"            
        ]
    },
    ...
]
```

### Получение списка групп управляющих параметров улья

#### Запрос

```
POST /api/controlgroups

{
    "token": "%auth_token%",
    "ids": [
        "%id1%",
        ...
        "%idN%"
    ]    
}
```

#### Ответ

```
"data": [
    {
        "id": "%control_group_id%",
        "name": "%control_group_name%",
        "description": "%control_group_description%",
        "controls": [
            "%id1%",
            ...
            "%idN%"            
        ]
    },
    ...
]
```

## Получение актуального состояния улья

#### Запрос

```
POST /api/state

{
    "token": "%auth_token%",
    "sensors": [
        "%sensor_id1%",
        ...
        "%sensor_idN%"
    ],
    "sensorgroups": [
        "%sensor_group_id1%",
        ...
        "%sensor_group_idN%"
    ],
    "controls": [
        "%control_id1%",
        ...
        "%control_idN%"
    ],
    "controlgroups": [
        "%control_group_id1%",
        ...
        "%control_group_idN%"
    ]
}
```

#### Ответ

```
"data": {
    "sensors": [
        {
            "id": "%sensor_id%",
            "value": "%sensor_current_value%"
        },
        ...
    ],
    "controls": [
        {
            "id": "%control_id%",
            "value": "%control_current_value%"
        },
        ...
    ]
}
```

## Получение данных по предыдущим состояниям улья

### Получение истории сенсора

#### Запрос

```
POST /api/sensorhistory

{
    "token": "%auth_token%",
    "id": "%sensor_id%",
    "from": "%from_time%",
    "to": "%to_time%",
    "limit": "%values_amount_limit%"
}
```

#### Ответ

```
"data": [
    {
        "time": "%time%",
        "value": "%value%"
    }
]
```

### Получение истории управляющего параметра

#### Запрос

```
POST /api/controlhistory

{
    "token": "%auth_token%",
    "id": "%control_id%",
    "from": "%from_time%",
    "to": "%to_time%",
}
```

#### Ответ

```
"data": [
    {
        "time": "%time%",
        "old_value": "%old_value%",
        "new_value": "%new_value%",
        "who_changed": "%user_id%"
    }
]
```

## Изменение актуального состояния улья

### Изменение значения управляющего параметра

#### Запрос

```
POST /api/changecontrol

{
    "token": "%auth_token%",
    "id": "%control_id%",
    "new_value": "%new_value%"
}
```

#### Ответ

```
"data": {
    "actual_value": "%actual_value%"
}
```

### Сброс значения управляющего параметра к значению по умолчанию

#### Запрос

```
POST /api/resetcontrol

{
    "token": "%auth_token%",
    "id": "%control_id%",
}
```

#### Ответ

```
"data": {
    "actual_value": "%actual_value%"
}
```

## Изменение структуры улья

## Сохранение и извлечение пользовательских настроек

## Администрирование пользователей

## Администрирование приложения

## Управление событиями, отчетами и автоматическими изменениями
