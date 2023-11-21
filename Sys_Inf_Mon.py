# -*- coding: utf-8 -*-
import psutil
import time
import pyodbc
con = pyodbc.connect('Driver={SQL Server};'
                     'Server=local\SQLEXPRESS;' # local connection
                     'Database=System_information;'
                     'Truested_Connection=yes;')
cursor= con.cursor()
while 1==1:
    CPU_Usage = psutil.cpu_percent()
    Memory_Usage = psutil.virtual_memory()[2]
    cpu_interrupts = psutil.cpu_stats()[1]
    cpu_calls = psutil.cpu_stats()[3]
    
    memory_used = psutil.virtual_memory()[3]
    memory_free = psutil.virtual_memory()[4]
    
    bytes_sent = psutil.net_io_counters()[0]
    bytes_received = psutil.net_io_counters()[1]
    
    disk_usage = psutil.disk_usage('/')[3]
    
    cursor.execute('insert into Performance values (GETDATE(),'
                   + str(CPU_Usage) + ','
                   + str(Memory_Usage) + ','
                   + str(cpu_interrupts) + ','
                   + str(cpu_calls) +','
                   + str(memory_used) +','
                   + str(memory_free) +','
                   + str(bytes_sent) +','
                   + str(bytes_received) +','
                   + str(disk_usage) +')'
                   )
    con.commit()
    print(CPU_Usage, Memory_Usage, bytes_sent, bytes_received)
    time.sleep(1)
