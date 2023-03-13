from db import get_connection

try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.excute('call VistaAlumno()')
        resultset=cursor.fetchall()
        for row in resultset:
            print(row)
except Exception as ex:
    print('Error')

#try:
    #connection=get_connection()
    #with connection.cursor() as cursor:
    #    cursor.execute('call agregarAlumno(%s,%s,%s)',())
    #    cursor.commit()
    #    cursor.close()
    #    resultset=cursor.fetchall()
    #    for row in resultset:
    #        print(row)
    pass
#except Exception as ex:
    pass