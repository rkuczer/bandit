from django.db import transaction, connections, connection


def foo(booking_id: str):
    with transaction.atomic():
        connections['default'].cursor().execute(f'SELECT pg_advisory_xact_lock({booking_id})')


def foo2(booking_id: str):
    with transaction.atomic():
        connection.cursor().execute(f'SELECT pg_advisory_xact_lock({booking_id})')


def foo3(booking_id: str):
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT pg_advisory_xact_lock({booking_id})')
