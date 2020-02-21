CANCEL = 0
NEW = 1
IN_PROCESSING = 2
COMPLETED = 4
ORDER_STATUS_CHOICES = [
    (CANCEL, 'Cancel'),
    (NEW, 'New'),
    (IN_PROCESSING, 'In-processing'),
    (COMPLETED, 'Completed')
]

DISPATCH_STATUS_ORDER = [
    (CANCEL, 'Cancel'),
]

DRIVER_STATUS_ORDER = [
    (COMPLETED, 'Completed'),
]
