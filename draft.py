

"""
a = [1,2,3]

print(a[:2])
"""

coco_annotation = {
    'info': {
        'description': "ABC",
        'url': "abc.com",
        'version': '0.1',
        'year': 2018,
        'contributor': 'Hang Wu',
        'date_created': '2018/10/25',
    },
    'licenses': [
        {
        "url": "xyz.com",
        "id": 0,
        "name": 'MIT'
        }
    ],
    "images": [
        {

        }
    ],
    "annotations": [
        {

        }
    ],
    "categories": [
        {

        }
    ]
}

coco_annotation['annotations'] = [{"segmentation": [[479.0, 270.5, 484.5, 258.0, 489.5, 237.0, 488.5, 235.0, 
    490.5, 228.0, 493.5, 194.0, 492.5, 144.0, 490.5, 136.0, 481.5, 122.0, 473.0, 112.5, 467.0, 111.5, 463.5, 
    105.0, 458.0, 99.5, 443.0, 87.5, 419.0, 71.5, 415.0, 70.5, 397.0, 59.5, 376.0, 52.5, 356.0, 52.5, 325.0, 
    61.5, 330.5, 71.0, 330.5, 75.0, 339.5, 94.0, 346.5, 115.0, 349.5, 145.0, 348.5, 148.0, 351.5, 152.0, 349.5, 
    154.0, 349.5, 161.0, 354.5, 178.0, 356.5, 200.0, 359.5, 206.0, 354.5, 217.0, 355.5, 220.0, 373.0, 226.5, 
    386.0, 233.5, 392.0, 234.5, 394.0, 236.5, 406.0, 240.5, 410.0, 243.5, 430.0, 250.5, 448.0, 259.5, 459.0, 
    262.5, 472.0, 269.5, 479.0, 270.5]], "iscrowd": 0, "image_id": 0, "category_id": 1, "id": 0, "bbox": [325.0, 
    52.5, 168.5, 218.0], "area": 24163.75}]

print(coco_annotation)

