from django.core.exceptions import ObjectDoesNotExist
from django import template
from courts.models import Reservation
from datetime import datetime
from datetime import time
from datetime import timedelta
from django.utils.safestring import mark_safe
from django.urls import reverse

register = template.Library()


@register.simple_tag
def check_reservation(time_data, court, date_data, csrf_token):
    url = reverse("reserve")
    print(time_data, court, date_data)
    date_str = f"{date_data} {time_data}"
    datetime_object = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    try:
        reserv = Reservation.objects.get(court=court, start_time=datetime_object)
        return mark_safe(f"""           <td class="reserved">
                                            <strong>{reserv.type}</strong> <br> { reserv.user.username }
                                        </td>""")

    except Reservation.DoesNotExist:
        return mark_safe(f"""<td class="available">
                            <form method="POST" action="{url}">
                                    <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                                    <input type="hidden" name="court_id" value="{ court.id }">
                                    <input type="hidden" name="start_time" value="{datetime_object}">
                                    <input type="hidden" name="end_time" value="{datetime_object + timedelta(hours=1)}">
                                    <div class="form-group">
                                    <select name="reservation_type" class="form-control">
                                        <option value="regular">Zwykła</option>
                                        <option value="league">Liga Format</option>
                                        <option value="school">Trening</option>
                                        <option value="membership">ClubCard</option>
                                    </select>
                                </div>
                            <button type="submit" class="btn btn-success btn-sm">Zarezerwuj</button>,
                        </form>
                </td>""")
