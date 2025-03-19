from rest_framework.permissions import BasePermission
from datetime import datetime

class GetOrPostPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'GET']:
            return True
        else :
            return False

class DeleteTwoMinutesPermission(BasePermission):
        def has_object_permission(self, request, view, obj):
            if request.method == 'DELETE' and obj.owner == request.user:
                time_limit = timezone.now() - obj.created_at
                if time_limit < timedelta(minutes=2):
                    return True
                return False
            return False

class WorkingDays(BasePermission):
        current_day = datetime.now().weekday()
        if 0 <= current_day <= 4:
            response_data ={"message": "API ishlamoqda"}
        else:
            response_data = {"message": "API faqat dushanbadan jumagacha ishlaydi"}

