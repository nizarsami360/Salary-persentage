import os
from dotenv import load_dotenv

# تحميل المتغيرات البيئية
load_dotenv()

# البيانات: الشهور والنسب التراكمية
MONTHS = [
    "Nov-21", "Dec-21",
    "Jan-22", "Feb-22", "Mar-22", "Apr-22", "May-22", "Jun-22", "Jul-22", "Aug-22", "Sep-22", "Oct-22", "Nov-22", "Dec-22",
    "Jan-23", "Feb-23", "Mar-23", "Apr-23", "May-23", "Jun-23", "Jul-23", "Aug-23", "Sep-23", "Oct-23", "Nov-23", "Dec-23",
    "Jan-24", "Feb-24", "Mar-24", "Apr-24", "May-24", "Jun-24", "Jul-24", "Aug-24", "Sep-24", "Oct-24", "Nov-24", "Dec-24",
    "Jan-25", "Feb-25", "Mar-25", "Apr-25"
]

CUMULATIVE_PERCENTAGES = [
    25.00, 45.00,
    65.00, 71.40, 91.40, 89.12, 103.66, 103.88, 111.49, 115.71, 122.14, 133.61, 145.93, 157.63,
    172.63, 183.00, 183.00, 203.00, 218.00, 233.00, 248.00, 258.00, 268.00, 318.00, 303.58, 343.58,
    378.58, 408.58, 458.58, 508.58, 548.58, 578.58, 608.58, 638.58, 668.58, 698.58, 728.58, 758.58,
    788.58, 818.58, 848.58, 948.58
]

# إعدادات المسؤول
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')

# أسماء الشهور
MONTH_NAMES = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
} 