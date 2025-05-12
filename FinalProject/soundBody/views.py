from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
import json
from soundBody.models import CustomWorkoutPlan, Musician, WorkoutCompleteEntry


class CustomWorkoutPlanView(View):
    def get(self, request, musicianId):
        try:
            plans = CustomWorkoutPlan.objects.filter(musician__musicianId=musicianId)
            plans_data = [model_to_dict(plan) for plan in plans]
            return JsonResponse(plans_data, safe=False, status=200)
        except Musician.DoesNotExist:
            return JsonResponse({"error": "Musician not found"}, status=404)


@method_decorator(csrf_exempt, name="dispatch")
class WorkoutCompleteEntryView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            entry = WorkoutCompleteEntry.objects.create(
                musician_id=data["musicianId"],
                baseWorkoutPlan_id=data.get("baseWorkoutPlanId"),
                customWorkoutPlan_id=data.get("customWorkoutPlanId"),
                dateCompleted=data["dateCompleted"],
                totalDuration=data["totalDuration"],
                caloriesBurned=data["caloriesBurned"],
            )

            return JsonResponse(model_to_dict(entry), status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
