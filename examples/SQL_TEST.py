from django.db import transaction, connections, connection


def foo(booking_id: str):
    with transaction.atomic():
        connections['default'].cursor().execute(f"SELECT pg_advisory_xact_lock({booking_id}) FROM table")


def foo2(booking_id: str):
    with transaction.atomic():
        connection.cursor().execute(f"SELECT pg_advisory_xact_lock({booking_id}) FROM table")


def foo3(booking_id: str):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT pg_advisory_xact_lock({booking_id}) FROM table")



def foo4(booking_id: str):
    with connection.cursor() as cursor:
        cursor.execute('SELECT pg_advisory_xact_lock(%s) FROM table', [booking_id])


def foo5(col: str):
    with connection.cursor() as cursor:
        cursor.execute('SELECT %s FROM table', [col])


def foo6(col: str):
    q = 'SELECT %s FROM table'
    with connection.cursor() as cursor:
        cursor.execute(q, [col])


def foo7(col, booking_id):
    q = 'SELECT %s FROM table WHERE id = %s'
    with connection.cursor() as cursor:
        cursor.execute(q, [col, booking_id])
